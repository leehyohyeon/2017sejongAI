from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer
 
 
 
input_text = "Do you know how tokenization works? Since it's my first time to study tokenization it's sometimes hard to understand but actually really awesome! Lets analyze a couple of sentences and figure it out." 
 
 
 
print("\nSentence Tokenizer:")
 
print(sent_tokenize(input_text))
 
 
 
print("\nWord tokenizer : ")
 
print(word_tokenize(input_text))
 
 
 
print("\nWord Punct Tokenizer : ")
 
print(WordPunctTokenizer().tokenize(input_text)) 
