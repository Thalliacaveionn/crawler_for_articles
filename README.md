# Crawler for read articles
This solution crawls articles from the www.bbc.com site, cleans the returned response, stores this response in BigQuery (Google Cloud), and makes it available for search through a python API.

## Requirementes: 
python 3.12

## Pip install requirements: 
scrapy, readability-lxml, google-cloud-bigquery

## Create the Scrapy Project:
Using the commands

`scrapy startproject article_creawler`
`cd article_creawler`

## Create a new spider:
`scrapy genspider guardian_spider bbc_article_spider`
