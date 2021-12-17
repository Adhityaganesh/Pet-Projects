from bs4 import BeautifulSoup
import requests
import pickle
import re
import csv

if __name__ == '__main__':

    def crawl_all():
#goes thro all the pages(A-Z)with their respective(#) and get their links and writes it into a pickle file

            all_pages=[]
            for i in range(ord('A'),ord('Z') +1):
                    url='https://itunes.apple.com/us/genre/ios-shopping/id6024?mt=8&letter=%s&page=1#page'%(chr(i))
                    req = requests.get(url)
                    y = BeautifulSoup(req.text, 'html.parser')
                    if y.find('ul',{'class':'list paginate'})!=None:
                        m=len(y.find('ul',{'class' : 'list paginate'}).findAll('li'))
                        for j in range(1,2):
                            all_pages.append("https://itunes.apple.com/us/genre/ios-shopping/id6024?mt=8&letter=%s&page=%d#page"%(chr(i),j))
                            
                    else:
                            all_pages.append('https://itunes.apple.com/us/genre/ios-shopping/id6024?mt=8&letter=%s'%(chr(i)))
                        


            pickle_out=open("all_pages","wb")
            pickle.dump(all_pages,pickle_out)
            pickle_out.close()
            #print(all_pages)
            print(len(all_pages))


    def get_app_link():
#reads the links from pickle file, goes thro all the pages and captures the all app links and writes it into a pickle file

            app_url = []
            pickle_in=open("all_pages","rb")
            all_pages=pickle.load(pickle_in)

            for g in all_pages:
                    req = requests.get(g)
                    y = BeautifulSoup(req.text, 'lxml')
                    x = y.find('div', class_ = 'grid3-column')
                    for a in x.findAll('li'):
                                    app_url.append(a.a['href'])

            pickle_out=open("app_url","wb")
            pickle.dump(app_url,pickle_out)
            pickle_out.close()
            #print(app_url)
            print(len(app_url))


    def get_app_data():
#reads the pickle file and gets all the app information and stores it in a dictionary		
            a={}
            pickle_in=open("app_url","rb")
            app_url=pickle.load(pickle_in)


            for d in app_url:
                req = requests.get(d)
                y = BeautifulSoup(req.text, 'lxml')
                app_name = y.find('h1',{'class' : 'product-header__title app-header__title'}).text
                a['app_name']=re.sub('[\s] +',' ',app_name).strip()
                b = y.find_all("div",{"class":"information-list__item l-row"})
                c = y.find("div",{"class" : 'l-column small-hide medium-show medium-9 medium-offset-3 large-10 large-offset-2'})
                d = y.find("div",{"class":"we-customer-ratings__averages"})
                try:
                	app_ratings=d.text
                	a['app_content_rating']=re.sub('[\s] +',' ',app_ratings).strip()
                except:
                	a['app_content_rating']='not sufficent ratings'
                for x in b:
                        try:
                                e=(x.find('dt',{'class' : 'information-list__item__term medium-valign-top l-column medium-3 large-2'}))
                                f=(x.find('dd',{'class' : 'information-list__item__definition l-column medium-9 large-6'}))
                                a[e.text]=re.sub('[\s] +',' ',f.text).strip()
                        except:
                                f='NIL'
                for link in c.findAll('a', href=True):
                                try:
                                        a[link.text]=re.sub('[\s] +',' ',link['href']).strip()
                                except:
                                        a['nil']='nil'

                supports = y.findAll('div',attrs={"class":"supports-list__item__copy"})
                supp_u=[]
                for x in supports:
                    ij=(x.find('h3').text)
                    supp_u.append(ij.strip())
                a['supports']=supp_u
                    

                description = y.find("div",{"class" : 'section__description'})
                des=description.find('p').get_text()
                a['desccrption']= re.sub('[\s] +',' ',des).strip()
                d={}
                c={}
                temp2=y.find_all("section",{"class":'l-content-width section section--bordered'})
                for h2tags in temp2:
                    temp=h2tags.find_all("h2",{"class":'section__headline'})
                    for x in temp:
                        names = x.get_text().strip()
                        if names == 'More By This Developer':
                            app_info=h2tags.find_all("div",{"class" : 'we-lockup__title '})
                            app_links=h2tags.find_all("a",{"class" : 'targeted-link'})
                            for z in app_links:
                                app_href=(z.attrs['href'])
                                app_names=z.find("div",{"class" : 'we-truncate we-truncate--single-line ember-view targeted-link__target'})
                                app_name=(app_names.get_text())
                                d[re.sub('[\s] +',' ',app_name).strip()]=re.sub('[\s] +',' ',app_href).strip()
                                a['apps_by_developer']=d
                        elif names == 'You May Also Like':
                            app_info=h2tags.find_all("div",{"class" : 'we-lockup__title '})
                            app_links=h2tags.find_all("a",{"class" : 'targeted-link'})
                            for z in app_links:
                                app_href=(z.attrs['href'])
                                app_names=z.find("div",{"class" : 'we-truncate we-truncate--single-line ember-view targeted-link__target'})
                                app_name=(app_names.get_text())
                                c[re.sub('[\s] +',' ',app_name).strip()]=re.sub('[\s] +',' ',app_href).strip()
                                a['similar apps']=c

                with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
                    w = csv.DictWriter(f, a.keys())
                    w.writeheader()
                    w.writerow(a)

                print(a)




crawl_all()
get_app_link()
get_app_data()
