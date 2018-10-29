# -*- coding: utf-8 -*-
import scrapy
import time
from random import randint

pagn = 0

class Spider(scrapy.Spider):
    name = ''
    allowed_domains = ['']
    start_urls = ['']

    def __init__(self, filename=None):
    	if filename:
    		with open(filename, 'r') as f:
    			self.start_urls = f.readlines()

    def start_requests(self):
    	for curr_url in self.start_urls:
    		yield scrapy.Request(curr_url, callback=, dont_filter=True)

    def parse_urls(self, response):
    	car_urls_curr_page = response.xpath('').extract()
    	for url_curr_page in urls_curr_page:
    		time.sleep(randint(0,1))
    		yield scrapy.Request(response.urljoin(url_curr_page), callback=self.parse)

    	global pagn
    	pagn+= 100
    	next_page = '' % pagn
    	if next_page:
    		time.sleep(randint(1,4))
    		yield scrapy.Request(next_page, callback=self.parse_urls)

    def parse(self, response):
    	pass