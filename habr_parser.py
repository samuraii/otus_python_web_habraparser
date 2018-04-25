import requests
import bs4

def _fetch_habr_feed_page(page_num):
    if page_num > 100:
        return None
    url = 'https://habr.com/all/'
    url += 'page{}/'.format(page_num)
    return requests.get(url).text


def fetch_raw_html_from_pages(pages=4):
    raw_pages = []
    for page_num in range(1, pages + 1):
        raw_pages.append(_fetch_habr_feed_page(page_num=page_num))
    return raw_pages


def create_bs4_objects_from_raw_html(raw_pages):
    bs4_objects = []
    for raw_page in raw_pages:
        bs4_objects.append(bs4.BeautifulSoup(raw_page, "html.parser"))
    return bs4_objects
