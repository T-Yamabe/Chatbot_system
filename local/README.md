# AIチャットボットシステム_国内PoC
このディレクトリは、ローカルサーバー環境に向けたリソースを格納しています。  
AIチャットボットシステムに認証機能を追加し、ユーザーのアクセスを管理することを目的とします。

## 機能

### 認証機能
- **ログイン画面**: Gradioの標準認証機能を使用したログイン機能
- **パスワード変更**: ユーザーが自身でパスワードを変更できる機能

### セキュリティレベル
- パスワードは`Argon2`でハッシュ化したデータを`users.json`に保存します。
- パスワードの要件は下記の通りです。
  - 最低12文字以上
  - 大小英数字および記号を組み合わせることを必須
  - 全角文字は使用不可

  使用可能な記号一覧：**! " # $ % & ' ( ) * + = - / < > _ ~ ^ : ; , . ? @ \ | [ ] { } `**

## 使い方（ビルド方法）

### 各種ファイルの説明
- `launch_gradio_system_ver.py`：`NLP_PPH_Chatbot_System/NLP_PPH_chatbot/chatbot/chatbot/launch_gradio.py`に認証機能を追加したPythonファイル
- `users.json`：ユーザー認証情報を記載したJSONファイル

> [!Warning]
> `users.json`には機密情報（ハッシュ化されたパスワード）が含まれるため、適切に管理してください。

### users.jsonのフォーマット
`users.json`ファイルは以下の形式で記述します。

```json
{
  "user_id": "hashed_password"
}
```
- `user_id`: ユーザーID
- `hashed_password`: Argon2でハッシュ化されたパスワード

> [!NOTE]
> パスワード発行については、専用のプログラムと手順書を別途用意します。詳細は以下のファイルを参照してください。
> - パスワード発行プログラム：`password_generator.py`
> - 発行手順書：`password_generation_guide.md`

### users.jsonが利用される流れ
- ログイン認証時：`launch_gradio_system_ver.py`内でログイン認証を行うときに`users.json`を読み込み、入力されたユーザー名・パスワードと照合します。
- パスワード変更時： `launch_gradio_system_ver.py`内でパスワード変更機能が実行されるときに`users.json`を読み込み、パスワードの検証、および更新します。

### 1. ファイルのコピー
`launch_gradio_system_ver.py`と`users.json`をサブモジュール内のディレクトリにコピーします。  
コピー先は`NLP_PPH_Chatbot_System/NLP_PPH_chatbot/chatbot/chatbot/`です。

```bash
# launch_gradio_system_ver.pyとusers.jsonをサブモジュールにコピー
# /NLP_PPH_Chatbot_System/localで実行
# launch_gradio_system_ver.pyはlaunch_gradio.pyを上書き
cp launch_gradio_system_ver.py ../NLP_PPH_chatbot/chatbot/chatbot/launch_gradio.py
cp users.json ../NLP_PPH_chatbot/chatbot/chatbot/
```

### 2. Gradioアプリケーションの実行
サブモジュールディレクトリ(NLP_PPH_chatbot)に移動し、NLP_PPH_chatbot/chatbot/README.mdの手順に従ってGradioを起動してください。

> [!NOTE]
> サブモジュール`NLP_PPH_chatbot`の具体的な実行方法については、`NLP_PPH_chatbot`内のドキュメントを参照してください。

## ディレクトリ構成

```
NLP_PPH_Chatbot_System/
  ├── local/
  │     ├── launch_gradio_system_ver.py    # コピー元
  │     └── users.json                     # コピー元
  └── NLP_PPH_chatbot/ (サブモジュール)
        └── chatbot/
            └── chatbot/
                ├── launch_gradio.py       # コピー先（リネーム）
                └── users.json             # コピー先
```
