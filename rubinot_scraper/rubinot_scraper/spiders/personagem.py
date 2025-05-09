import scrapy
from scrapy_playwright.page import PageCoroutine


class PersonagemSpider(scrapy.Spider):
    name = "personagem"
    start_urls = [
        "https://rubinot.com.br/?subtopic=characters&name=Ulezovisk",
        "https://rubinot.com.br/?subtopic=characters&name=OutroChar"
    ]

    custom_settings = {
        "PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT": 60000,
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta={
                    "playwright": True,
                    "playwright_page_coroutines": [
                        PageCoroutine("wait_for_selector", "table.TableContent")
                    ],
                },
                callback=self.parse,
            )

    def parse(self, response):
        nome_td = response.css("table.TableContent td:contains('Name:') + td")

        nome = nome_td.css("font::text").get()
        cor_nome = nome_td.css("font::attr(color)").get()

        online = None
        if cor_nome:
            online = cor_nome.lower() == "green"

        yield {
            "nome": nome,
            "online": online
        }