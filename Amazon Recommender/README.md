# Amazon Beauty Products Recommendation System

## Introduction


Amazon is an American multinational technology company focusing on e-commerce, cloud computing, online advertising, digital streaming, and artificial intelligence. In 2020, Amazon captured 32 percent of all beauty and skin care bought online, with $23 billion in total sales.

The Covid-19 pandemic has boosted the sale online purchases in general globally, with consumers found themselves spending their time in quarrantine.

Some stats taken from: https://www.powerreviews.com/insights/2021-beauty-industry-consumer-report/
87% of people say they spend more or the same online than before Covid
49% say they now spend more than $50 online on beauty products; compared to 16% in the previous year (2019)
57% of shoppers say that they had never tried more of a quarter of the beauty products they bought online in 2020 (i.e. they were first time purchases)
41% say they rely on reviews more than they did pre-Covid
76% focusing on buying products that are sustainably made
54% (more than half) of consumers indicate they wear less makeup now than pre-COVID

The Covid-19 pandemic has boosted the sale online purchases in general globally, with consumers found themselves spending their time in quarrantine.

Some stats taken from: https://www.powerreviews.com/insights/2021-beauty-industry-consumer-report/
- 87% of people say they spend more or the same online than before Covid
- 49% say they now spend more than $50 online on beauty products; compared to 16% in the previous year (2019)
- 57% of shoppers say that they had never tried more of a quarter of the beauty products they bought online in 2020 (i.e. they were first time purchases)
- 41% say they rely on reviews more than they did pre-Covid
- 76% focusing on buying products that are sustainably made
- 54% (more than half) of consumers indicate they wear less makeup now than pre-COVID


One pattern was observed that, during Covid, more than half of the consumers claimed that they wore less makeup, yet beauty product sales has soared. On the other hand, survey suggest that the consumers do care about products that are sustainably made, yet on a personal level, consumers are buying in excess

## Problem Statement

Consumers are concerned about beauty products manufactured and the impact it does to the environment, yet they are indulging in buying new products that are pushed to them via attractive sales or word of mouths recommendations from influencers.


This project aims to address a consumer's desire to create less waste from beauty products by encourageing them to purchase more sensibly via a recommendation system that contains reviews and scores of a product that were gathered from an Amazon user's raw inputs.

**This project aims to address a consumer's desire to create less waste from beauty products by encourageing them to purchase more sensibly via a content based recommendation system that contains reviews and scores of a product that were gathered from an Amazon user's raw inputs.**


## Dataset

Amazon Product Dataset: http://jmcauley.ucsd.edu/data/amazon/


## EDA, Pre-processing


## TF-IDF + Cosine Similarity Baseline model


<img src="attachment:198e6485-31e0-4508-af05-ea0f91ff90b3.png" width="320">

## Word2vec + Cosine Similarity model

#### Word Embeddings with t-SNE

<img src="attachment:a8b26efc-2f00-4542-8d9c-8a12c683198c.png" width="600">

=======
## TF-IDF + Cosine Similarity Baseline model
The baseline recommendation system model was built with Bag-Of-Words **TF-IDF** and combined with cosine simlarity.

<img width="699" alt="image" src="https://media.git.generalassemb.ly/user/43940/files/b1b0a79c-51d7-4362-9272-85f7be61dc48">

A recommendation can be obtained based on user inputs with cosine similarity. It is used to measure the similarity between two vectors. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space like in the picture above. The cosine similarity captures the angle of the word vectors and not the magnitude.

## Word2vec + Cosine Similarity model
<img width="725" alt="image" src="https://media.git.generalassemb.ly/user/43940/files/9a4f821f-1107-4be1-9e96-c1f417e09c38">
This diagram depicts what goes under the hood when a corpus is trained with the Word2vec architecture.

Word2vec creates word embeddings to capture the contextual meaning of the words in a document. Word2vec is a simple neural network model with 1 hidden layer, in this case we are not interested in the inputs and outputs of this network, rather the goal is actually just to learn the weights of the hidden layer that are actually the “word vectors” that we’re trying to learn.

Combined Word2vec with cosine similarity, we are able to complete a more robust recommendation system that will recommend items that are more relevant to the user. 

## Word Embeddings with t-SNE

<img width="1083" alt="image" src="https://media.git.generalassemb.ly/user/43940/files/b8e0cbdf-c8a8-484e-a478-337c64cc09d4">
A visualization of word embeddings is plotted with t-SNE. For this model, it is trained on 300 dimensions, however humans are unable to visualise anything beyong 3 dimensions. t-SNE is used to squash this down to 2D or 3D for ease of visualisation. This example shows the location of the top 10 similar words to "perfume" and "mask".

## End Product Deployment
<img width="1423" alt="image" src="https://user-images.githubusercontent.com/106056323/217907810-139f9e5d-569a-47e3-8224-4a5228e6fcfb.png">

