import csv
import requests
from bs4 import BeautifulSoup

PATH = "ads.csv"

ads = []

URL = "https://www.olx.ua/d/dopomoga/?currency=UAH&search%5Bprivate_business%5D=business&page=2"
# u = input("Enter your url: ")

HEADERS = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "accept":"*/*"
}


def save_file(path, items):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Товар(услуга)", "Цена", "Местоположение"
        ])
        for ad in items: 
            print(f'AD: {ad}')
            try:
                writer.writerow([
                ad["title"], ad["price"], ad["location"]
            ])
            except TypeError:
                print(f'The last ad: {ad}')


def get_html(html):
    return requests.get(html,headers = HEADERS)


def get_last_page(html):
    r = get_html(html)
    soup = BeautifulSoup(r.content, "html.parser")
    last_page = soup.findAll("a", {"class":"css-1mi714g"})[-1].text

    return int(last_page)


def get_ads(html):
    r = get_html(html)
    soup = BeautifulSoup(r.content, "html.parser")
    cards = soup.findAll("div", {"class": "css-wmzjt6"})
    print(f"Ads on page: {len(cards)}")

    for card in cards:
        data = {}

        title = card.find("h6").text
        try:
            price = card.find("p",{"class":"css-l0108r-Text eu5v0x0"}).text
        except TypeError:
            price = "Check the price"
        except AttributeError:
            price = ""
            print(f'card {card} has no text')
            
        location = card.find("p", {"class":"css-p6wsjo-Text eu5v0x0"}).text

        data["title"] = title
        data["price"] = price
        data["location"] = location

        print(data)

        ads.append(data)


    #     ads.append(title)
    #     print(title)
    # return ads


def main():
    base_url = URL[:-1]
    lp = get_last_page(URL)
    for i in range(1, lp + 1):
        current_url = base_url + str(i)
        print(f"PAGE NUMBER--- {current_url}")
        ads.append(get_ads(current_url))
    
main()
save_file(PATH, ads)

print(f"Total ads: {len(ads)}")
