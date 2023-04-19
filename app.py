import  streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    m_index= movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[m_index])), reverse=True, key=lambda x: x[1])
    rec_mve=[]
    for i in distances[1:6]:
        rec_mve.append(movies.iloc[i[0]].title)
    return rec_mve


m_dict=pickle.load(open('mvs.pkl','rb'))
movies=pd.DataFrame(m_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
m_list=movies['title'].values
st.title("Movie recommender system")
options=st.selectbox(
    "Please select movies from the given below options",
m_list
)
if st.button('Recommend a movie'):
    ms=recommend(options)
    st.write(options)
    for i in ms:
        st.write(i)