import os
import re
import bs4
import requests
import wget


def main():
    def_url = 'http://www.talif.sch.ir/thinking.htm#powerpoint'
    extention = '.rar'
    res_lst, farsinames = get_file_link(def_url, extention)
    for li, lb in zip(res_lst, farsinames):
        try:
            downlodfile(li, lb)
        except Exception as e:
            print('error to download file {0} : {1}'.format(lb, e))
    print('***    download complete !!!!   ***')


def check_out_folder_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)


def get_file_link(url, extention):
    lst_file = []
    lst_name = []
    my_url = url
    res = requests.get(my_url)
    res_bs4 = bs4.BeautifulSoup(res.content, 'html.parser')
    links = res_bs4.find_all('a', href=True)
    for li in links:
        finl_res = str(li.get('href'))
        if finl_res.endswith(extention):
            t = str(li.text)
            sentence = " ".join(re.split("\s+", t, flags=re.UNICODE))
            lst_name.append(sentence)
            lst_file.append(finl_res)
    return lst_file, lst_name


def downlodfile(url, farsiname):
    try:
        out_folder_1 = 'e:/tafkor/'
        check_out_folder_exists(out_folder_1)
        my_url = str(url)
        name = os.path.basename(my_url)
        fixname = out_folder_1 + name.replace(name, farsiname + ".rar")
        print(fixname)
        print("*** download start : {}   *** ".format(my_url))
        if not os.path.exists(fixname):
            wget.download(my_url, fixname)
    except Exception as e:
        print('downlod error {} file!!! because {}'.format(my_url, e))


if __name__ == '__main__':
    main()
