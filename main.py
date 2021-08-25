#
#   This test was created by dennis_rocha
# 
#   The starting url is https://sample-university-site.herokuapp.com/approvals/1
#   The test must contain:
#       * Persistence in SQL database (Postgree, MySQL, or any other database you feel comfortable with)
#       * Perform data hygiene
#       * Validate the CPFs contained (valid and not valid numerically)
#       * performance on the site where the data is scraping 
#       
#   







from unicodedata import normalize
import re
import scrapy
from error import errorRequest
from saveData import MongoDb


class CandidateTest(scrapy.Spider):
    name = "Candidate Scrapy Test"
    start_urls = ["https://sample-university-site.herokuapp.com"]
    
    url_init = "https://sample-university-site.herokuapp.com"
    db = MongoDb() #host default 'mongodb://localhost:27017/'
    
    
    def parse(self, response):
        if response.status == 200: #If request status != 200 save error
            links = response.xpath("//li//a/@href").getall() #Capture all links CPFs
             
            if links: #page 4672 dont have 
                for link in links:
                    yield scrapy.Request(
                        self.url_init+link,
                        callback=self.parse_candidate
                    )
                    
            else:
                errorRequest(404, response.url, "Dont Have Data")    
        
        else:
            errorRequest(response.status, response.url)
            
        yield scrapy.Request(
            self.url_init+response.xpath('//div//a/@href').get(), #Page 4672 dont have button 'next'
            callback=self.parse #Call the parse function again on the next page
        )
        
    def parse_candidate(self, response):
        if response.status == 200:
            filters_name = ["JR" , "MRS", "I" , "II" , "III" , "IV" , "V", "MR", "DR", "MS", "MSS" ,"MISS", "SR","MD","DDS","DVM","PHD","DM"] #list to clear names
            
            try:
                name = response.css('div::text').getall()[0].strip()
                score = response.css('div::text').getall()[1].strip()
                cpf = str(response).split('/')[-1] #Get the url from 'response' and divide into '/' get the last index (cpf)
                                                     
            
            except:
                errorRequest(404, response.url, "Dont Have Data")
                
            else:
                name = normalize('NFKD', name).encode('ASCII','ignore').decode('ASCII').upper() #remove special characters (é, á, ã, ç, etc) and capitalize
                name = re.sub(r"[.,;:!?]", "", name) #Remove '.,:' in the name 
                
                data = {
                    'name': " ".join(["" if char in filters_name else char for char in name.split(" ")]).strip(), #If any words contained in the name and in the filter list (filters_name) will be removed from the name
                    'cpf': "".join(re.findall('[0-9]',cpf)), #only numbers will be captured
                    'score': re.sub(r"[,;:]", ".", score) #If there is ',;:' it will be replaced by '.'
                }
                
                #Saving data in MongoDB
                self.db.insert_one({
                    "status":response.status,
                    "url": response.url,
                    "data":data
                })
                
                yield data
            
        else:
            errorRequest(response.status, response.url)