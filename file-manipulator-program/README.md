# File Manipulator Program

## 概要

*RecursionCS*のバックエンドプロジェクトで、コードをコマンドラインから実行可能なプログラムに変換する方法を学ぶために取り組みました。

また、コマンドラインからプログラムに直接引数を渡して、以下4つの出力を生成する方法を学びました。

プロジェクトの仕様が与えられ、コードは全て自分で記述しました。

## 準備

```bash
❯ echo file manipulator program > testfile
❯ cat testfile

file manipulator program
```

## reverseコマンド

reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成

```bash
❯ python3 main.py reverse testfile reversefile
❯ cat reversefile

margorp rotalupinam elif
```

## copyコマンド

copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存

```bash
❯ python3 main.py copy testfile copyfile
❯ cat copyfile

file manipulator program
```

## duplicate-contentsコマンド

duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製

```bash
❯ python3 main.py duplicate-contents testfile 5
❯ cat testfile

file manipulator program
file manipulator program
file manipulator program
file manipulator program
file manipulator program
```

## replace-stringコマンド

replace-string inputpath needle newstring: inputpath' にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換える

```bash
❯ python3 main.py replace-string testfile program "application"
❯ cat testfile

file manipulator application
file manipulator application
file manipulator application
file manipulator application
file manipulator application
```