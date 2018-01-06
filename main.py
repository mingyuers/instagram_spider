# coding:utf-8

from instagram_spider import Instagram_Spider
import MySQLdb


def get_start_urls():
    start_urls = []
    db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='inst', charset='utf8')
    cursor = db.cursor()
    sql = 'select * from star'
    cursor.execute(sql)
    db.commit()
    stars = cursor.fetchall()
    print stars
    for star in stars:
#         if star[0] > 41:
            start_urls.append({
                'url': star[4],
                'name': star[1]
            })
    db.close()
    return start_urls


def main():
    start_urls = get_start_urls()
#     start_urls = [{'url':'https://www.instagram.com/kikuchanj/','name':'jujingyi'}]
    for i in range(len(start_urls)):
        url = start_urls[i]['url']
        name = start_urls[i]['name']
        print url, name
        ins = Instagram_Spider(url, name)
        ins.main()


main()

