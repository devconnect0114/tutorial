# DevConnectチュートリアルプロジェクト

## 目次

- [環境設定](#環境設定)
- [レポジトリのclone](#レポジトリのclone)
- [サンプルアプリ開発](#サンプルアプリ開発)
- [gitコミットとGitHubへpush](#gitコミットとGitHubへpush)

## 環境設定

### phpのインストール

#### Macの場合

- pyenvをインストール

```
brew install pyenv
```

- pathを通す

```
echo $SHELL
/usr/local/bin/zsh # <- zsh使ってる
```

zshを使っている場合は~/.zshrcに、
bashを使っている場合は、~/.bash_profileに下記コードを追加。

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

shellの設定を読み込ませる。

```
# bashの場合
source ~/.bash_profile

# zshの場合
source ~/.zshrc
```

- Python 3.12.4をインストール

```
pyenv install 3.12.4
```

- 使用するpythonのバージョンを指定

```
tomioka-s@tommys-MacBook-Pro sample % pyenv versions
  system
* 3.12.4 (set by /Users/tomioka-s/Documents/DevConnect/sample/.python-version)
```

python 3.12.4を設定する。

```
# localで設定
pyenv local 3.9.9
```

pythonバージョンの確認。

```
python --version

Python 3.12.4 # <- 設定されている
```

### gitおよびsourcetreeのインストール

```
brew install git
brew install --cask sourcetree
```

sourcetreeはGitをGUIで操作するためのツールになります。

## レポジトリのclone

- SSHキー設定（初回のみ）

```
ssh-keygen -t ed25519 -N ""
# 秘密鍵と公開鍵が作成されていることを確認
ls ~/.ssh
id_ed25519  id_ed25519.pub
```

- GitHubに公開鍵を登録

```
# クリップボードに公開鍵をコピー
pbcopy < ~/.ssh/id_ed25519.pub
```

GitHubの公開鍵の設定画面を開く
https://github.com/settings/keys
New SSH key
Title を適当に入力する(PC名を入れておくと鍵管理しやすい)
Key にクリップボードにコピーした公開鍵を貼り付ける
Add SSH Key で鍵を登録する

- 確認

```
ssh -T github.com
Warning: Permanently added 'github.com,52.69.186.44' (RSA) to the list of known hosts.
Hi xxx! You've successfully authenticated, but GitHub does not provide shell access.
```

- GitHubからclone

```
git clone git@github.com:devconnect0114/tutorial.git
```

## サンプルアプリ開発

- Pythonの仮想環境を作成

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

- Flaskをインストール

```
pip install Flask
```

- アプリケーションの作成

以下ソースコードをコピーして、任意の名前をつけて下さい。

```
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    name = 'World'
    if request.method == 'POST':
        name = request.form['name']
    
    template = '''
    <!doctype html>
    <html>
    <head>
      <title>Hello App</title>
    </head>
    <body>
      <h1>Hello, {{ name }}!</h1>
      <form method="post">
        <input type="text" name="name" placeholder="Enter your name" />
        <input type="submit" value="Submit" />
      </form>
    </body>
    </html>
    '''
    return render_template_string(template, name=name)

if __name__ == '__main__':
    app.run(debug=True)
```

このスクリプトでは、基本的なHTMLフォームを用いてユーザー名を受け取り、サーバーがその名前を使って応答します。

- アプリケーションの実行

```
python [任意の名前].py
```

ブラウザを開いて http://127.0.0.1:5000/ にアクセスすると、アプリケーションが表示されます。フォームに名前を入力して送信すると、ページに「Hello, [入力した名前]!」と表示されます。

## gitコミットとGitHubへpush

- 先ほど任意の名前でつけたファイルをsourcrtreeを使ってgitコミットとGitHubへpushをする