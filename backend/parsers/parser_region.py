#!/usr/bin/python3.6

from parser_requirements import *


def region_parser():
    '''get parse title url'''
    url = 'http://sarnovosti.ru'
    reg = Request('http://sarnovosti.ru/mindex.php', headers=headers)
    reg_read = urlopen(reg).read()
    reg_soup = BeautifulSoup(reg_read, 'lxml')
    title_reg = reg_soup.find('div', {'id': 'headerwrap'}).find_all('a')[1:2]
    url_reg = reg_soup.find('div', {'id': 'headerwrap'}).find_all('a')[1:2]
    rg_title = [title.getText()[3:] for title in title_reg]
    rg_url = [url.get('href') for url in url_reg]

    '''id gen'''
    # hash_md = hashlib.md5(f'{title_nvrs}'.encode('utf-8')).hexdigest()
    idgen = random.randint(1, 11111111111111111111)

    d = datetime.strftime(datetime.now(), "%b %Y %H:%M:%S")
    date_now = parser.parse(d).isoformat()

    c = conn.cursor()

    # get news on the title
    oldtitle = c.execute(f"SELECT * FROM simple_app_newsurls WHERE title LIKE '{rg_title[0]}'")

    if oldtitle.fetchone() == None:
        c.execute(
            f"INSERT INTO simple_app_newsurls VALUES ('{idgen}', '{rg_title[0]}', '{rg_url[0]}','{date_now}', '{url}')")
    else:
        print('none')

    print(oldtitle.fetchone())
    conn.commit()
    conn.close()


if __name__ == '__main__':
    region_parser()
