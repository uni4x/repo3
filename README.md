# イベント管理アプリ

## 概要
このプロジェクトは、家族や友人間での予定共有を目的としたイベント管理アプリケーションです。DjangoとFullCalendarを使用して、カレンダー表示、イベントの追加・編集、コメント機能を提供します。

## 機能
- ユーザー登録およびログイン機能
- FullCalendarを使用したカレンダー表示
- イベントの追加、編集、削除
- 他のユーザーのイベントにコメントを追加
- ユーザーごとにカスタムカラー設定

## インストール
このプロジェクトをローカル環境にインストールする手順です。

### 前提条件
- Python 3.6以上
- pip (Pythonのパッケージ管理ツール)

### 手順
1. リポジトリをクローンします。
    ```bash
    git clone https://github.com/username/event-management-app.git
    cd event-management-app
    ```

2. 仮想環境を作成して有効化します。
    ```bash
    python3 -m venv env
    source env/bin/activate  # macOS/Linux
    env\Scripts\activate  # Windows
    ```

3. 必要なパッケージをインストールします。
    ```bash
    pip install -r requirements.txt
    ```

4. データベースのマイグレーションを実行します。
    ```bash
    python manage.py migrate
    ```

5. 開発サーバーを起動します。
    ```bash
    python manage.py runserver
    ```

6. ブラウザでアプリケーションにアクセスします。
    ```
    http://127.0.0.1:8000/
    ```

## 使用方法
### ユーザー登録
1. `Sign Up` ページにアクセスして、新しいユーザーを登録します。
2. 登録後、ログインページにリダイレクトされます。

### イベントの追加
1. カレンダーページで日付をクリックして、イベントを追加します。
2. イベントの詳細を入力し、保存します。

### コメントの追加
1. イベントをクリックして、イベント詳細ページに移動します。
2. コメントを入力し、追加します。

## カスタムカラーの設定
1. `Update Color` ページにアクセスします。
2. カラーを選択し、保存します。

## 貢献
貢献を希望される方は、以下の手順に従ってください。

1. リポジトリをフォークします。
2. 新しいブランチを作成します。
    ```bash
    git checkout -b feature-branch
    ```
3. 変更をコミットします。
    ```bash
    git commit -m 'Add some feature'
    ```
4. ブランチにプッシュします。
    ```bash
    git push origin feature-branch
    ```
5. プルリクエストを作成します。

## ライセンス
このプロジェクトポートフォリオです。