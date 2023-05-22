from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_movies = movies_data[['original_title','poster_link','release_date','runtime','weighted_rating']]


# variables to store data
liked_movies = []
disliked_movies = []
did_not_watch = []


# method to fetch data from database
def assigned_val():
  m_data = {
    'original_title': all_movies.iloc[0,0],
    'poster_link' : all_movies.iloc[0,1],
    'release_date' : all_movies.iloc[0,2] or 'na' ,
    'runtime' : all_movies.iloc[0,3],
    'weighted_rating' : all_movies.iloc[0,4]/2
  }
  return m_data

# /movies api
@app.route('/movies')
def get_movies():
  movies_data = assigned_val()
  return jsonify({
    'data' : movies_data,
    'status' : 'sucess',

  })


# /like api
@app.route('/like')
def liked():
  global all_movies_movies 
  movies_data = assigned_val()
  liked_movies.append(movies_data)
  all_movies.drop([0],inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
    
    'status' : 'sucess'
    
  })


# /dislike api
@app.route('/dislike')
def disliked():
  global all_movies 
  movies_data = assigned_val()
  disliked_movies.append(movies_data)
  all_movies.drop([0],inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
    
    'status' : 'sucess'
    
  })


# /did_not_watch api
@app.route('/like')
def did_not_watch():
  global all_movies 
  movies_data = assigned_val()
  did_not_watch.append(movies_data)
  all_movies.drop([0],inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
    
    'status' : 'sucess'
    
  })

if __name__ == "__main__":
  app.run()