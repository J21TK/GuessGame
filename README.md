# Introduction
## GuessGame
You can try to guess the secret number this program has.

## GuessGame_2 and Variations
Same as GuessGame, but this is simulator (You cannot play the game).
GuessGame_2 includes the fundamental functions,
and Variations includes some developped codes (inherited from GuessGame_2).
All of the results with this simulator are in the "results" directory.

## GuessGame_3
This is the opposite game of GuessGame;
You have a secret number, and this program try to guess it.


# results directory
## IndividualGraph
This code will read all of the .txt files in the same directory, and make a graph per one text file.
()
Pandas, numpy, and matplotlib libraries are required

# 現状
## 今できること
wx_main.pyをrun --> メニューバーの「新規作成」をクリック --> csvファイルをファイルダイアログから選択 --> そのファイルの中身を表とグラフとして別々に表示

## 作製可能グラフ
xyグラフ、棒グラフ

## 課題
1. 表とグラフのウィンドウを紐付けする（片方閉じたらもう片方も閉じる、みたいな）
2. 表で値を変更したら、グラフにもそれが反映するようにする
3. 保存できるようにする
4. 2群グラフ形式
5. 棒グラフの色を各群で別にする
6. 統計処理、有意差マークの自動付加
