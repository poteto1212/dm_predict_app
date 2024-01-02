#dockerのビルド
docker-compose build
#dokcerの起動
docker-compose up -d
#テスト
docker-compose run app pytest
#docker停止
docker-compose down
