import eel

import win32clipboard as w32c
import requests as req
from requests_oauthlib import OAuth1
import json
import pyttsx3
import base64

NAME = 'ggetgget60'
KEY = '8e6eb7ccebb147bbc5d50f1b4d939f64062c407c1'
SECRET = 'ec49eaf43f2757131685bc2af9a74626'
URL = 'https://mt-auto-minhon-mlt.ucri.jgn-x.jp/api/mt/generalNT_en_ja/'

consumer = OAuth1(KEY , SECRET)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)

pre_seq = None

def read():
    try:
        w32c.OpenClipboard()
        return w32c.GetClipboardData()
    except Exception as ex:
        return ex
    finally:
        w32c.CloseClipboard()

def load_dict(path):
    dic = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line[:-1].split('\t')
            dic[line[0]] = line[1]
    return dic

def translate(text):
    params = {
        'key': KEY,
        'name': NAME,
        'type': 'json',
        'text': text
    }    # その他のパラメータについては、各APIのリクエストパラメータに従って設定してください。

    try:
        res = req.post(URL , data=params , auth=consumer)
        res.encoding = 'utf-8'
        dic = json.loads(res.text)["resultset"]
        result_text = dic["result"]["text"]
        return result_text

    except:
        return ''

def onchange(data):
    if isinstance(data, Exception):
        print("Failed:", data)
    else:
        key = data.lower()
        print()
        print("Clipboard:", data.lower())
        if key!='' and key in dic.keys(): # 辞書に結果がある時
            words = dic[key].split('/')
        else:
            words = []
        trans_text = translate(data)
        return {"key":key, "words":words, "translate":trans_text}

def save_mp3(data):
    engine.save_to_file(data, 'web/tmp.mp3')
    engine.runAndWait()


dic = load_dict('dic/ejdict-hand-utf8.txt')

eel.init('web')

def my_other_thread():
    while True:
        eel.sleep(1.0)                  # Use eel.sleep(), not time.sleep()

eel.spawn(my_other_thread)

eel.start('index.html', block=False)     # Don't block on this call

def main(pre_seq):
    while True:
        seq = w32c.GetClipboardSequenceNumber()

        if pre_seq != seq:
            data = read()
            pre_seq = seq

            result = onchange(data)
            save_mp3(data)
            eel.transport_json(result)
        eel.sleep(1.0)


if __name__ == '__main__':
    main(pre_seq)