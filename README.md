# langsplit

[![test](https://github.com/yama0511/robosys2025-langsplit/actions/workflows/test.yml/badge.svg)](https://github.com/yama0511/robosys2025-langsplit/actions/workflows/test.yml)

標準入力から読み込んだテキストを解析し、**英語の行**と**日本語の行**に分離して出力するコマンドラインツールです。

* **英語（ASCII文字主体）** → 標準出力 (stdout)
* **日本語（マルチバイト文字主体）** → 標準エラー出力 (stderr)

## 概要
このコマンドは、ログファイルや混合テキストデータから、特定の言語の行だけを抽出したい場合に便利です。UNIX哲学に基づき、標準入出力を利用しているため、パイプライン処理に組み込んで使用できます。

## 必要な環境
* **OS:** Linux (Ubuntu 20.04 / 22.04 LTS で動作確認済み)
* **言語:** Python 3.7 以上

## 使用方法

### 1. 基本的な使い方
*パイプを使ってテキストを渡すと、画面上で分離されて表示されます。

```bash
$ echo -e "Hello World\nこんにちは\nPython script" | ./langsplit
```

Hello World
Python script
こんにちは    <-- (標準エラー出力として表示)
2. ファイルへの保存（リダイレクト）
*標準出力と標準エラー出力を別々のファイルに保存することで、完全に分離できます。

```bash
$ cat mixed_log.txt | ./langsplit 1> english.txt 2> japanese.txt
```

3. ヘルプの表示
* オプション --help で使い方が表示されます。

```bash
$ ./langsplit --help
```
## インストール
* このリポジトリをクローンし、実行権限を付与してください。

```bash
$ git clone [https://github.com/yama0511/robosys2025-langsplit.git](https://github.com/yama0511/robosys2025-langsplit.git)
$ cd robosys2025-langsplit
$ chmod +x langsplit
```
## ライセンス
* このソフトウェアは、BSD 3-Clause License の下で公開されています。 詳細については LICENSE をご確認ください。
* © 2025 Yamato Okada
