BOT_NAME = "placement"

SPIDER_MODULES = ["placement.spiders"]
NEWSPIDER_MODULE = "placement.spiders"
ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 16
DUPEFILTER_DEBUG = True

EXTENSIONS = {"spidermon.contrib.scrapy.extensions.Spidermon": 500}

SPIDERMON_ENABLED = True

ITEM_PIPELINES = {"spidermon.contrib.scrapy.pipelines.ItemValidationPipeline": 800}

SPIDERMON_VALIDATION_CERBERUS = ["/home/vipulgupta2048/placement/placement/schema.json"]

USER_AGENT = "Vipul Gupta - placement (vipulgupta2048@gmail.com)"
