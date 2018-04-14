import os
import re
import bs4
import requests
import wget


def main():
    # web address to download files
    def_url = 'http://www.m-afshar.net/ganjineye%20adabi.htm'
    # get urls and farsi names  list form links
    res_lst, farsinames = get_file_link(def_url)
    lb: str
    for li, lb in zip(res_lst, farsinames):
        try:
            # download file one by one
            downlodfile(li, lb)
        except:
            print('error to downloa file {0}'.format(lb))
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
        # find custome extions ( '.doc', '.docx', '.pdf') in links
        if finl_res.endswith(('.doc', '.docx', '.pdf')):
            t = str(li.text)
            sentence = " ".join(re.split("\s+", t, flags=re.UNICODE))
            lst_name.append(sentence)
            lst_file.append(finl_res)
    return lst_file, lst_name


def downlodfile(url, farsiname):
    # for fix borken link
    fixlink = 'http://www.m-afshar.net/'
    # set place to store file in pc
    out_folder_1 = 'e:/t/books/'
    try:
        my_url = str(url)
        name = os.path.basename(my_url)
        # set  path and ext for evey file
        if name.endswith('.pdf'):
            fixname = out_folder_1 + name.replace(name, farsiname + ".pdf")
        elif name.endswith('.docx'):
            fixname = out_folder_1 + name.replace(name, farsiname + ".docx")
        else:
            fixname = out_folder_1 + name.replace(name, farsiname + ".doc")
        # fix broken links
        if my_url.startswith('future'):
            my_url = fixlink + my_url
        print("*** download start : {}   *** ".format(my_url))
        # download file
        wget.download(my_url, fixname)
    except:
        print('downlod error {} file!!!'.format(my_url))


if __name__ == '__main__':
    main()
