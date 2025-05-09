BOT_NAME = "rubinot_scraper"

SPIDER_MODULES = ["rubinot_scraper.spiders"]
NEWSPIDER_MODULE = "rubinot_scraper.spiders"

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

DOWNLOADER_MIDDLEWARES = {
    "scrapy_playwright.middleware.ScrapyPlaywrightMiddleware": 543,
}

ROBOTSTXT_OBEY = False
PLAYWRIGHT_BROWSER_TYPE = "chromium"