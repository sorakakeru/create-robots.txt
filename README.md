# create-robots.txt

指定サイト分のrobots.txtを生成します。

## 使い方

1. `/src/config.py`で以下を設定する

- key: `robots.txt`を生成するディレクトリ（サイト名でなくてもOK）
- value(list): `Disallow`に指定するディレクトリやファイルなど
  - `User-agent: *`に対して設定されます

> [!NOTE]
> 生成される`robots.txt`は、上記の指定と各AIクローラーbot（使用ライブラリ参照）の`Disallow`指定が書き込まれます。

1. `main.py`を実行する

`main.py`と同階層に`dist`フォルダが作成され、その中に`key`で指定したディレクトリと`robots.txt`が生成されます。

## 使用ライブラリ

AIbotの指定には、[ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt)の`robots.json`を使用しています。

## ライセンス

MIT License
