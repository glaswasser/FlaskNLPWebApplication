import pandas as pd
from bertopic import BERTopic

f = "/Users/alexanderheinz/github/privat/topic modelling/labeled-german-tables/bra_tee_labeled.xlsx"
comments = pd.read_excel(f)
## INSERT TOPIC MODELLING HERE
comments.loc[comments.text.isnull(), "text"] = " " # replace nan with empty string
## RUN BERTOPIC
docs = comments.text
topic_model = BERTopic(language = "multilingual", verbose = True, calculate_probabilities = True) # arguments: min_topic_size, nr_topics = "auto", 

topics, probabilities = topic_model.fit_transform(docs)

topic_model.visualize_topics()