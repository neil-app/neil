# neil

## 環境変数
`.envrc`で管理
clone後の初回のみ`cp .envrc.sample .envrc`

## migration
`app/`で行う
- migrationファイルの作成
    - `flask db migrate`
- migrationの実行
    - `flask db upgrade`
- migrationのrollback
    - `flask db downgrade`
