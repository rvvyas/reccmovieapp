import streamlit as st
import pickle
import requests

movies= pickle.load(open('movie_list.pkl','rb'))
movies_list = movies['title'].values
similarty = pickle.load(open('similarity.pkl','rb'))
top20 = pickle.load(open('top20.pkl','rb'))
top_grossing = pickle.load(open('top_grossing.pkl','rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarty[index])),reverse=True,key = lambda x: x[1])
    recommended_movies = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
        
        
    return recommended_movies,recommended_movie_posters


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

st.title('Movie Recommender')

tab1,tab2,tab3 = st.tabs(['Movie Recommender','Top Movies','Top Grossing'])

#-------------------------------Tab 1----------------------------------------#

with tab1:
    st.header('Movie Recommender')

selected_movie = st.selectbox('Select the movie or you can search also!',movies_list)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.write(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.write(recommended_movie_names[1])
    with col3:
        st.image(recommended_movie_posters[2])
        st.write(recommended_movie_names[2])
    with col4:
        st.image(recommended_movie_posters[3])
        st.write(recommended_movie_names[3])
    with col5:
        st.image(recommended_movie_posters[4])
        st.write(recommended_movie_names[4])
        
#------------------------------------Tab 2-------------------------------------------#
               
with tab2:
    st.header('Top 30 Movies')
    
    col1,col2,col3,col4,col5 = st.columns(5,gap="small")

    with col1:
        st.image(fetch_poster(top20['movie_id'].values[0]))
        st.write(top20['title'].values[0])
        st.caption('Ratings : '+top20['vote_average'].values[0].astype(str))

    with col2:
        st.image(fetch_poster(top20['movie_id'].values[1]))
        st.write(top20['title'].values[1])
        st.caption('Ratings : '+top20['vote_average'].values[1].astype(str))

    with col3:
        st.image(fetch_poster(top20['movie_id'].values[2]))
        st.write(top20['title'].values[2])
        st.caption('Ratings : '+top20['vote_average'].values[2].astype(str))

    with col4:
        st.image(fetch_poster(top20['movie_id'].values[3]))
        st.write(top20['title'].values[3])
        st.caption('Ratings : '+top20['vote_average'].values[3].astype(str))

    with col5:
        st.image(fetch_poster(top20['movie_id'].values[4]))
        st.write(top20['title'].values[4])
        st.caption('Ratings : '+top20['vote_average'].values[4].astype(str))
        
        
        #-----------second row---------------#
        
    col6,col7,col8,col9,col10 = st.columns(5,gap="small")
        
    with col6:
        st.image(fetch_poster(top20['movie_id'].values[5]))
        st.write(top20['title'].values[5])
        st.caption('Ratings : '+top20['vote_average'].values[5].astype(str))

    with col7:
        st.image(fetch_poster(top20['movie_id'].values[6]))
        st.write(top20['title'].values[6])
        st.caption('Ratings : '+top20['vote_average'].values[6].astype(str))

    with col8:
        st.image(fetch_poster(top20['movie_id'].values[7]))
        st.write(top20['title'].values[7])
        st.caption('Ratings : '+top20['vote_average'].values[7].astype(str))

    with col9:
        st.image(fetch_poster(top20['movie_id'].values[8]))
        st.write(top20['title'].values[8])
        st.caption('Ratings : '+top20['vote_average'].values[8].astype(str))

    with col10:
        st.image(fetch_poster(top20['movie_id'].values[9]))
        st.write(top20['title'].values[9])
        st.caption('Ratings : '+top20['vote_average'].values[9].astype(str))
        
        
        #---------Third row---------------
        
    
    col11,col12,col13,col14,col15 = st.columns(5,gap="small")
    
    
    with col11:
        st.image(fetch_poster(top20['movie_id'].values[10]))
        st.write(top20['title'].values[10])
        st.caption('Ratings : '+top20['vote_average'].values[10].astype(str))

    with col12:
        st.image(fetch_poster(top20['movie_id'].values[11]))
        st.write(top20['title'].values[11])
        st.caption('Ratings : '+top20['vote_average'].values[11].astype(str))

    with col13:
        st.image(fetch_poster(top20['movie_id'].values[12]))
        st.write(top20['title'].values[12])
        st.caption('Ratings : '+top20['vote_average'].values[12].astype(str))

    with col14:
        st.image(fetch_poster(top20['movie_id'].values[13]))
        st.write(top20['title'].values[13])
        st.caption('Ratings : '+top20['vote_average'].values[13].astype(str))

    with col15:
        st.image(fetch_poster(top20['movie_id'].values[14]))
        st.write(top20['title'].values[14])
        st.caption('Ratings : '+top20['vote_average'].values[14].astype(str))
        
        #------------ Fourth Row-------------#
        
        
    col16,col17,col18,col19,col20 = st.columns(5,gap="small")
    
    with col16:
        st.image(fetch_poster(top20['movie_id'].values[15]))
        st.write(top20['title'].values[15])
        st.caption('Ratings : '+top20['vote_average'].values[15].astype(str))

    with col17:
        st.image(fetch_poster(top20['movie_id'].values[16]))
        st.write(top20['title'].values[16])
        st.caption('Ratings : '+top20['vote_average'].values[16].astype(str))

    with col18:
        st.image(fetch_poster(top20['movie_id'].values[17]))
        st.write(top20['title'].values[17])
        st.caption('Ratings : '+top20['vote_average'].values[17].astype(str))

    with col19:
        st.image(fetch_poster(top20['movie_id'].values[18]))
        st.write(top20['title'].values[18])
        st.caption('Ratings : '+top20['vote_average'].values[18].astype(str))

    with col20:
        st.image(fetch_poster(top20['movie_id'].values[19]))
        st.write(top20['title'].values[19])
        st.caption('Ratings : '+top20['vote_average'].values[19].astype(str))
        
        
         #------------ Fifth Row-------------#
        
        
    col21,col22,col23,col24,col25 = st.columns(5,gap="small")

    with col21:
        st.image(fetch_poster(top20['movie_id'].values[20]))
        st.write(top20['title'].values[20])
        st.caption('Ratings : '+top20['vote_average'].values[20].astype(str))

    with col22:
        st.image(fetch_poster(top20['movie_id'].values[21]))
        st.write(top20['title'].values[21])
        st.caption('Ratings : '+top20['vote_average'].values[21].astype(str))

    with col23:
        st.image(fetch_poster(top20['movie_id'].values[22]))
        st.write(top20['title'].values[22])
        st.caption('Ratings : '+top20['vote_average'].values[22].astype(str))

    with col24:
        st.image(fetch_poster(top20['movie_id'].values[23]))
        st.write(top20['title'].values[23])
        st.caption('Ratings : '+top20['vote_average'].values[23].astype(str))

    with col25:
        st.image(fetch_poster(top20['movie_id'].values[24]))
        st.write(top20['title'].values[24])
        st.caption('Ratings : '+top20['vote_average'].values[24].astype(str))
        
        #------------ Sixth Row-------------#
        
    col26,col27,col28,col29,col30 = st.columns(5,gap="small")
    
    with col26:
        st.image(fetch_poster(top20['movie_id'].values[25]))
        st.write(top20['title'].values[25])
        st.caption('Ratings : '+top20['vote_average'].values[25].astype(str))

    with col27:
        st.image(fetch_poster(top20['movie_id'].values[26]))
        st.write(top20['title'].values[26])
        st.caption('Ratings : '+top20['vote_average'].values[26].astype(str))

    with col28:
        st.image(fetch_poster(top20['movie_id'].values[27]))
        st.write(top20['title'].values[27])
        st.caption('Ratings : '+top20['vote_average'].values[27].astype(str))

    with col29:
        st.image(fetch_poster(top20['movie_id'].values[28]))
        st.write(top20['title'].values[28])
        st.caption('Ratings : '+top20['vote_average'].values[28].astype(str))

    with col30:
        st.image(fetch_poster(top20['movie_id'].values[29]))
        st.write(top20['title'].values[29])
        st.caption('Ratings : '+top20['vote_average'].values[29].astype(str))
        
#------------------------------Tab 3 ----------------------------------------#
        
        
with tab3:
    st.header('Top Grossing Movies of All Time')
    
    col1,col2,col3,col4,col5 = st.columns(5,gap="small")

    with col1:
        st.image(fetch_poster(top_grossing['movie_id'].values[0]))
        st.write(top_grossing['title'].values[0])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[0].astype(str)+'M')

    with col2:
        st.image(fetch_poster(top_grossing['movie_id'].values[1]))
        st.write(top_grossing['title'].values[1])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[1].astype(str)+'M')

    with col3:
        st.image(fetch_poster(top_grossing['movie_id'].values[2]))
        st.write(top_grossing['title'].values[2])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[2].astype(str)+'M')

    with col4:
        st.image(fetch_poster(top_grossing['movie_id'].values[3]))
        st.write(top_grossing['title'].values[3])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[3].astype(str)+'M')

    with col5:
        st.image(fetch_poster(top_grossing['movie_id'].values[4]))
        st.write(top_grossing['title'].values[4])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[4].astype(str)+'M')
        
        
        #-----------second row---------------#
        
    col6,col7,col8,col9,col10 = st.columns(5,gap="small")
        
    with col6:
        st.image(fetch_poster(top_grossing['movie_id'].values[5]))
        st.write(top_grossing['title'].values[5])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[5].astype(str)+'M')

    with col7:
        st.image(fetch_poster(top_grossing['movie_id'].values[6]))
        st.write(top_grossing['title'].values[6])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[6].astype(str)+'M')

    with col8:
        st.image(fetch_poster(top_grossing['movie_id'].values[7]))
        st.write(top_grossing['title'].values[7])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[7].astype(str)+'M')

    with col9:
        st.image(fetch_poster(top_grossing['movie_id'].values[8]))
        st.write(top_grossing['title'].values[8])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[8].astype(str)+'M')

    with col10:
        st.image(fetch_poster(top_grossing['movie_id'].values[9]))
        st.write(top_grossing['title'].values[9])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[9].astype(str)+'M')
        
        
        #---------Third row---------------
        
    
    col11,col12,col13,col14,col15 = st.columns(5,gap="small")
    
    
    with col11:
        st.image(fetch_poster(top_grossing['movie_id'].values[10]))
        st.write(top_grossing['title'].values[10])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[10].astype(str)+'M')

    with col12:
        st.image(fetch_poster(top_grossing['movie_id'].values[11]))
        st.write(top_grossing['title'].values[11])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[11].astype(str)+'M')

    with col13:
        st.image(fetch_poster(top_grossing['movie_id'].values[12]))
        st.write(top_grossing['title'].values[12])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[12].astype(str)+'M')

    with col14:
        st.image(fetch_poster(top_grossing['movie_id'].values[13]))
        st.write(top_grossing['title'].values[13])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[13].astype(str)+'M')

    with col15:
        st.image(fetch_poster(top_grossing['movie_id'].values[14]))
        st.write(top_grossing['title'].values[14])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[14].astype(str)+'M')
        
        #------------ Fourth Row-------------#
        
        
    col16,col17,col18,col19,col20 = st.columns(5,gap="small")
    
    with col16:
        st.image(fetch_poster(top_grossing['movie_id'].values[15]))
        st.write(top_grossing['title'].values[15])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[15].astype(str)+'M')

    with col17:
        st.image(fetch_poster(top_grossing['movie_id'].values[16]))
        st.write(top_grossing['title'].values[16])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[16].astype(str)+'M')

    with col18:
        st.image(fetch_poster(top_grossing['movie_id'].values[17]))
        st.write(top_grossing['title'].values[17])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[17].astype(str)+'M')

    with col19:
        st.image(fetch_poster(top_grossing['movie_id'].values[18]))
        st.write(top_grossing['title'].values[18])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[18].astype(str)+'M')

    with col20:
        st.image(fetch_poster(top_grossing['movie_id'].values[19]))
        st.write(top_grossing['title'].values[19])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[19].astype(str)+'M')
        
        
    #------------ Fourth Row-------------#
    
    
    col21,col22,col23,col24,col25 = st.columns(5,gap="small")

    with col21:
        st.image(fetch_poster(top_grossing['movie_id'].values[20]))
        st.write(top_grossing['title'].values[20])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[20].astype(str)+'M')

    with col22:
        st.image(fetch_poster(top_grossing['movie_id'].values[21]))
        st.write(top_grossing['title'].values[21])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[21].astype(str)+'M')

    with col23:
        st.image(fetch_poster(top_grossing['movie_id'].values[22]))
        st.write(top_grossing['title'].values[22])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[22].astype(str)+'M')

    with col24:
        st.image(fetch_poster(top_grossing['movie_id'].values[23]))
        st.write(top_grossing['title'].values[23])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[23].astype(str)+'M')

    with col25:
        st.image(fetch_poster(top_grossing['movie_id'].values[24]))
        st.write(top_grossing['title'].values[24])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[24].astype(str)+'M')
        
        
    #------------ Sixth Row-------------#
    
    col26,col27,col28,col29,col30 = st.columns(5,gap="small")
    
    with col26:
        st.image(fetch_poster(top_grossing['movie_id'].values[25]))
        st.write(top_grossing['title'].values[25])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[25].astype(str)+'M')

    with col27:
        st.image(fetch_poster(top_grossing['movie_id'].values[26]))
        st.write(top_grossing['title'].values[26])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[26].astype(str)+'M')

    with col28:
        st.image(fetch_poster(top_grossing['movie_id'].values[27]))
        st.write(top_grossing['title'].values[27])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[27].astype(str)+'M')

    with col29:
        st.image(fetch_poster(top_grossing['movie_id'].values[28]))
        st.write(top_grossing['title'].values[28])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[28].astype(str)+'M')

    with col30:
        st.image(fetch_poster(top_grossing['movie_id'].values[29]))
        st.write(top_grossing['title'].values[29])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[29].astype(str)+'M')
        
        
    #------------ Seventh Row-------------#

    
    col31,col32,col33,col34,col35 = st.columns(5,gap="small")
    
    with col31:
        st.image(fetch_poster(top_grossing['movie_id'].values[30]))
        st.write(top_grossing['title'].values[30])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[30].astype(str)+'M')

    with col32:
        st.image(fetch_poster(top_grossing['movie_id'].values[31]))
        st.write(top_grossing['title'].values[31])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[31].astype(str)+'M')

    with col33:
        st.image(fetch_poster(top_grossing['movie_id'].values[32]))
        st.write(top_grossing['title'].values[32])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[32].astype(str)+'M')

    with col34:
        st.image(fetch_poster(top_grossing['movie_id'].values[33]))
        st.write(top_grossing['title'].values[33])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[33].astype(str)+'M')

    with col35:
        st.image(fetch_poster(top_grossing['movie_id'].values[34]))
        st.write(top_grossing['title'].values[34])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[34].astype(str)+'M')
        
        
    #------------ Eight Row-------------#
    
    col36,col37,col38,col39,col40 = st.columns(5,gap="small")
    
    with col36:
        st.image(fetch_poster(top_grossing['movie_id'].values[35]))
        st.write(top_grossing['title'].values[35])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[35].astype(str)+'M')

    with col37:
        st.image(fetch_poster(top_grossing['movie_id'].values[36]))
        st.write(top_grossing['title'].values[36])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[36].astype(str)+'M')

    with col38:
        st.image(fetch_poster(top_grossing['movie_id'].values[37]))
        st.write(top_grossing['title'].values[37])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[37].astype(str)+'M')

    with col39:
        st.image(fetch_poster(top_grossing['movie_id'].values[38]))
        st.write(top_grossing['title'].values[38])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[38].astype(str)+'M')
        
    with col40:
        st.image(fetch_poster(top_grossing['movie_id'].values[39]))
        st.write(top_grossing['title'].values[39])
        st.caption('Revenue : '+'$'+top_grossing['revenue'].values[39].astype(str)+'M')