import scrapy
import json
import pandas as pd

class ScraperSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["www.noon.com"]

    # Start with page 1
   
    def start_requests(self):
        base_url = (
            "https://www.noon.com/_next/data/"
            "bigalog-a18cbfcc8fcee7b143949c818af903078f57319d/uae-en/sports-and-outdoors/"
            "exercise-and-fitness/yoga-16328.json?isCarouselView=false&limit=50&"
            "page={page}&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc&"
            "catalog=sports-and-outdoors&catalog=exercise-and-fitness&catalog=yoga-16328"
        )

        for page in range(1, 101):  # Loop through pages 1 to 100
            url = base_url.format(page=page)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extract JSON data directly from the response
        data = response.json()

        # Safely access hits
        hits = data.get("pageProps", {}).get("catalog", {}).get("hits", [])
        

        # Extract relevant fields from each product
        for hit in hits:
            yield{
                "name": hit.get("name"),
                "id": hit.get("sku"),
                "brand": hit.get("brand"),
                "brand_id": hit.get("brand_code"),
                "price": hit.get("price"),
                "sale_price": hit.get("sale_price"),
                "image_key": hit.get("image_key"),
            }
        
