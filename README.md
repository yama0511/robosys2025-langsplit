## 必要な環境
* Python 3.7+
* Linux (Tested on Ubuntu 20.04 / 22.04)

## 使用方法

### 基本的な使い方
パイプを使って標準入力からテキストを渡します。

```bash
$ echo -e "Hello World\nこんにちは" | ./langsplit
Hello World
こんにちは   <-- (標準エラー出力)


