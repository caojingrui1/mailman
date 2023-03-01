# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 10:56
# @Author  : Tom_zc
# @FileName: enable_user.py
# @Software: PyCharm


from mailmanclient import Client


def enable_user():
    client = Client("http://0.0.0.0:8001/3.1/", "", "")
    all_mailman_list = client.get_lists()
    for mailman_list in all_mailman_list:
        for mailman_list_member in mailman_list.members:
            if mailman_list_member.role == "member" and mailman_list_member.delivery_mode == "regular" and \
                    mailman_list_member.preferences['delivery_status'] != "enabled":
                print("find list:{},member:{},data:{}".format(mailman_list.list_name, mailman_list_member.address,
                                                              mailman_list_member.preferences))
                prefs = mailman_list_member.preferences
                prefs["delivery_status"] = 'enabled'
                prefs.save()
                print("Update list:{},member:{},data:{}".format(mailman_list.list_name, mailman_list_member.address,
                                                                mailman_list_member.preferences))


if __name__ == '__main__':
    enable_user()
