# -*- coding: utf-8 -*-
# @Time    : 2023/2/28 18:55
# @Author  : Tom_zc
# @FileName: cancel_subscribe_pending.py
# @Software: PyCharm
import os
import time
from mailmanclient import Client


class TokenOwner:
    """Who 'owns' the token returned from the registrar?"""
    subscriber = 'subscriber'
    moderator = 'moderator'


def cancel_subscribe_pending(mailman_url, mailman_username, mailman_password):
    """cancel subscribe pending"""
    client = Client(mailman_url, mailman_username, mailman_password)
    all_mailman_list = client.get_lists()
    for mailman_list in all_mailman_list:
        req_list = [req for req in
                    mailman_list.get_requests(token_owner=TokenOwner.subscriber, request_type="subscription")]
        for req in req_list:
            time_array = time.strptime(req["request_date"], "%Y-%m-%dT%H:%M:%S")
            timestamp = time.mktime(time_array)
            if int(time.time()) - timestamp > 5 * 60:
                mailman_list.moderate_request(req["token"], "discard", None)
                print("Discard the list：{}; email:{}".format(req["list_id"], req["email"]))
            else:
                print("Not discard the list：{}; email:{}, because the request is not expired(create<5min)".format(req["list_id"],
                                                                                                                  req["email"]))


if __name__ == '__main__':
    url = os.getenv("mailman_url")
    username = os.getenv("mailman_username")
    password = os.getenv("mailman_password")
    if not all([url, username, password]):
        raise RuntimeError("Please check the env of mailman_url.mailman_username.mailman_password ")
    cancel_subscribe_pending(url, username, password)
