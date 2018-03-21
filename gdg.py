import os
import signal
import sys
import warnings

import requests

from bs4 import BeautifulSoup
def gsoc_spider():

    url='https://summerofcode.withgoogle.com/archive/2017/organizations/'
    default = "https://summerofcode.withgoogle.com"

    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    orgs = soup.findAll('li', attrs={'class': 'organization-card__container'})

    for org in orgs:
        link = org.find('a', attrs={'class': 'organization-card__link'})
        org_name = org['aria-label']
        org_link = default + link['href']
        response = requests.get(org_link)
        html = response.content
        soup = BeautifulSoup(html, "html.parser")
        print(org_name)
        print(org_link)
        tags = soup.find('li', attrs={
            'class': 'organization__tag organization__tag--technology'

        }
        )
        print(tags.text)


gsoc_spider()