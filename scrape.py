from bs4 import BeautifulSoup
import requests
from lxml import html
import json

def get_trailer_xpath(imdb_id):
    url = f"https://www.imdb.com/title/{imdb_id}/"
    page = requests.get(url)
    tree = html.fromstring(page.content)

    # Trailer linki için genel bir XPath
    trailer_xpath = '//a[contains(@href, "videoplayer") and contains(@aria-label, "Trailer")]'

    # XPath'i kullanarak trailer linkini bul
    trailer_link = tree.xpath(trailer_xpath)
    for link in trailer_link:
        print(link.get("href"))
    return trailer_link


def get_image_from_imdb(imdb_id):
    url = f"https://www.imdb.com/title/{imdb_id}/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page for {imdb_id}, Status Code: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.content, "html.parser")
    image_tag = soup.find("img", {"class": "ipc-image"})
    
    if image_tag is not None:
        return image_tag["src"]
    else:
        print(f"Image not found for {imdb_id}")
        return None




"""
def get_trailer_from_imdb(imdb_id):
    url = f"https://www.imdb.com/title/{imdb_id}/"
    response = requests.get(url)
    response.raise_for_status()  # Hata varsa raise et

    # HTML içeriğini parse et
    soup = BeautifulSoup(response.content, 'html.parser')

    # JSON-LD scriptini bul
    json_ld_script = soup.find('script', type='application/ld+json')
    if not json_ld_script:
        return None

    # JSON-LD scriptini parse et
    try:
        json_data = json.loads(json_ld_script.string)
        # embedUrl'yi al
        embed_url = json_data.get("url", "")
        return embed_url
    except json.JSONDecodeError:
        return None


"""


if __name__ == "__main__":
    pass
