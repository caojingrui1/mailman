# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 16:38
# @Author  : Tom_zc
# @FileName: refresh_to_mysql.py
# @Software: PyCharm

import os
import pymysql
import click
import traceback


class GlobalConfig:
    GITHUB_URL = "https://github.com/opensourceways/mailman/raw/main/templates/{}/{}"
    QUERY_SQL = """select count(*) as count from template where name='{}' and context='{}'"""
    UPDATE_SQL = "update template set uri='{}' where name='{}' and context='{}'"
    INSERT_SQL = """insert into template(name, context, uri, username) values('{}', '{}', '{}', NULL);"""


def get_template_name_list(domain_name):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    domain_dir_name = os.path.join(dir_name, domain_name)
    return os.listdir(domain_dir_name)


def refresh_to_mysql(template_name_list, domain, username, password, ip, port, database="mailman"):
    mysql_conn = pymysql.connect(user=username, password=password, host=ip, port=port, database=database)
    cursor = mysql_conn.cursor()
    try:
        for template_name in template_name_list:
            complete_git_url = GlobalConfig.GITHUB_URL.format(domain, template_name)
            base_name = os.path.splitext(template_name)[0]
            name = ":".join(base_name.split("_"))
            query_sql = GlobalConfig.QUERY_SQL.format(name, domain)
            cursor.execute(query_sql)
            data = cursor.fetchone()
            if data[0] != 0:
                update_complete_sql = GlobalConfig.UPDATE_SQL.format(complete_git_url, name, domain)
                cursor.execute(update_complete_sql)
            else:
                insert_complete_sql = GlobalConfig.INSERT_SQL.format(name, domain, complete_git_url)
                cursor.execute(insert_complete_sql)
        mysql_conn.commit()
    except Exception as e:
        print(e, traceback.format_exc())
    finally:
        mysql_conn.close()


@click.command()
@click.argument("domain")
@click.argument("username")
@click.argument("password")
@click.argument("ip")
@click.argument("port", default=3306)
def refresh_data(domain, username, password, ip, port):
    """获取所有的数据，先查询数据库是否存在，如果存在，则修改，否则新填"""
    template_name_list = get_template_name_list(domain)
    refresh_to_mysql(template_name_list, domain, username, password, ip, port)


if __name__ == '__main__':
    refresh_data()
