import scrapy
from readability import Document
from google.cloud import bigquery
import os

class BbcArticleSpider(scrapy.Spider):
    name = "bbc_article_spider"
    
    # Start URL for the specific article
    start_urls = [
        # 'https://www.bbc.com/news/articles/ckdg7jjlx2go',
        'https://www.bbc.com/news/articles/ce812qvld9do',
        'https://www.bbc.com/news/articles/cly5d9y07e3o'

    ]

    # Initialize BigQuery client
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\gales\OneDrive\Documentos\Thallia\crawler\crawler-article-437116-eba32b148e4e.json"
    client = bigquery.Client()
    dataset_id = 'articles'
    table_id = 'bbc'
    
    def parse(self, response):
        # Get article content using Readability
        doc = Document(response.text)
        article_text = doc.summary()
        article_title = doc.title()
        article_url = response.url
        
        # # Extract author if available
        author = response.css('meta[name="author"]::attr(content)').get() or response.css('a[data-component="author"]::text').get()
        
        # Prepare the data
        data = {
            'title': article_title,
            'author': author,
            'url': article_url,
            'content': article_text
        }

        # Log extracted data for debugging
        # self.logger.info(f"Extracted data: {data}")
        self.logger.info(f"Extracted data: {article_title}")

        # Yield the data to be saved
        yield data

        # Optionally save to BigQuery
        self.save_to_bigquery(data)

    def save_to_bigquery(self, data):
        table_ref = self.client.dataset(self.dataset_id).table(self.table_id)
        errors = self.client.insert_rows_json(table_ref, [data])
        if errors:
            self.logger.error(f"Failed to insert rows: {errors}")
        else:
            self.logger.info(f"Inserted row: {data['title']}")
