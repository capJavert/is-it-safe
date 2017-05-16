import click
import requests
from includes.Scanner import Scanner
from includes.Result import Result

# !/usr/bin/python
# -*- coding: utf8 -*-
from includes.Scraper import Scraper

__author__ = '@capJavert'

website_scanners = [
    Scanner(
        'http://www.avgthreatlabs.com/ww-en/website-safety-reports/domain',
        'website',
        '//div[contains(@class, "rating")]/text()'
    )
]

email_scanners = [
    Scanner(
        'https://hunter.io/trial/v2/email-verifier?email=ivamajnar@foi.hr&format=json',
        'email',
        {"json": "data.result"}
    )
]

results = []


def do_request(url, param):
    print(url + "/" + param)
    response = requests.get(url + "/" + param)
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
        print("Email search not implemented yet.")

        return

        for target in email_scanners:
            scraper = Scraper(Scraper.html_dom(do_request(target.url, email)))

            results.append(
                Result(target,
                       kind=target.kind,
                       data=scraper.get_custom_filter(target.identifier)[0].strip(),
                       subject=email
                       )
            )

    if website:
        for target in website_scanners:
            scraper = Scraper(Scraper.html_dom(do_request(target.url, website)))

            results.append(
                Result(target,
                       kind=target.kind,
                       data=scraper.get_custom_filter(target.identifier)[0].strip(),
                       subject=website
                       )
            )

    for result in results:
        print(result.subject + " (" + result.kind + ") STATUS: " + result.data
              + " (" + result.target.url + "/" + result.subject + ")\n")

main()
