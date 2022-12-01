#Magic function that saves the code cell as a file

from mrjob.job import MRJob #import the mrjob library
from mrjob.step import MRStep #import the MRStep library
import csv #import the csv library
import time

#store columns names
columns = ['Unnamed: 0', 'date_', 'user_id_maped', 'program_name',
       'duration_seconds', 'program_class', 'season', 'episode',
       'program_desc', 'program_genre', 'series_title', 'hd', 'name',
       'rating']

class NoRatings(MRJob): # Create a class named NoRatings (number of Ratings )
    def steps(self): # Create method named steps and pass  the mapper and the reducer for MRStep 
        return[
            MRStep(mapper=self.mapping,
            reducer=self.reducing)
        ]
    
    #Create Mapper function 
    def mapping(self, _, line): #(_, line)ignore the key and take each line of the document as the value.
        reader = csv.reader([line]) #reader from csv file line by line
        for row in reader: # for loop to read rows 
            zipped=zip(columns,row) # creates a tuple  ,,, the columns is the key , row is the values
            diction = dict(zipped)
            rate = self.return_number(diction['rating'])
            movie_name = diction['name']
            genre = diction['program_genre']
            yield ((movie_name.lower(), genre.lower()), (rate, 1))  #outputing as key value pairs
    
    def return_number(self, num):
        if num == '1':
            return 1
        elif num in '2':
            return 2
        elif num in '3':
            return 3
        elif num in '4':
            return 4
        return 0

    
    def reducing(self, key, values):
        totalrate, totalviews = 0,0
        for value in values:
            totalrate += value[0]
            totalviews += value[1]
            average = round(totalrate/totalviews,2)
        yield ((key, average), totalviews)
    
if __name__ == "__main__":
    start = time.time()
    NoRatings.run()
    end = time.time()
    print(end-start)
