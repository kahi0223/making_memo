# making_memo

## overview

指定した時間ひたすらメモを書き続ける。Windows用。

## usage

バッチファイルをクリックで実行。

作動中、コマンドラインで任意のキーボードを打つと停止する。

任意のキーボードを押した時もしくは指定した最大時間が過ぎた時、メモ帳が保存せずに終了、その後Enteeを推すとコマンドラインも閉じる。

時間を変更したいときはpythonスクリプトの`MAX_HOUR`を変更。


## sub module

- mouse_move: 指定した座標分マウスを動かす。
