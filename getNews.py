import requests
import bs4


# appratech        
url="http://appratech.net/"      
r=requests.get(url)
soup=bs4.BeautifulSoup(r.content, 'html.parser')
print("----------------------*** "+soup.title.string+" ***----------------------")
link=soup.find_all("h2")
for li in link :
    if len(li.text)>50:
        print(li.text + '\n'  )

#zoomit
url="https://www.zoomit.ir/"   
r=requests.get(url)
soup=bs4.BeautifulSoup(r.content, 'html.parser')
print("----------------------*** "+soup.title.string+" ***----------------------")
link=soup.find_all("h3")
counter_to_skip_item=0
for li in link :
        counter_to_skip_item+=1
        if counter_to_skip_item<7 or counter_to_skip_item> 27:
                continue
        print(li.text + '\n'  )

       
#digiato
url="http://digiato.com/"   
r=requests.get(url)
soup=bs4.BeautifulSoup(r.content, 'html.parser')
print("----------------------*** "+soup.title.string+" ***----------------------")
for li in link :
    if len(li.text)>20:
        print(li.text + '\n'  )

     



