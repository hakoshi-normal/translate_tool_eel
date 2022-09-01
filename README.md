# translate_tool_eel

現在プロトタイプの辞書検索/翻訳アプリ．

Chromeの某翻訳拡張機能の紹介を見かけて欲しかったので似たようなのを自作してみました．  
Chrome拡張機能を作成しようとも思いましたが2023年1月にmanifest v2が廃止されマニュアルが乏しいv3への移行が強制されるため，今回はデスクトップアプリとしました．  
ただ，GUI作成が面倒なのでPythonからchromiumが触れるeelを利用しました．

## 動作環境
Windowsのみ．Pythonにeel, requests, requests_oauthlibをPyPIから導入してapp.pyを実行すると動くと思います．Google Chromeで動作確認済み  
（後日requirements.txtもちゃんと書きたい）

## 操作
操作は翻訳したい英単語，英文をクリップボードにコピーするだけです．  
自動で辞書引きと機械翻訳を行い，結果をブラウザウィンドウに表示します．

## 利用翻訳サービス
パブリックドメインの英和辞書データ「ejdict-hand」
https://github.com/kujirahand/EJDict

みんなの自動翻訳＠TexTra®
https://mt-auto-minhon-mlt.ucri.jgn-x.jp/content/menu/

## 今後
ある程度見やすいインタフェースにしたい．  
インターバルの調整．  
かなり雑にコーディングを勧めたためapp.pyがハチャメチャに見づらい．なんとかする．  
en→jaだけでなくその逆や別言語にも対応したい．  
発音記号を表示したい．  
読み上げ機能をつけたい．  
StarDictのバイナリが読めれば，より多彩な情報提供が可能となるため，試してみたい．
