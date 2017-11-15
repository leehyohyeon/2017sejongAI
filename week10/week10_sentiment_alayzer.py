from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy

def extract_features(words):
    return dict([(word, True) for word in words])

if __name__=='__main__':
    #말뭉치에서 리뷰를 로딩
    fileids_pos = movie_reviews.fileids('pos')
    fileids_neg = movie_reviews.fileids('neg')

features_pos = [(extract_features(movie_reviews.words(
fileids=[f])), 'Positive') for f in fileids_pos]
features_neg = [(extract_features(movie_reviews.words(
fileids=[f])), 'Negative') for f in fileids_neg]

threshold = 0.8
num_pos = int(threshold * len(features_pos))
num_neg = int(threshold * len(features_neg))

features_train = features_pos[:num_pos] + features_neg[:num_neg]
features_test = features_pos[num_pos:] + features_neg[num_neg:]

print('\nNumber of training datapoints:', len(features_train))
print('Number of test datapoints:', len(features_test))

classifier = NaiveBayesClassifier.train(features_train)
print('\nAccuracy of the classifier:', nltk_accuracy(
classifier, features_test))

N = 15
print('\nTop ' + str(N) + ' most informative words:')
for i, item in enumerate(classifier.most_informative_features()):
    print(str(i+1) + '. ' + item[0])
    if i == N - 1:
            break

input_reviews = [
"This is my first review on the IMDb website and i have been a member for more that 9 years now, that's who much i loved this movie. It just give you that positive thoughts and energy within a lovely comedian scenario.I loved how they mix between the classic culture with the modern one. It was very interesting to watch how they remind our generation about the habits which they are missing from the classic one.De Niro and Anne Hathaway have excellent work chemistry. Director and camera teams made a great job too... Team work, thank you for this lovely movie",
"The Intern .... The sweetest, most perfect And heart touching I have seen in a long time. Of course it helps that Robert De Niro is there but what a movie! This is what all movies should be.Robert De Niro plays the perfect gentleman, the kind we don't see anymore. And every woman who sees the movie will fall a bit in love with him. Anne Hathaway perfectly plays the role of a successful entrepreneur, a working wife and mom who thinks about everything and everyone and still feels guilty about being a working woman, even after the perfect gentleman tells her He should not be the feminist amongst the two of them. Every working woman will identify with her inner struggles. The story is perfect, with the perfect practical ending, as life is always more practical than idealistic.",
"Wonderful contemporary story, great acting. What more can one ask for? DeNiro totally inhabits the role of a bored NewYorker retiree who quietly, commandingly changes everyone around him for the better. There were little bits of sentimental predictability but not many.",
"Sometimes you don't need a film to try and change the world, make bold political or societal statements or even be shocking. Sometimes it's good enough to be an audience member who can just sit back, relax and enjoy the show… and smile. That's the kind of movie you get when you sit down to enjoy 'The Intern'."
]

print("\nMovie review predictions:")
for review in input_reviews:
    print("\nReview:", review)
    probabilities = classifier.prob_classify(extract_features(review.split()))
    predicted_sentiment = probabilities.max()
    print("Predicted sentiment:", predicted_sentiment)
    print("Probability:", round(probabilities.prob(predicted_sentiment), 2))

