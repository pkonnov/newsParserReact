#!/usr/bin/python3.6

from parser_requirements import *


def echo_parser():
    '''get parse title url'''
    url = 'http://echosar.ru'
    ech = Request('http://echosar.ru/news/', headers=headers)
    ech_read = urlopen(ech).read()
    ech_soup = BeautifulSoup(ech_read, 'lxml')
    title_ech = ech_soup.find('div', {'class':'nc_list'}).find_all('h2')[:1]
    url_ech = ech_soup.find('div', {'class':'nc_list'}).find_all('a', {'class':'more'})[:1]
    e_title = [title.getText() for title in title_ech]
    e_url = [url.get('href') for url in url_ech]

    '''id gen'''
    # hash_md = hashlib.md5(f'{title_nvrs}'.encode('utf-8')).hexdigest()
    idgen = random.randint(1, 11111111111111111111)

    d = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    date_now = parser.parse(d).isoformat()

    c = conn.cursor()

    # get news on the title
    oldtitle = c.execute(f"SELECT * FROM simple_app_newsurls WHERE title LIKE '{e_title[0]}'")

    if oldtitle.fetchone() == None:
        c.execute(
            f"INSERT INTO simple_app_newsurls VALUES ('{idgen}', '{e_title[0]}', '{e_url[0]}','{date_now}', '{url}')")
    else:
        print('none')

    print(oldtitle.fetchone())
    conn.commit()
    conn.close()


if __name__ == '__main__':
    echo_parser()
