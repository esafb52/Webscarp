import os
import re
import bs4
import requests
import wget
import random


def main():
    def_url = 'http://www.m-afshar.net/ganjineye%20adabi.htm'
    res_lst, farsinames = get_file_link(def_url)
    lb: str
    for li, lb in zip(res_lst, farsinames):
        try:
            downlodfile(li, lb)
        except Exception as e:
            print('error to download file {0} because {1}'.format(lb,e))

    print('***    download complete !!!!   ***')


def get_file_link(url):
    lst_file = []
    lst_name = []
    my_url = url
    res = requests.get(my_url)
    res_bs4 = bs4.BeautifulSoup(res.content, 'html.parser')
    links = res_bs4.find_all('a', href=True)
    for li in links:
        finl_res = str(li.get('href'))
        if finl_res.endswith(('.doc', '.docx', '.pdf')):
            t = str(li.text)
            sentence = " ".join(re.split("\s+", t, flags=re.UNICODE))
            lst_name.append(sentence)
            lst_file.append(finl_res)

    return lst_file, lst_name


def downlodfile(url, farsiname):

    fixing = 'http://www.m-afshar.net/'
    out_folder_1 = 'e:/book/'
    out_folder_2 = 'e:/book/error/'
    try:
        my_url = str(url)
        name = os.path.basename(my_url)

        if name.endswith('.pdf'):
            fixname = out_folder_1 + name.replace(name, farsiname + ".pdf")
        elif name.endswith('.docx'):
            fixname = out_folder_1 + name.replace(name, farsiname + ".docx")
        else:
            fixname = out_folder_1 + name.replace(name, farsiname + ".doc")

        if my_url.startswith('future'):
            my_url = fixing + my_url
        print("*** download start : {}   *** ".format(my_url))
        wget.download(my_url, fixname)
    except Exception as e:
        tem=str(random.randint(0,10000))
        wget.download(my_url,out_folder_2+tem+'.doc')
        print('downlod error {} file!!! because {}'.format(my_url,e))


if __name__ == '__main__':
    main()
