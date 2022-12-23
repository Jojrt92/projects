import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

import pandas as pd
import numpy as np
import pickle

#----------------------------Import file---------------------------------#
df = pickle.load(open("dataset/df_for_deployment.pkl","rb"))
df = pd.DataFrame(df)
corpus = []
for words in df['cleaned']:
    corpus.append(words.split())

google_model = pickle.load(open('model/word2vec_model.sav','rb'))

#----------------------------Functions---------------------------------#
def is_word_in_model(word, model):
    """
    Check on individual words ``word`` that it exists in ``model``.
    """
    assert type(model).__name__ == 'KeyedVectors'
    is_in_vocab = word in model.key_to_index.keys()
    return is_in_vocab

def predict(query_sentence, dataset, model, topk=5):
    query_sentence = query_sentence.split()
    in_vocab_list, best_index = [], [0]*topk
    for w in query_sentence:
        # remove unseen words from query sentence
        if is_word_in_model(w, model.wv):
            in_vocab_list.append(w)
    # Retrieve the similarity between two words as a distance
    if len(in_vocab_list) > 0:
        sim_mat = np.zeros(len(dataset))  # TO DO
        for i, sentence in enumerate(dataset):
            if sentence:
                sim_sentence = model.wv.n_similarity(
                        in_vocab_list, sentence)
            else:
                sim_sentence = 0
            sim_mat[i] = np.array(sim_sentence)
        # Take the five highest norm
        best_index = np.argsort(sim_mat)[::-1][:topk]
    return best_index

#----------------------------Layout---------------------------------#

st.title("Doppler Recommender")

st.write("This recommendation system is built on the dataset of Amazon's beauty products. With upwards of more than 30,000+ products to choose from, you will definitely get what your heart desires!")
st.subheader("Input your queries and the app will do the rest of the work!")

user_text = st.text_input("Searching for something?")

if st.button("Search"):
    st.header("Will you be interested in these products")
    best_index = predict(user_text, corpus, google_model)    
    df_rec = df[['product', 'brand', 'price','review', 'average_reviewer_score', 'imageURLHighRes']].iloc[best_index]
    with st.container():
        col1,col2,col3,col4,col5 = st.columns(5)
        with col1:
            st.write(df_rec["product"][0])
            st.write(df_rec["average_reviewer_score"][0]+" :star:")
            st.write("Brand: "+df_rec["brand"][0])
            st.write("Price: "+df_rec["price"][0])
            st.image(df_rec['imageURLHighRes'][0])
            with st.expander("See what people say about this product"):
                st.write(df_rec['review'][0])
        with col2:
            st.write(df_rec["product"][1])
            st.write(df_rec["average_reviewer_score"][1]+" :star:")
            st.write("Brand: "+df_rec["brand"][1])
            st.write("Price: "+df_rec["price"][1])
            st.image(df_rec['imageURLHighRes'][1])
        
        with col3:
            st.write(df_rec["product"][2])
            st.write(df_rec["average_reviewer_score"][2]+" :star:")
            st.write("Brand: "+df_rec["brand"][2])
            st.write("Price: "+df_rec["price"][2])
            st.image(df_rec['imageURLHighRes'][2])
            
        with col4:
            st.write(df_rec["product"][3])
            st.write(df_rec["average_reviewer_score"][3]+" :star:")
            st.write("Brand: "+df_rec["brand"][3])
            st.write("Price: "+df_rec["price"][3])
            st.image(df_rec['imageURLHighRes'][3])
            
        with col5:
            st.write(df_rec["product"][4])
            st.write(df_rec["average_reviewer_score"][4]+" :star:")
            st.write("Brand: "+df_rec["brand"][4])
            st.write("Price: "+df_rec["price"][4])
            st.image(df_rec['imageURLHighRes'][4])
            
            