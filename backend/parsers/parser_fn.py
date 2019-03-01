#!/usr/bin/python3.6

from parser_requirements import *


def fn_parser():
    '''get parse title url'''
    url = 'https://fn-volga.ru'
    fn = Request('https://fn-volga.ru/news/archive', headers=headers)
    fn_read = urlopen(fn).read()
    fn_soup = BeautifulSoup(fn_read, 'lxml')
    title_fn = fn_soup.find_all('div', class_='inf')[1:2]
    url_fn = fn_soup.find_all('a', class_='title')[1:2]
    free_title = [title.find('a').getText()[1:] for title in title_fn]
    free_url = [url.get('href') for url in url_fn]

    '''id gen'''
    # hash_md = hashlib.md5(f'{title_nvrs}'.encode('utf-8')).hexdigest()
    idgen = random.randint(1, 11111111111111111111)

    d = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    date_now = parser.parse(d).isoformat()

    c = conn.cursor()

    # get news on the title
    oldtitle = c.execute(f"SELECT * FROM simple_app_newsurls WHERE title LIKE '{title_fn[0]}'")

    if oldtitle.fetchone() == None:
        c.execute(
            f"INSERT INTO simple_app_newsurls VALUES ('{idgen}', '{free_title[0]}', '{free_url[0]}','{date_now}', '{url}')")
    else:
        print('none')

    print(oldtitle.fetchone())
    conn.commit()
    conn.close()


if __name__ == '__main__':
    fn_parser()
