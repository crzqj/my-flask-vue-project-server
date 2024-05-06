import requests
from bs4 import BeautifulSoup


def crawl_baidu_pan(url):
    """
    Crawls a Baidu Pan share link to extract and print all links that contain 'pan.baidu.com'.
    
    :param url: The URL of the Baidu Pan share link to crawl.
    :type url: str
    
    :return: None
    :rtype: None
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            if 'pan.baidu.com' in link['href']:
                print(link['href'])
    else:
        print('Request failed!')


if __name__ == '__main__':
    baidu_pan_url = input('Enter the Baidu Pan share link: ')
    crawl_baidu_pan(baidu_pan_url)