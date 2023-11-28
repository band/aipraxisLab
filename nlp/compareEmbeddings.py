#!/usr/bin/env python
"""
compare embeddings of two sentences
pre-requisites:

pip install gensim
pip install scikit-learn

"""

# import libraries
import gensim
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# load word2vec word vector model
model_path = './word2vec/GoogleNews-vectors-negative300.bin'
model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)

# your inputs
first_sentence_list = ['driver', 'backs', 'into', 'stroller', 'with', 'child', ',', 'drives', 'off']
second_sentence_list = ['driver', 'backs', 'into', 'mom', ',', 'stroller', 'with', 'child', 'then', 'drives', 'off']

# remove out-of-vocabulary words
first = [word for word in first_sentence_list if word in model.key_to_index]
second = [word for word in second_sentence_list if word in model.key_to_index]

# average word embeddings to get sentence embeddings
first_sent_embedding = np.mean(model[first], axis=0)
second_sent_embedding = np.mean(model[second], axis=0)

# calculate similarities
result = cosine_similarity(first_sent_embedding.reshape(1,-1),second_sent_embedding.reshape(1,-1))

print(result)
