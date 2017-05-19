import click
import requests
from includes.Scanner import Scanner
from includes.Result import Result
import json

# !/usr/bin/python
# -*- coding: utf8 -*-
from includes.Scraper import Scraper

__author__ = '@capJavert'

website_scanners = [
    Scanner(
        'http://www.avgthreatlabs.com/ww-en/website-safety-reports/domain/',
        'website',
        '//div[contains(@class, "rating")]/text()'
    )
]

email_scanners = [
    Scanner(
        'https://api.hunter.io/v2/email-verifier?'
        'api_key=8a483e0389d17d1009b14b9311bc268da6b3e2a0&email=',
        'email',
        "api-hunter",
        True
    )
]


def decode_api_hunter(data):
    data = json.loads(data)

    return data["data"]["result"] + ", score: " + str(data["data"]["score"])


results = []
options = {
    "api-hunter": decode_api_hunter
}


def do_request(url, param):
    response = requests.get(url + param)
    response.encoding = 'ISO-8859-1'

    return response.content


@click.command()
@click.option('--email', '-e', default=None, help='Email address that you wish to check.')
@click.option('--website', '-w', default=None, help='Website that you wish to check.')
def main(email, website):
    if not email and not website:
        print("You are missing --email or --website params. Use --help for more info.")
        return

    if email:
        for target in email_scanners:
            if target.is_json:
                data = options[target.identifier](do_request(target.url, email))
            else:
                scraper = Scraper(Scraper.html_dom(do_request(target.url, email)))
                data = scraper.get_custom_filter(target.identifier)[0].strip()

            results.append(
                Result(target,
                       kind=target.kind,
                       data=data,
                       subject=email
                       )
            )

    if website:
        for target in website_scanners:
            if target.is_json:
                data = options[target.identifier](do_request(target.url, website))
            else:
                scraper = Scraper(Scraper.html_dom(do_request(target.url, website)))
                data = scraper.get_custom_filter(target.identifier)[0].strip()

            results.append(
                Result(target,
                       kind=target.kind,
                       data=data,
                       subject=website
                       )
            )

    for result in results:
        print(result.subject + " (" + result.kind + ") STATUS: " + result.data
              + " (" + result.target.url + "/" + result.subject + ")")

main()
