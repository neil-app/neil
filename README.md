# neil

## 初回
- `$ cp .envrc.sample .envrc`
- `$ docker-compose build`
- ToDo db create(一旦手動)

## 起動
- frontend, backend, db起動
    - `$ docker-compose up`
- frontend起動
    - `$ make web`
- backend起動
    - `$ make web_backend`
- db起動
    - `$ docker-compose up db`

## migration
`app/`で行う
- migrationファイルの作成
    - `$ flask db migrate`
- migrationの実行
    - `$ flask db upgrade`
- migrationのrollback
    - `$ flask db downgrade`

