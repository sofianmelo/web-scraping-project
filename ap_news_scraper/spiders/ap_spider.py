import scrapy

class APSpider(scrapy.Spider):
    name = "ap_spider"  # Certifique-se de que este é o nome do spider
    start_urls = [
        'https://apnews.com',  # URL inicial
    ]

    def parse(self, response):
        # Extraia títulos e links de artigos da página principal
        for article in response.css('article'):
            yield {
                'title': article.css('h2 a::text').get(),  # Seleciona o título
                'link': article.css('h2 a::attr(href)').get(),  # Seleciona o link
            }
        
        # Navegar para a próxima página se houver
        next_page = response.css('a[aria-label="Next"]::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
