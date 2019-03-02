#!/usr/bin/python3.6

from parser_requirements import *


def obmnenie_parser():
    '''get parse title url'''
    url = 'https://om-saratov.ru'
    ob_m = Request('https://om-saratov.ru/novosti', headers=headers)
    ob_m_read = urlopen(ob_m).read()
    ob_m_soup = BeautifulSoup(ob_m_read, 'lxml')
    title_ob_m = ob_m_soup.find('div', {'class':'lenta_box'}).find_all('b')[:1]
    url_ob_m = ob_m_soup.find('div', {'class':'lenta_box'}).find_all('a', {'class': 'name'})[:1]
    ob_title = [title.getText() for title in title_ob_m]
    ob_url = [url.get('href') for url in url_ob_m]

    '''id gen'''
    # hash_md = hashlib.md5(f'{title_nvrs}'.encode('utf-8')).hexdigest()
    idgen = random.randint(1, 11111111111111111111)

    d = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    date_now = parser.parse(d).isoformat()

    c = conn.cursor()

    # get news on the title
    oldtitle = c.execute(f"SELECT * FROM simple_app_newsurls WHERE title LIKE '{ob_title[0]}'")

    if oldtitle.fetchone() == None:
        c.execute(
            f"INSERT INTO simple_app_newsurls VALUES ('{idgen}', '{ob_title[0]}', '{ ob_url[0]}','{date_now}', '{url}')")
    else:
        print('none')

    print(oldtitle.fetchone())
    conn.commit()
    conn.close()


if __name__ == '__main__':
    obmnenie_parser()
