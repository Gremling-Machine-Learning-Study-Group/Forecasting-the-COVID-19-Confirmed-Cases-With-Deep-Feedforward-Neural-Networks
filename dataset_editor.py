import csv
import datetime

#reference the file as f an get a parsed file:
f = open('brazil_covid19.csv')
csv_f = csv.reader(f)

'''
obs. about the rows of the csv:
date_of_confirmation|hour|state|suspects|refused|confirmed|deaths
'''

'''
#print just "Minas Gerais" rows:
for row in csv_f:
    if(row[2]=='Minas Gerais'):
        print(row)
'''

'''
#print just the date, confimerd cases and deaths:
for row in csv_f:
    if(row[2]=='Minas Gerais'):
        print(row[0],row[5],row[6])
'''

#create lists:
date = []
confirmed_cases = []
death_cases = []

date_datetime_format = []

date_day_of_the_year = []

#append data to the lists
for row in csv_f:
    
    if(row[2]=='Minas Gerais'):
        
        date.append(row[0])
        confirmed_cases.append(row[5])
        death_cases.append(row[6])

#convert strs of the list date in datetime object
for i in range(len(date)):
    #put the days (int) in the date_datetime_format
    date_datetime_format.append(datetime.datetime.strptime(date[i], '%Y-%m-%d').strftime('%d'))

#convert the "day of the month" in the "day of the year"
for i in range(len(date_datetime_format)):
    #january
    if(i<=1):
        date_day_of_the_year.append(int(date_datetime_format[i]))
    #february
    elif(i<=32):
        date_day_of_the_year.append(int(date_datetime_format[i])+31)
    #march
    elif(i<=63):
        date_day_of_the_year.append(int(date_datetime_format[i])+60)
    
#create files so we can store our data to train the neural network:
file_cases = open("dataset_cases_21032020.txt", "w+")
file_deaths = open("dataset_deaths_21032020.txt", "w+")
    
#there are days where the number of cases were notified two times.
#so lets skip the oldest notification from the same day:
for i in range(len(date_day_of_the_year)):
    
    if((i+1!=len(date_day_of_the_year))and(date_day_of_the_year[i]!=date_day_of_the_year[i+1])):
        
        #confirmed cases dataset: day of the year X confirmed cases:
        file_cases.write(str(date_day_of_the_year[i]))
        file_cases.write(" ")
        file_cases.write(str(confirmed_cases[i]))
        file_cases.write("\n")
        
        #death cases dataset: day of the year X death cases:
        file_deaths.write(str(date_day_of_the_year[i]))
        file_deaths.write(" ")
        file_deaths.write(str(death_cases[i]))
        file_deaths.write("\n")
            
        #print(date_day_of_the_year[i],confirmed_cases[i],death_cases[i])
    
    elif(i==len(date_day_of_the_year)-1):
        
        #last day of the dataset for confimad cases:
        file_cases.write(str(date_day_of_the_year[i]))
        file_cases.write(" ")
        file_cases.write(str(confirmed_cases[i]))
        file_cases.write("\n")
        
        #last day of the dataset for death cases
        file_deaths.write(str(date_day_of_the_year[i]))
        file_deaths.write(" ")
        file_deaths.write(str(death_cases[i]))
        file_deaths.write("\n")
        
        #print(date_day_of_the_year[i],confirmed_cases[i],death_cases[i])

#close the instances of the files
file_cases.close()
file_deaths.close()
