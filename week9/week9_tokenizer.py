from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer 
  
input_text = "These days many makeup artists are less likely to talk about hiding a woman’s age and wrinkles than about playing up her individual gifts. “For me to get a great result on an older woman, age is not what I see,” said David De Leon, a makeup artist who often works with Jane Fonda. “I look for her potential.”But finding the makeup that makes that woman look and feel great can be tricky. Application techniques that worked for years start to fail as one’s skin changes. Longtime favorites begin to detract, not enhance. Mature skin is typically drier, and those mattifying, pore-shrinking products don’t deliver like their hydrating and illuminating counterparts."  
  
print("\nSentence Tokenizer:") 
print(sent_tokenize(input_text)) 
  
print("\nWord tokenizer : ")  
print(word_tokenize(input_text)) 
   
print("\nWord Punct Tokenizer : ") 
print(WordPunctTokenizer().tokenize(input_text))  
