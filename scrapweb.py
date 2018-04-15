import re
import bs4
import requests
import wget
import random
import string


def main():
    def_url = 'http://www.m-afshar.net/ganjineye%20adabi.htm'
    downlodfile_counter = 0
    lst_url, farsinames = get_file_link(def_url)
    for li, lb in zip(lst_url, farsinames):
        try:
            downlodfile(li, lb)
            downlodfile_counter += 1
        except Exception as e:
            print('error to download file {0} because {1}'.format(lb,e))

    print('***    download {} files complete  !!!!   ***'.format(downlodfile_counter))


def generate_word(length):
    VOWELS = "aeiou"
    CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    return word


def get_file_link(url):
    lst_file_url = []
    lst_name = []
    my_url = url
    res = requests.get(my_url)
    res_bs4 = bs4.BeautifulSoup(res.content, 'html.parser')
    links = res_bs4.find_all('a')
    for li in links:
        finl_res = str(li.get('href'))
        if finl_res.endswith(('.doc', '.docx', '.pdf')):
            t = str(li.text).replace('|','w')
            farsi_name = " ".join(re.split("\s+", t, flags=re.UNICODE))
            lst_name.append(farsi_name)
            lst_file_url.append(finl_res)

    return lst_file_url, lst_name


def downlodfile(url, farsiname):

    fixing_url = 'http://www.m-afshar.net/'
    out_folder_1 = 'e:/book2/'
    out_folder_2 = 'e:/book2/error/'
    try:
        my_url = str(url)
        if my_url.endswith('.doc'):
            fixname = out_folder_1 + farsiname + ".doc"
        elif my_url.endswith('.docx'):
            fixname = out_folder_1 + farsiname + ".docx"
        else:
            fixname = out_folder_1 + farsiname + ".pdf"
        if 'http://' not in my_url:
            my_url = fixing_url + my_url
        print("*** download start : {}   *** ".format(my_url))
        wget.download(my_url, fixname)
    except Exception as e:
        wget.download(my_url,out_folder_2+generate_word(5)+'.doc')
        print('downlod error {} file!!! because {}'.format(my_url,e))


if __name__ == '__main__':
    main()
