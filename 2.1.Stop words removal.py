from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
example = "A bird on the tree saw me and flew away."
  
stop_words = set(stopwords.words('english')) 
  
word = word_tokenize(example) 
  
filtered_sentence = [w for w in word if not w in stop_words] 
  
filtered_sentence = [] 
  
for w in word: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
  
print(word) 
print(filtered_sentence) 
