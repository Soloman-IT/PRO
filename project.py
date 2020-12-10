import requests
import re
import time
import random
from bs4 import BeautifulSoup
da = []
class Random_film:
    fi = 1 
    html_tags = ["<div class=\"filmInfo_descEditor visualEditorInsertion\">","/div","<p>","</p>"]
    def __init__(self, url):
        self.url = url
        self.req = requests.get(self.url)
        self.names_films = []
        self.ratings_films = []
        self.ganres_films = []
        self.infos_films = []
        self.urls_films = []
        self.all = []
    def collect_data(self):
        num = random.randrange(0,10)
        print(num)
        for i in range(num,num+1):
            self.url = self.url[0:-1]+ str(i)
            self.req = requests.get(self.url)
            print(self.url)
            name_films = re.findall(r"<a class=\"films_name ref\" href=\"\/movies\/[\d]+\/\">([\'a-zA-Zа-яёА-ЯЁ «»\"+\d№=.\(\)\-+,?!:]+)<\/a>",self.req.text)
            rating_films = re.findall(r"<span data-js=\"numRating\" class=\"rating_num\">([\d.]+)<\/span>",self.req.text)
            ganre_films = re.findall(r"<span class=\"films_info\">([а-яёА-ЯЁ ,]+)<\/span>",self.req.text)
            url_films = re.findall(r"<a class=\"films_name ref\" href=\"(\/movies\/[\d]+\/)\">[\'a-zA-Zа-яёА-ЯЁ «»\"+\d№=.\(\)\-+,?!:]+<\/a>",self.req.text)
            if i == 4:
                rating_films.pop(23)
                ganre_films.pop(23)

            if len(ganre_films) == 99 and i == 9:
                ganre_films.insert(69,"нет")
            self.names_films.extend(name_films)
            self.ratings_films.extend(rating_films)
            self.ganres_films.extend(ganre_films)
            self.urls_films.extend(url_films)
            name_films = None
            rating_films = None
            ganre_films = None
            url_films = None
        for i in range(len(self.urls_films)):
            html_tags = ["<div class=\"filmInfo_descEditor visualEditorInsertion\">","/div","<p>","</p>","<>","\n","\t","\xa0","<br/>","<em>","</em>"]
            self.urls_films[i] = "https://www.kinoafisha.info" + self.urls_films[i]
            soup = BeautifulSoup(requests.get(self.urls_films[i]).text)
            info_films = None
            info_films = soup.find_all("div",{"class":"filmInfo_descEditor visualEditorInsertion"})
        
            for j in range(11):
                try :
                   if str(info_films[0]).find(html_tags[j]) != -1:
                        info_films[0] = str(info_films[0]).replace(html_tags[j],"")
                except BaseException:
                    info_films.append("Пока не вышло")
                    break
            self.infos_films.append(str(info_films[0]))
        self.infos_films[84] = "Содержание: Волшебное кольцо, Грибок-Теремок, Две сказки, Сказка со сказкой, Мальик спальчик"
        try:
            for i in range(100):
                
                self.all.append({self.names_films[i],self.ratings_films[i],self.ganres_films[i],self.infos_films[i]})
        except BaseException:
            pass
        global da
        da = list(random.choice(self.all))
def start():
    print("Подготавливаем софт для взлома пентагона...")
    kinopoisk = Random_film("https://www.kinoafisha.info/rating/movies/?page=0")
    kinopoisk.collect_data()
if "__name__" =="__main__":
    print("та да")







