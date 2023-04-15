pip install -r ../requirements.txt
rm -rf comments.txt;
rm -rf .env;
echo "media_id=$1" >> .env
scrapy crawl bilibilicomment;
python3 generateWordCloud.py