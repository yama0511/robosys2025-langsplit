# langsplit

[![test](https://github.com/yama0511/robosys2025-langsplit/actions/workflows/test.yml/badge.svg)](https://github.com/yama0511/robosys2025-langsplit/actions/workflows/test.yml)

標準入力から読み込んだテキストを解析し、**ASCII文字主体の行**と**それ以外の文字（日本語など）主体の行**に分離して出力するコマンドラインツールです。

* **ASCII文字（英数字・半角記号）** → 標準出力 (stdout)
* **その他の文字（日本語・全角文字）** → 標準エラー出力 (stderr)

## 概要
このコマンドは、ログファイルや混合テキストデータから、文字種別ごとに行を抽出したい場合に便利です。

## 必要な環境
* **OS:** Linux (Tested on Ubuntu 20.04 / 22.04 / 24.04)
* **言語:** Python 3.7 以上

## 使用方法

### 1. 基本的な使い方
パイプを使ってテキストを渡すと、画面上で分離されて表示されます。

```bash
echo -e "Hello World\nこんにちは\nPython script" | ./langsplit
```

Hello World
Python script
こんにちは    <-- (標準エラー出力として表示)

### 2. ファイルへの保存（リダイレクト）
標準出力と標準エラー出力を別々のファイルに保存することで、完全に分離できます。
```bash
cat mixed_log.txt | ./langsplit 1> ascii.txt 2> others.txt
```

## インストール
このリポジトリをクローンし、実行権限を付与してください。

```bash
git clone https://github.com/yama0511/robosys2025-langsplit.git

cd robosys2025-langsplit

chmod +x langsplit
```

## ライセンス
このソフトウェアは、BSD 3-Clause License の下で公開されています。 詳細については LICENSE をご確認ください。

## Copyright
(C) 2025 Yamato Okada
