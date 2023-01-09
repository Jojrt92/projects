# Project 3: Web APIs & NLP

### Introduction

Starbucks and Dunkin Donuts are the two most recognized brands in the United States' coffee chain industry. Both comapnies offer similar coffee options and similar overall strategies. Nonetheless, there are key differences in the ways both businesses operates.

Despite being founded 20 years after Dunkin Donuts, Starbucks have grew beyond their competitors and is currently a substantially larger company. Generating over 23.5 billion in 2020 while Dunkin's revenue only stood at $1.3 billion.

### Problem Statement

Upper management in Starbucks has noticed that the starbucks subreddit generates over 90 post and 600 comments a day. The number of subsribers has also increased exponentially especailly in the past 4 years.

They have then engaged the data science team to explore the possibility of extracting value from the starbucks subreddit. The team has decided to compare the content on starbucks subreddit to our competitor DunkinDonuts. As Halloween is just a month away, both Starbucks and DunkinDonuts have launched new products to celebrate this holiday.

Objective
We aim to discover if the new products are actually getting any buzz through reddit
To discover if it is of any value to Starbucks if reddit is a good source to validate our products in the future

---

### Executive Summary
Methodology

1) External research on the brands regarding this project (ie. Starbucks and Dunkin donuts)
2) Explore options for a compelling problem statement which can be solved by a machine learning classification model
3) Webscrape a substantial amount of post from reddit
4) Perform EDA and observe what insights can be gathered before preprocessing
5) Perform preprocessing and input data into a classification model

---

### Conclusion and recommendations
This section is for future work to improve on the current model. The logistic model is great for binary classification and relatively inexpensive to compute results, however this current model is overfitted. For future work, these points can be considered

- Use PDA to reduce the features
- XGBoost to improve the model performance on random forest (although this is computationally expensive and will take longer computing time)
- Collecting data on different seasons and put them through the same models for test because the logistic regression model might not be the best performer throughout the seasons
- Sentiment Analysis should also be performed on the top words to determine if these keywords could potentially lead to an improvement of customer's experience.

We embarked on this project to aim to solve achieve 2 objectives.

To discover if the new products are actually getting any buzz through reddit
To discover if it is of any value to Starbucks if reddit is a good source to validate our products in the future
The new products indeed created buzz, by being among the top keywords appearing before preprocessing. It is also worth noting that reddit can be a platform to validate the response of starbucks new products in the future as the comments and sentiments derive from them are very raw and authentic.

The top 10 words that strongly classify a post belonging to starbucks are

- barista
- partner
- frappuccino
- grand
- art
- transfer
- shaken
- flat
- siren
- store
None of which includes our festive drinks (pumpkin spice) A good guess will be that the new products are no longer unique to starbucks and their competitors have already released similar products for this holiday. In the future, new products can likewise be validated in the same way. Starbucks can validate future new products that are unique to their competitors by harvesting the data among the text in reddit and check if the list of new keywords contains any words that are related to the new products.

---


