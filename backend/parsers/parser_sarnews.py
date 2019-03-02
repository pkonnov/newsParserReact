#!/usr/bin/python3.6

from parser_requirements import *


def sarnews_parser():
    '''get parse title url'''
    url = 'https://www.saratovnews.ru'
    sarnews = Request('https://www.saratovnews.ru/', headers=headers)
    sarnews_read = urlopen(sarnews).read()
    sarnews_soup = BeautifulSoup(sarnews_read, 'lxml')
    title_sarnews = sarnews_soup.find('ul', {'class': 'pins'}).find_all('a', {'class': 'nodecor'})[:1]
    url_sarnews = sarnews_soup.find('ul', {'class': 'pins'}).find_all('a', {'class': 'nodecor'})[:1]
    srn_title = [title.getText() for title in title_sarnews]
    srn_url = [url.get('href') for url in url_sarnews]

    '''id gen'''
    # hash_md = hashlib.md5(f'{title_nvrs}'.encode('utf-8')).hexdigest()
    idgen = random.randint(1, 11111111111111111111)

    d = datetime.strftime(datetime.now(), "%d %b %Y %H:%M:%S")
    date_now = parser.parse(d).isoformat()

    c = conn.cursor()

    # get news on the title
    oldtitle = c.execute(f"SELECT * FROM simple_app_newsurls WHERE title LIKE '{srn_title[0]}'")

    if oldtitle.fetchone() == None:
        c.execute(
            f"INSERT INTO simple_app_newsurls VALUES ('{idgen}', '{srn_title[0]}', '{srn_url[0]}','{date_now}', '{url}')")
    else:
        print('none')

    print(oldtitle.fetchone())
    conn.commit()
    conn.close()


if __name__ == '__main__':
    sarnews_parser()
