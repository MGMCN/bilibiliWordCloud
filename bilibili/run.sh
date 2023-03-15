rm -rf comments.txt;
rm -rf .env;
touch .env;
echo "media_id=$1" >> .env
scrapy crawl bilibilicomment;
python3 generateWordCloud.py