# !/usr/bin/python
# -*- coding: utf-8 -*

from discord_webhook import DiscordWebhook
import argparse
import logging
import sys
import requests


def start_bot(webhook):
    public_ip = get_public_ip()
    _webhook = DiscordWebhook(url=webhook, content=f'My server ip is {public_ip}')
    response = _webhook.execute()
    logging.info(f'response : {response}')


def get_public_ip():
    try:
        res = requests.get('https://api.ipify.org')
        return res.content.decode('utf-8')
    except:
        return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    argp = argparse.ArgumentParser()
    argp.add_argument("-w", "--webhook", required=True, help='Discord webhook url', type=str, default="")
    param = argp.parse_args()
    start_bot(webhook=param.webhook)
