import re
from urllib.parse import urlparse,urljoin

def create_unique_foldername_from_url(url):
    parsed_url = urlparse(url)
    
    domain = parsed_url.netloc
    if domain.startswith('www.'):
        domain = domain[4:]
    
    domain = re.sub(r":\d+", "", domain)  # Remove port number
    
    if len(domain) > 255:  # Max folder name length for most file systems
        domain = domain[:255]
    
    return domain 


def convert_relative_to_absolute(base_url, relative_url):
    return urljoin(base_url, relative_url)

