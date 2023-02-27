# Scrapy settings for waterpipeline project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# ''' Config File Method '''
# import sys
# sys.path.append('../../')
# from .config.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

''' DOTENV Method '''
# import os
# from os.path import join, dirname
# from dotenv import load_dotenv

BOT_NAME = "waterpipeline"

SPIDER_MODULES = ["waterpipeline.spiders"]
NEWSPIDER_MODULE = "waterpipeline.spiders"

# FEED_URI = 's3://water-pipeline/%(name)s/%(name)s_%(date)s.csv'
# FEED_FORMAT = 'csv'

# FEED_STORAGES_BASE = {
#     '':'scrapy.extensions.feedexport.FilesFeedStorage',
#     's3':'scrapy.extensions.feedexport.s3FeedStorage',
# }

# FEED_STORAGES = {
#     '':'scrapy.extensions.feedexport.FilesFeedStorage',
#     's3':'waterpipeline.extensions.s3.s3FeedStorage',
# }

# FEED_EXPORTERS_BASE = {
#      'csv': 'scrapy.exporters.CsvItemExporter'
#      }

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)
# load_dotenv()

# AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

# S3_BUCKET_NAME = 'water-pipeline'
# AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY
# S3_PREFIX = 'water-pipeline/'



# ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
# ITEM_PIPELINES = {'scrapy.pipelines.files.FilesPipeline': 1}
# IMAGES_STORE = {
#     "s3://water-pipeline/middle-river/": {
#         "format": "tsv",
#     }}
# IMAGES_STORE_S3_ACL = 'private'

# ITEM_PIPELINE = {
# 'scrapy.pipelines.files.S3FilesStore': 1
# }

# FEED_EXPORT_BATCH_ITEM_COUNT = 3

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "waterpipeline (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "waterpipeline.middlewares.WaterpipelineSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "waterpipeline.middlewares.WaterpipelineDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "waterpipeline.pipelines.WaterpipelinePipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
