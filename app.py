from crawler import get_direct_html
from html_parser import create_soup,get_meta,extract_largest_favicon
from db import tool


def extract_url_data(url:str):
    html = get_direct_html(url)
    soup =  create_soup(html)
    meta = get_meta(soup)
    favicon = extract_largest_favicon(soup,url)
    data = {**meta,"favicon":favicon,"url":url}
    return data

def save_to_db(url_data):
    url = url_data.get("url")
    data = extract_url_data(url)
    tool.insert_one(data)
    print("Inserted", url)
