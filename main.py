
from bs4 import BeautifulSoup
import requests
from csv import writer
from urllib.parse import urljoin

def find_jobs():
    with open(f'companies.csv','w', encoding='utf-8', newline='') as f:
        thewriter = writer(f)
        header = ['Company','Position']
        thewriter.writerow(header)
        url = 'https://merojob.com/category/it-telecommunication/'
        html_text = requests.get('https://merojob.com/category/it-telecommunication/').text
        soup = BeautifulSoup(html_text, 'lxml')
        # page_link_el = soup.select('.pagination a')
        for x in range(1,21):
            link = urljoin( url, '?page='+str(x) )
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'lxml')

            companies = soup.find_all('div',class_='card-body')

            for company in companies:
                company_name = company.find('a', class_='text-dark')
                    
                position_val = company.find('h1', class_='text-primary font-weight-bold media-heading h4')
                if company_name:
                    company_name = company_name.text.replace(' ','')
                    
                    if position_val:
                        position = position_val.find('a').text.replace(' ','')
                        info = [ company_name, position]
                        thewriter.writerow(info)
                
                

        
def find_grocery():
    with open(f'grocery_store.csv','w', encoding='utf-8', newline='') as f:
        thewriter = writer(f)
        header = ['Grocery Store']
        thewriter.writerow(header)
        url = 'https://www.seek.com.au/grocery-jobs/in-All-Sydney-NSW'
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')

        for x in range(1,15):
            link = urljoin( url, '?page='+str(x) )
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'lxml')

            stores = soup.find_all('div',class_='yvsb870 _1sx92fk0 _1sx92fk6')
            
            for store in stores:
                store_name = store.find('a',class_='l2mi890')
                if store_name:
                    store_name = store_name.text
                    info = [ store_name]
                    thewriter.writerow(info)
        
        
def find_mobile():

    with open(f'mobile_developers.csv','w', encoding='utf-8', newline='') as f:
        thewriter = writer(f)
        header = ['Company','location']
        thewriter.writerow(header)    
        url = 'https://techbehemoths.com/companies/mobile-app-development/nepal'
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        developers = soup.find_all('div',class_='co-list__itm')

        for developer in developers:
            developer_name_var = developer.find('p', class_='co-box__name')
            developer_name = developer_name_var.find('a').text.replace(' ','')
            
            location_var = developer.find('span',class_='co-box__loc-itm')
            location = location_var.find('a').text.replace(' ','')
            
            info = [ developer_name, location ]
            thewriter.writerow(info)   


def find_laptop():
    with open(f'laptop_repairs.csv','w', encoding='utf-8', newline='') as f:
        thewriter = writer(f)
        header = ['Shop','location','url']
        thewriter.writerow(header)     
        
        url = "https://www.experteasy.com.au/computer-repair"
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')

        service_providers = soup.find_all('li',class_='landing-list-item')
        
        for shop in service_providers:
            shop_name = shop.select('div > h3 >a')
            for x in shop_name:
                shop_name = x.text.replace(' ','')
            
            address = shop.select('h4 > span > span[itemprop="addressLocality"]')
            for x in address:
                address = x.text.replace(' ','')
            shop_url = 'https://www.experteasy.com.au/'+shop['faux-link']
            
            info = [ shop_name,address,shop_url]
            thewriter.writerow(info)  
            
        
def scrape():
    with open(f'countries.csv','w', encoding='utf-8', newline='') as f:
        thewriter = writer(f)
        header = ['Name','Capital','Population','Area']
        thewriter.writerow(header) 
        
        url = 'https://www.scrapethissite.com/pages/simple/'
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        
        countries = soup.find_all('div', class_='col-md-4 country')
        
        for country in countries:
            country_name = country.h3.text.replace(' ','')
            capital = country.find('span',class_='country-capital').text.replace(' ','')
            population = country.find('span',class_='country-population').text.replace(' ','')
            area = country.find('span',class_='country-area').text.replace(' ','')
            
            info = [country_name, capital, population,area]
            thewriter.writerow(info)
        
        
        

    
    

find_jobs()   
find_grocery()
find_mobile()
find_laptop()
scrape()

print ('All csv files are ready')




