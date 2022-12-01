# Stc-tv Recommendation System - HDFS and Mapreduce Capstone Project


<img src="https://drive.google.com/uc?export=view&id=1ISI6tfW3QMWiWWP95FuhvuHPkdZY2NGq"/>

## :round_pushpin: Table of contents
> * [Table of contents](#round_pushpin-table-of-contents)
> * [Vision 2030](#green_circle-vision-2030)
> * [Stc ](#purple_circleabout-stc)
> * [Stc-tv](#orange_circle-about-stc-tv)
> * [Data Review](#)
> * [Business problem](#)
> * [EDA](#bar_charteda)
> * [Approach](#)
> * [MapReduce Process](#)
> * [Implementation](#)
> * [Ruselt](#)
> * [Future work](#black_small_squarefuture-work)
> * [Web blog](#black_small_squarereal-Web_blog)
> * [Team Memebers](#octocatteam-memebers)

## :green_circle:	 Vision 2030
2030 vision introduced many ambitious goals to make huge leap in the Saudi economy and develop the local content, One of the programs of the 2030 vision (Quality of Life) which focus on improving the quality of life for the people & families.

## :purple_circle:	About Stc 

One of the Saudi digital companies who contribute on in improving the life of the singles & families is STC. Which is a pioneer digital company that provide digital solutions & services in many fields including telecommunications,  information technology, digital payments and digital media. 

## :orange_circle:		 About Stc-tv

In the field of digital media STC created (STC TV) to be the pioneer media provider of digital entertainment and the sport content in the Middle East. 
STC TV is an entertainment streaming service that provide you with the best movies, tv shows, documentaries, kids shows & more.


## :card_index_dividers:	Data Review
STC website provides the STC-TV dataset that was used in this case study.
It consists of 13 columns and 1048576 rows

### Columns:
> * User_id_maped : Unique ID
> * Date : date added
> * Program_name :  The Official name of the Program
> * Duration_seconds
> * Program_class : SERIES/EPISODES	and MOVIE
> * Season : Number of Season
> * Episode : Number of Episode
> * Program_desc :  Description of Program
> * Preogram genre: Action, Comedy ,Thriller etc.
> * Series_title : Title(Name) of the Series
> * HD
> * Original_name : The Official name of the movie/Series
> * Rating


## Business problem

The business problem here is that we want an insight into the movies/series to build a future
decision and answer those questions: what kind of movies/series to go for? , what is the
feedback on the current movies/series? and what kind of movies/series do users prefer?


##  :bar_chart:	EDA

<img src="https://drive.google.com/uc?export=view&id=1VskBxHOlTph3rtQsJ5JZbzehJIEyLnpX"/>



## Approach

Our approach to solving this problem is building a MapReduce function that counts the views of the movies/series along with the names of the movies/series and counts the average rating provided by users. We implemented a python MapReduce function and we used Hadoop MapReduce to run the code.



## MapReduce Process

Hadoop MapReduce processes the massive amount of structured and unstructured data
stored in HDFS. MapReduce works in five phases:

Input Splitting:  MapReduce splits the inputs into chunks called input splits; each piece represents a portion of work with a single mapper task.
Mapping: The input data is processed and divided into smaller segments.
Shuffling: The output of the mapper phase is passed to the reducer after removing any duplicate values and grouping the values
Sorting: It's responsible for merging and sorting the output of the mappers. 
Reducing: the intermediate values from the shuffling step are reduced to produce a single output value that summarizes the entire dataset. HDFS is then used to store the final output.

## Implementation
<img src="https://drive.google.com/uc?export=view&id=1lHJ2vPSc5NzSyzGlF4cskBpz_T6oKhD3"/>

mrjobis a package for writing map-reduce jobs in python very quickly, it abstracts away all the complexities of dealing with the streaming interfaces

<img src="https://drive.google.com/uc?export=view&id=157eNAJgjs1S-Bi6K56xrk4LDuvjDWpgQ"/>

First we created a class named NoRatings (number of Ratings) then we created a function named steps and pass the mapper and the reducer for MRStep.

Then we created a mapper function which is read the data line by line by using "reader" and it's for loop to create a tuple and dictionary then store the rate, movies and program_genre to return them.

<img src="https://drive.google.com/uc?export=view&id=1l4xFn4mMHlpjSXRtVyZ0gTjuNLxkZi7R"/>

Finally, we create the reducing function that counts the total rate and total views, takes the average, and returns the program name with its average and total views.


## Ruselt

Running the python code into Hadoop
<img src="https://drive.google.com/uc?export=view&id=1v5W4YYXeRvrody3LM1kIbjkQiwMPLvKb"/>
As you can see the GPU time spent is 98450 milliseconds

<img src="https://drive.google.com/uc?export=view&id=1tZsGCLfjlyTCob-Mk7h14Ql5_DMbL19-"/>

## Future work
<img src="https://drive.google.com/uc?export=view&id=1ULGG0WeoDibrdsDRuwY84J4_UNrJh4Dm"/>





## :black_small_square:	Web blog
https://biggerthandata.blogspot.com/2022/11/hadoop-and-mapreduce-weekly-project.html

## :octocat:	Team Memebers

- [Abdullah Huwaishel](https://github.com/hush966)
- [Afnan Alzahrani](https://github.com/AfnanAlzahrani)
- [Jumana Almussa](https://github.com/jumana0)
- [Mahmuod Alhassan](https://github.com/alhassanm)
- [Amjad Almusallam](https://github.com/ASM650)



# SDA - Machine learning - Recommendation System - CodingDojo - Vision 2030 - stc - stc-tv

