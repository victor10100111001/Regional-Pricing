import requests
from bs4 import BeautifulSoup
import re

content = requests.get("https://dataimpulse.com/proxies-by-location/residential-proxies-by-location/").content

soup = BeautifulSoup(content, "html.parser")

countries = soup.select(".proxy-list-country")

links = [country["href"] for country in countries]
id = [link.split("/")[-2] if len(link.split("/")[-2]) == 2 else link.split("/")[-2].split("-")[-1] for link in links]

countries = [country.select_one("span").text for country in countries]

for (country, link) in zip(countries, links):
    country_to_id = {country: id for (country, id) in zip(countries, id)}

for country, id in country_to_id.items():
    proxies =  {
        "https": f"http://3d829a34d1ce6cf7d275__cr.{id}:adca78d414ce9054@gw.dataimpulse.com:823"
    }

    print(f"Testing {country} with ID {id}")
    response = requests.get("https://api.ipify.org", proxies=proxies, ).text
    print(f"{country}: {response}")