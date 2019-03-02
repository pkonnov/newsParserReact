#!/usr/bin/python3.6

from parser_requirements import *

conn = sqlite3.connect('../db.sqlite3', check_same_thread=False)


def vzsar_parser():
    '''get parse title url'''
    url = 'http://www.vzsar.ru/'
    vzsar = Request('http://www.vzsar.ru/news', headers=headers)
    vzsar_read = urlopen(vzsar).read()
    vzsar_soup = BeautifulSoup(vzsar_read, 'lxml')
    title_vzsar = vzsar_soup.find_all('div', class_='titles')[:1]
    url_vzsar = vzsar_soup.find('div', class_='newslist').find_all('a')[:1]
    vz_title = [title.find('h2').getText() for title in title_vzsar]
    vz_url = [url.get('href') for url in url_vzsar]

    '''id gen'''
    # hash_md = hashlib.md5(f'{title_nvrs}'.encode('utf-8')).hexdigest()
    idgen = random.randint(1, 11111111111111111111)

    d = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    date_now = parser.parse(d).isoformat()

    c = conn.cursor()

    # get news on the title
    oldtitle = c.execute(f"SELECT * FROM simple_app_newsurls WHERE title LIKE '{vz_title[0]}'")

    if oldtitle.fetchone() == None:
        c.execute(
            f"INSERT INTO simple_app_newsurls VALUES ('{idgen}', '{vz_title[0]}', '{vz_url[0]}','{date_now}', '{url}')")
    else:
        print('none')

    print(oldtitle.fetchone())
    conn.commit()
    conn.close()


if __name__ == '__main__':
    vzsar_parser()
