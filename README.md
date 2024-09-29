# crawler_for_articles
Esta solução que rastreia artigos de sites de notícias, limpa a resposta retornada, armazena esta resposta no BigQuery (Google Cloud) e disponibiliza para pesquisa por meio de uma API python.

Requirementes: python 3.12, scrapy, readability-lxml, Google Cloud SDK

# Create the Scrapy Project:
Using the command

`scrapy startproject news_crawler
cd news_crawler`
