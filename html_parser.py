from bs4 import BeautifulSoup
from typing import List
from urllib.parse import urljoin


def create_soup(html:str)->BeautifulSoup:
    soup = BeautifulSoup(html,"html.parser")
    return soup

META_PROPERTIES = {
    'title': ['og:title', 'twitter:title', 'title'],
    'description': ['og:description', 'twitter:description', 'description'],
    'image': ['og:image', 'twitter:image', 'image'],
    "twitter_handle": ["twitter:site","twitter:creator"]
}

def get_meta_content(soup:BeautifulSoup, property_list:List[str]):
    for prop in property_list:
        if content := soup.find('meta', property=prop) or soup.find('meta', attrs={"name": prop}):
            return content.get('content', '')
    return ''

def get_meta(soup:BeautifulSoup):
    meta_info = {}
    for key, properties in META_PROPERTIES.items():
        meta_info[key] = get_meta_content(soup, properties)
    return meta_info

def extract_largest_favicon(soup:BeautifulSoup,url:str):
    icon_links = soup.find_all('link', rel=lambda value: value and 'icon' in value.lower())

    largest_size = 0
    largest_icon_url = ''

    for link in icon_links:
        size = link.get('sizes')
        if size:
            try:
                width, height = map(int, size.lower().split('x'))
                if width * height > largest_size:
                    largest_size = width * height
                    largest_icon_url = link.get('href')
            except ValueError:
                pass
        elif not largest_icon_url:  
            largest_icon_url = link.get('href')

    if largest_icon_url:
        largest_icon_url = urljoin(url, largest_icon_url)

    return largest_icon_url