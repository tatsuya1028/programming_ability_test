### gitの使い方

- リモートから最新ソースコードをとってくる
git pull


- ソースコードをリポジトリに保存
    - modifiedが赤色になってることの確認
        - git status
    - git addをする
    - modifiedが緑色になってることの確認
    - コメント打ち込んでコミット
        - git commit -m "何かしらのコメント"
    - git pushする
        - git push origin fetaure/tatuya


    - 使うコマンド一覧
    ```bash
    git status
    git add .
    git commit -m "何かしらのコメント"
    git push origin fetaure/tatuya
    ```