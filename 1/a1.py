# Q1.1
# ------------------
# Write your implementation here.
words_list = [y for x in corpus for y in x]
unsorted_corpus_words = set(words_list)
corpus_words = sorted(list(unsorted_corpus_words))
num_corpus_words = len(corpus_words)
# ------------------

# Q1.2
# ------------------
# Write your implementation here.
M = np.zeros((num_words, num_words))
    word2ind = {w: index for index, w in enumerate(words)}
    
    for doc in corpus:
        word_indexes = [word2ind[word] for word in doc]
        for counter, center_word_index in enumerate(word_indexes):
            left = max(counter - window_size, 0)
            right = min(counter + window_size + 1, len(doc))
            window_indexes = word_indexes[left:right]

            M[center_word_index, window_indexes] += 1
            M[center_word_index, center_word_index] -= 1 
# ------------------

# Q1.3
# ------------------
# Write your implementation here.
svd = TruncatedSVD(n_components=k, n_iter=n_iters)
M_reduced = svd.fit_transform(M)
# ------------------

# Q1.4
# ------------------
# Write your implementation here.
for word in words:
    index = word2ind[word]
    directions = M_reduced[index]
    x = directions[0]
    y = directions[1]
    plt.scatter(x, y, marker='x', color='red')
    plt.text(x, y, word, fontsize=9)
# ------------------

# Q1.5-Explanation
#  <your explanation in English or Farsi>
clusters :
    
    1- petroleum
    
    2- industry
       energy

    3- oil
    
    4- ecuador
       kuwait
    
    5- irag
    
    6- output
       barrels
    
    7- bpd
    

I've expect that oil and petroleum must have located near by each other but the model located them far from each other.
I thing the performance of this co-ocurrence matrix method isn't doing well. also bpd and barrels must locate near by each other but they too far.
# ------------------

# Q2.1-Explanation
#  <your explanation in English or Farsi>
clusters:
    
    1- industry
    
    2- ecuador
       irag
       petroleum
    
    3- oil
    
    4- kuwait
    
    5- output
    
    6- barrels
    
    7- bpd
    
petroleum must not have been with ecuador and petroleum. and  kuwait and oil is not been with related words.
    like:
    
        oil - petroleum
        kuwait - irag - ecuador
    
The clustering phenomemon is much less obvious here.
    
reduding dimensions may cause the fault of this event.
# ------------------


# Q2.2
# ------------------
# Write your implementation here.
wv_from_bin.most_similar("bank") 
# ------------------

# Q2.2-Explanation
#  <your explanation in English or Farsi>
The main reason is corpus. beacuse word2vec was trained in special way and the existing meaning of words is in special field. so the model returned the high probablity of meaning of words
# ------------------

# Q2.3
# ------------------
# Write your implementation here.
num1 = wv_from_bin.distance("beautiful", "handsome")
num2 = wv_from_bin.distance("beautiful", "ugly")
print(num1)
print(num2)
# ------------------

# Q2.3-Explanation
#  <your explanation in English or Farsi>
It's all about varoius dimestions of a word in space. beautiful and ulgy might be opposite but they're describing the mood of a person.
but beautiful and handsome might not be descring mood. in another vision beautiful and handsome might describe appearance of that person.
# ------------------

# Q2.4-Explanation
#  <your explanation in English or Farsi>
x = m-w+k
# ------------------

# Q2.5
# ------------------
# Write your implementation here.
the second case works as well as possible. because the model can find chine to chinese is like american to america.
but the first case don't work probebly. because only terrific can be the answer of this situations and other words can not be used in this part.
# ------------------

# Q2.5-Explanation
#  <your explanation in English or Farsi>
pprint.pprint(wv_from_bin.most_similar(positive=['fantastic', 'good'], negative=['bad']))
pprint.pprint(wv_from_bin.most_similar(positive=['chinese', 'america'], negative=['china']))
# ------------------

# Q2.6
# ------------------
# Write your implementation here.
pprint.pprint(wv_from_bin.most_similar(positive=['soil', 'food'], negative=['plant']))
# ------------------

# Q2.6-Explanation
#  <your explanation in English or Farsi>
expectaion of the answer is that soil for planet is like food for human but the result was wrong and related to foods.
# ------------------

# Q2.7-Explanation
#  <your explanation in English or Farsi>
Most similiar word to worker for men is employee and most similiar word to worker in woman is workers.
the first case refered to words that have family meaning like mother, child, pregnant and so on
but second case refered to words that have working meaning and activities.
so first case added distance to worker vector in family dimension and second case added it to vector in work vector.
# ------------------

# Q2.8
# ------------------
# Write your implementation here.
pprint.pprint(wv_from_bin.most_similar(positive=['man', 'waiter'], negative=['woman']))
print()
pprint.pprint(wv_from_bin.most_similar(positive=['king', 'president'], negative=['queen']))
# ------------------

# Q2.8-Explanation
#  <your explanation in English or Farsi>
in first case we expect that waiters have the most possibility but the answer is bartender that do not mean sexuality in it.
in second case also have some problem. vice means helper to president and do not use for woman's presindent.
# ------------------

# Q2.9-Explanation
#  <your explanation in English or Farsi>
we can compute bias from subtracing the distance of two word from each other. this can help us to find synonyms of a word.
by adding the distance of two in a dimension to another dimension of a word we can find synonyms.
by another vision bias in word prediction is the thing that can help us to find the word related to context.
# ------------------



