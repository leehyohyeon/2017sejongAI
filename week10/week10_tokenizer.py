from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer 
 
input_text = "Now in its 91st year, the Macy’s Thanksgiving Day Parade is a quintessential American  holiday staple. This year’s lineup of balloons includes Pikachu, SpongeBob SquarePants and several trolls (from the movie of the same name).  If you’re in New York, the parade begins at 9 a.m. E.S.T. on the Upper West Side and finishes near Herald Square, home to the world’s largest Macy’s store. If you’re looking for something a bit less traditional, consider riding off Thursday’s meal with the Pilgrim Pedal Ride on Friday, Nov. 24, a family-friendly biking excursion that weaves through Brooklyn and Queens. The event, which begin at East 23rd Street and the East River, includes a “sit-down social” breakfast at a Brooklyn diner midway through the ride."

print("\nSentence Tokenizer:") 
print(sent_tokenize(input_text)) 
   
print("\nWord tokenizer : ")  
print(word_tokenize(input_text)) 
  
print("\nWord Punct Tokenizer : ") 
print(WordPunctTokenizer().tokenize(input_text))  
