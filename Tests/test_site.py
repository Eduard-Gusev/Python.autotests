from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from Pages.homepage import HomePage
from Pages.product import Product_page


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = Product_page(browser)
    product_page.check_title_is('Samsung galaxy s6')


def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(3)
    homepage.check_products_count(2)