#!/usr/bin/python3.6

from parser_requirements import *


def sarbc_parser():
    '''get parse title url'''
    url = 'https://news.sarbs.ru'
    sarbc = urllib.request.urlopen('https://news.sarbc.ru/')
    sarbc_read = lxml.html.fromstring(sarbc.read())
    title_sarbc = sarbc_read.xpath('//div[@class="item-title"]/a/text()')[:1]
    url_sarbc = sarbc_read.xpath('//div[@class="item-title"]/a/@href')[:1]

    '''id gen'''
    # hash_md = hashlib.md5(f'{title_nvrs}'.encode('utf-8')).hexdigest()
    idgen = random.randint(1, 11111111111111111111)

    d = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    date_now = parser.parse(d).isoformat()

    c = conn.cursor()

    # get news on the title
    oldtitle = c.execute(f"SELECT * FROM simple_app_newsurls WHERE title LIKE '{title_sarbc[0]}'")

    if oldtitle.fetchone() == None:
        c.execute(
            f"INSERT INTO simple_app_newsurls VALUES ('{idgen}', '{title_sarbc[0]}', '{url_sarbc[0]}','{date_now}', '{url}')")
    else:
        print('none')

    print(oldtitle.fetchone())
    conn.commit()
    conn.close()


if __name__ == '__main__':
    sarbc_parser()
