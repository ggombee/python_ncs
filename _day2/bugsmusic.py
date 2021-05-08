from bs4 import BeautifulSoup
from urllib.request import urlopen

class Bugsmusic:

   url = ''


   def crawl(self):
       url = urlopen(self.url)
       soup = BeautifulSoup(url, 'lxml')
       cnt_artist = 0
       ctn_title = 0

       for link1 in soup.find_all(name="p", attrs=({"class": "artist"})): #p태그의 class가 artist인 것을 찾음
           cnt_artist += 1
           print(str(cnt_artist) + "위")
           print("아티스트 : " + link1.find('a').text)
       print('---------------------------------------')

       for link2 in soup.find_all(name="p", attrs=({"class": "title"})):
           ctn_title += 1
           print(str(ctn_title) + "위")
           print("노래제목" + link2.text)

   @staticmethod
   def main():
       bugs = Bugsmusic()
       bugs.url = 'https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210508&charthour=13'
       bugs.crawl()

if __name__ == '__main__':
    Bugsmusic.main()