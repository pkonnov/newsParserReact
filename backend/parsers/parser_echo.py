#!/usr/bin/python3.6

from parser_requirements import *

conn = sqlite3.connect('../db.sqlite3', check_same_thread=False)


def nversia_parser():
    '''get parse title url'''
    url = 'https://nversia.ru'
    nvrs_url = 'https://nversia.ru/news/index/'
    nvrs = urllib.request.urlopen(nvrs_url)
    nvrs_read = lxml.html.fromstring(nvrs.read())
    title_nvrs = nvrs_read.xpath('//div[@class="material-body"]/a/text()')[:1]
    url_nvrs = nvrs_read.xpath('//div[@class="material-body"]/a/@href')[:1]

    '''id gen'''
    # hash_md = hashlib.md5(f'{title_nvrs}'.encode('utf-8')).hexdigest()
    idgen = random.randint(1, 11111111111111111111)

    d = datetime.strftime(datetime.now(), "%a, %d %b %Y %H:%M:%S")
    date_now = parser.parse(d).isoformat()

    c = conn.cursor()

    # get news on the title
    oldtitle = c.execute(f"SELECT * FROM simple_app_newsurls WHERE title LIKE '{title_nvrs[0]}'")

    if oldtitle.fetchone() == None:
        c.execute(
            f"INSERT INTO simple_app_newsurls VALUES ('{idgen}', '{title_nvrs[0]}', '{url_nvrs[0]}','{date_now}', '{url}')")
    else:
        print('none')

    print(oldtitle.fetchone())
    conn.commit()
    conn.close()


if __name__ == '__main__':
    nversia_parser()
