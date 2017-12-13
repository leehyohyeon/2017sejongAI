import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import brown
from text_chunker import chunker
#브라운 말뭉치에서 데이터읽기
input_data = ' '.join(brown.words()[:5400])
# 단어 묶음에 포함될 단어수
chunk_size = 800
#텍스트를 단어 묶음으로 나눔
text_chunks = chunker(input_data, chunk_size)
# 사전 구조체로 변경
chunks = []
for count, chunk in enumerate(text_chunks):
    d = {'index': count, 'text': chunk}
    chunks.append(d)

count_vectorizer = CountVectorizer(min_df=7, max_df=20)
document_term_matrix = count_vectorizer.fit_transform([chunk['text'] for chunk in chunks])
# 어휘 목록 추출 후 화면에 출력
vocabulary = np.array(count_vectorizer.get_feature_names())
print("\nVocabulary:\n", vocabulary)
# 단어 묶음별 이름 붙이기
chunk_names = []
for i in range(len(text_chunks)):
    chunk_names.append('Chunk-' + str(i+1))
print("\nDocument term matrix:")
formatted_text = '{:>12}' * (len(chunk_names) + 1)
print('\n', formatted_text.format('Word', *chunk_names), '\n')
for word, item in zip(vocabulary, document_term_matrix.T):
    output = [word] + [str(freq) for freq in item.data]
    print(formatted_text.format(*output))



