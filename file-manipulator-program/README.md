# File Manipulator Program

## 準備

```bash
❯ echo file manipulator program > testfile
❯ cat testfile

file manipulator program
```

## reverseコマンド

```bash
❯ python3 main.py reverse testfile reversefile
❯ cat reversefile

margorp rotalupinam elif
```

## copyコマンド

```bash
❯ python3 main.py copy testfile copyfile
❯ cat copyfile

file manipulator program
```

## duplicate-contentsコマンド

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

```bash
❯ python3 main.py replace-string testfile test "application"
❯ cat testfile

file manipulator application
file manipulator application
file manipulator application
file manipulator application
file manipulator application
```