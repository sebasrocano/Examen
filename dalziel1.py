citypop = {}
import csv 

with open('../data/Dalziel2016_dat.csv', 'r') as f:
    my_csv = csv.DictReader(f)
    for line in my_csv:
        mycity = line['loc']
        cases = float(line['cases'])
        pop = float(line['pop'])
        citypop[mycity] = citypop.get(mycity, [0,0])
        citypop[mycity][0] = citypop[mycity][0] + pop
        citypop[mycity][1] = citypop[mycity][1] + cases
        
# Se integró la función avgcity 
     
def avgcity(city):  
    for city in citypop.keys():
            citypop[city][0] = citypop[city][0] / citypop[city][1]                                                            
    for city in ['BALTIMORE', 'BOSTON', 'BRIDGEPORT', 'BUFFALO', 'CHICAGO']:
             print(city,':', round(citypop[city][0],2)) 
    return None

avgcity(city= citypop)

cityyear = {}
import csv 
with open('../data/Dalziel2016_dat.csv', 'r') as f:
    my_csv = csv.DictReader(f)
    for line in my_csv:
        mycity = line['loc']
        year = line['year']
        cases = int(line['cases'])
        pop = float(line['pop'])        
        cityyear[mycity] = cityyear.get(mycity, {})        
        cityyear[mycity][year] = cityyear[mycity].get(year, [0,0])       
        cityyear[mycity][year][0] = cityyear[mycity][year][0] + pop       
        cityyear[mycity][year][1] = cityyear[mycity][year][1] + cases
for city in cityyear.keys():
    for year in cityyear[city].keys():
        cityyear[city][year][0] = cityyear[city][year][0] / cityyear[city][year][1]

        
years = list(cityyear['BALTIMORE'].keys())
years.sort()

# Se creó el archivo avgyear

def avgyear(years1):  
    for year in years:
         print(year, round(cityyear['BALTIMORE'][year][0]))
    return None

avgyear(years1=cityyear)



cityyear = {}
import csv 
with open('../data/Dalziel2016_dat.csv', 'r') as f:
    my_csv = csv.DictReader(f)
    for line in my_csv:
        mycity = line['loc']
        year = line['biweek']
        cases = int(line['cases'])
        pop = float(line['pop'])
        cityyear[mycity] = cityyear.get(mycity, {})
        cityyear[mycity][year] = cityyear[mycity].get(year, [0,0])
        cityyear[mycity][year][0] = cityyear[mycity][year][0] + pop
        cityyear[mycity][year][1] = cityyear[mycity][year][1] + cases
for city in cityyear.keys():
    for year in cityyear[city].keys():
        cityyear[city][year][0] = cityyear[city][year][0] / cityyear[city][year][1]

years = list(cityyear['CHICAGO'].keys())
years.sort()

# Se creó la función avgbiweek

def avgbiweek(biweeks1):  
    for year in years:
         print(year, round(cityyear['CHICAGO'][year][0]))
    return None

avgbiweek(biweeks1=city)
