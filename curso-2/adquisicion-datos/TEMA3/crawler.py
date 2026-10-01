import scrapy
from scrapy.crawler import CrawlerProcess


class BookScraper(scrapy.Spider):
    """
    Class that implements scrapy's spyder interface to crawl books from the web
    """

    name = "books"
    start_urls = ["https://books.toscrape.com/"]
    categories_map = {}
    category_names = []

    def parse(self, response):
        """
        Method that parses the response from the page and extracts the available categories
        """
        categories = response.css("ul.nav")[0].css("a")
        for category in categories:
            name = category.css("::text").get().replace("\n", "").strip().lower()
            self.category_names.append(name)
            href = category.css("::attr(href)").get()
            self.categories_map[name] = href
        for category_to_scrap in getattr(self, "categories", []):
            if not category_to_scrap.lower() in self.category_names:
                print(
                    f"Category {category_to_scrap} does not exist and won't be extracted"
                )
            else:
                yield response.follow(
                    self.categories_map[category_to_scrap],
                    self.parse_category,
                    meta={"category": category_to_scrap},
                )

    def parse_category(self, response):
        # Get current category from meta field in response
        current_category = response.meta.get("category")
        # Get all book URLs in current page
        books = response.css(
            "article.product_pod div.image_container a::attr(href)"
        ).getall()
        for book in books:
            yield response.follow(
                book, self.parse_book, meta={"category": current_category}
            )
        # If current page has a next button, navigate to next page and scrap books from there
        next_page_url = response.css("ul.pager li.next a::attr(href)").get()
        if next_page_url is not None:
            yield response.follow(
                next_page_url, self.parse_category, meta={"category": current_category}
            )

    def parse_book(self, response):
        title = response.css("h1::text").get()
        upc = response.css("table.table tr")[0].css("td::text").get()
        current_category = response.meta.get("category")
        yield {"title": title, "upc": upc, "category": current_category}


if __name__ == "__main__":
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "books.json": {"format": "json", "overwrite": True},
            },
        }
    )
    process.crawl(BookScraper, categories=["mystery", "fiction"])
    process.start()
