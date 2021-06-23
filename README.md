# Python Whl Package Update and Extract Tools
*PythonのWHLパッケージ用アップデートツールとWHLパッケージ自動解凍ツール*

## 使い方
`python3 WHLAutoExtracter.py`

`python3 WHLPackageUpdateTool.py`

## 補足
*「WHLPackageUpdateTool」はオプションが幾つかあり*

*-h/--help: ヘルプを出します。*

*-l/--list: アップデートのあるパッケージをリストアップします。*

*-d/--download: アップデートのあるwhlパッケージをダウンロードします。*

*-u/--update: アップデートのあるwhlパッケージを一括アップデートします。*

*となっており、「WHL Extracter」の方はwhlパッケージがあるディレクトリで実行していただくとディレクトリ内のwhlパッケージが全て解凍されます。*

## 開発秘話
*実はパッケージアップデートツール自体は他にもありまして「pip-review」というモジュールがすでに存在しています。*

*しかし、「pip-review」は手動や「tar.gz」形式で追加したパッケージもアップデートするという機能なため、*

*配布サイトに無い場合はエラーが出たりして止まっていたのでこれを解消すべく作ったのが始まりでした。*

*実はパッケージリストを取得する時にsubprocessモジュールを使っているのですが、*

*subprocessモジュールなしでリストアップする「sys.__stdout__」を使った手法が昔あり、以前はそれを使っていました。*

*しかし、githubに載せる以上昔の手法を載せるのはよくないと考えたので、githubに載せているものはsubprocessモジュールを使っています。*
