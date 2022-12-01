# Stc-tv Recommendation System - ML Capstone Project


<img src="https://drive.google.com/uc?export=view&id=14pxZ2LMX6Yvn3NrDHi5cluWCldARvKR0"/>


## :round_pushpin: Table of contents
> * [Table of contents](#round_pushpin-table-of-contents)
> * [Vision 2030](#green_circle-vision-2030)
> * [About Stc & Stc-tv](#purple_circleabout-stc)
> * [Stc-tv](#orange_circle-about-stc-tv)
> * [Our target](#dartour-target)
> * [Stc-tv dataset](#card_index_dividersstc-tv-dataset)
> * [EDA](#bar_charteda)
> * [Dashboard](#bar_chartchart_with_downwards_trendchart_with_upwards_trenddashboard)
> * [Preprocessing](#gear-preprocessing)
> * [Recommendation System](#black_small_squarerecommendation-system)
> * [Real world project](#black_small_squarereal-world-project)
> * [Future work](#black_small_squarefuture-work)
> * [Web blog](#black_small_squarereal-Web_blog)
> * [Resource](#file_folder-resource)
> * [Team Memebers](#octocatteam-memebers)

## :green_circle:	 Vision 2030
2030 vision introduced many ambitious goals to make huge leap in the Saudi economy and develop the local content, One of the programs of the 2030 vision (Quality of Life) which focus on improving the quality of life for the people & families.

## :purple_circle:	About Stc 

One of the Saudi digital companies who contribute on in improving the life of the singles & families is STC. Which is a pioneer digital company that provide digital solutions & services in many fields including telecommunications,  information technology, digital payments and digital media. 

## :orange_circle:		 About Stc-tv

In the field of digital media STC created (STC TV) to be the pioneer media provider of digital entertainment and the sport content in the Middle East. 
STC TV is an entertainment streaming service that provide you with the best movies, tv shows, documentaries, kids shows & more.


##  :dart:	Our target
So our vision target for this project is to contribute efficiently in developing a recommendation system for the viewer which will improve his quality of life, with the implementing the latest AI technology.

## :card_index_dividers:	Stc-tv dataset
STC website provides the STC-TV dataset that was used in this case study.
It consists of 13 columns and 3598607 rows.

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

We used another dataset that had the same columns but with an additional column called "rating", and because the program_desc column wasn't enough for the recommendation system that we wanted to build,we collected data for the description by using web scraping
The rating and description columns are added to the main dataset. 

##  :bar_chart:	EDA
### - The percentage of movies and series that STC-TV have.

<img src="https://drive.google.com/uc?export=view&id=10DXqQBTKNQBE_w7u6YFp941XZ9TkBjgs"/>


### - Animation is the most popular genre in movies and series, while horror is the least popular.

<img src="https://drive.google.com/uc?export=view&id=1UQR9xxQJ6NV0Awzm_tuHyW1lI6neDbW1"/>
<img src="https://drive.google.com/uc?export=view&id=18a9yFai903JyDzFP4jXiU9_7biVvR0GQ"/>


### - This plots shows the total number of users watching and the total duration spent by program class. The majority of time is spent on series, which is understandable given the series long duration, but most users prefer to watch movies. 

<img src="https://drive.google.com/uc?export=view&id=1G4g3MDL3241h-1gai9walvwwFyaQe64A"/>

### - Here, we study the relationship and the user's behavior against the HD flag. As you can see, the majority prefers HD for series and movies. 
<img src="https://drive.google.com/uc?export=view&id=1JIDWojZEURBrf8yAqURjwmYHxqsmYV_y"/>

### - The highest total watched program is "The Boss Baby" and the lowest is "The Amazing Spider-Man".
<img src="https://drive.google.com/uc?export=view&id=1d41lyt2v_Gu3LZ07X3H1NSn63Xot2pzf"/>


### - The number of users who watched and rated the program class
<img src="https://drive.google.com/uc?export=view&id=1KRdSCYSvaq9b_U7VAw9nvoQHDR4DGKBw"/>


### - The most frequently used words in the program description
<img src="https://drive.google.com/uc?export=view&id=1gNu-1QiOuU91Ur8hc3sSi37dZKr-ScW3"/>



##  :bar_chart:	:chart_with_downwards_trend:	:chart_with_upwards_trend:	Dashboard
<img src="https://drive.google.com/uc?export=view&id=1bzgvKqS6F_YNRp1nWUNCjgHvxtVhXVG_"/>





## :gear:	 Preprocessing

First, we checked for missing values.
All good except the "program_desc" column, so we reset the program_desc column to have this information (genre, class, name, hd) because we will be adding a description column that was gathered from web scraping.

Then we set the program genre for the programs that were not specified. 

we dropped unnecessary columns like: season, episode, series_title, date and program_name.

Converting the duration seconds to hours by divide the sec to 3600.

Then we join the description(gathered from web scraping) with movies names. Then we dropped the null and duplicated values.



After that, we created a function that did the following process: 
made the text a string with all characters in lower case, removed all punctuation and differentiating characters from the text, splits a string into a list and finally, the word lemmatizer.

After cleaning the data we apply CountVectorizer(Converting a collection of text documents to a matrix of token counts) on the description text with max_df=0.80, min_df=2 parameters.

Finally, we use pickle to save the matrices. 


## :black_small_square:		Recommendation System
 Recommendation Systems are a type of information filtering systems as they improve the quality of search results and provides items that are more relevant to the search item or are realted to the search history of the user.

> * Content-based : 
In the content-based recommendation system we created three functions:
The first one for the program description that contains (the movie name, movie class, movie genre, and whether it's HD or not),
The second function was for the description that we gathered from the web scrapping.
The third function contains both the program description and the description.

> * Collaborative Filtering: 
In the collaborative filtering, we used the user's ids, movies names, and ratings.



## :black_small_square:	Real world project 
<img src="https://drive.google.com/uc?export=view&id=1-ueAQ-hmeRI_JngiBj2PTZRA7aL1ICZf"/>
<h3><a href="https://github.com/alhassanm/BDAI-demo_project-capstone-project-1">Go to domo project repository for this project</a></h3>

 
## :black_small_square:	Future work
> * Gathering pictures
> * Deploy the webpage in global  server
> * Upload pictures for the results in webpage

## :black_small_square:	Web blog
https://biggerthandata.blogspot.com/2022/11/stc-tv-recommendation-system-ml.html
 
## :file_folder: Resource
- Data Resource : https://lab.stc.com.sa/dataset/ar/ 

## :octocat:	Team Memebers

- [Abdullah Huwaishel](https://github.com/hush966)
- [Afnan Alzahrani](https://github.com/AfnanAlzahrani)
- [Jumana Almussa](https://github.com/jumana0)
- [Mahmuod Alhassan](https://github.com/alhassanm)
- [Amjad Almusallam](https://github.com/ASM650)



# SDA - Machine learning - Recommendation System - CodingDojo - Vision 2030 - stc - stc-tv

