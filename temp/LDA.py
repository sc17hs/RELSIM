# coding: utf-8

#import sys
#try:
#    reload(sys)
#    sys.setdefaultencoding("utf-8")
#except:
#    print('python3')
    
import nltk
#try:
#    from nltk.corpus import stopwords
#    from nltk.stem import wordnet
#    print 'stopword & wordnet data downloaded already'
#except:
print ('downloading nltk data')
nltk.download("stopwords")
nltk.download("wordnet")

    
# coding: utf-8




import sys
try:
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    print('python3')
    
import warnings
warnings.filterwarnings("ignore")
    
    
    
import pandas as pd
from time import time, ctime

from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
from gensim.models.phrases import Phraser, Phrases

stopwords = set(stopwords.words('english'))
punctuation = set(string.punctuation) 
lemmatize = WordNetLemmatizer()

from collections import defaultdict


import gensim
from gensim import corpora

import pyLDAvis.gensim

from time import time
import logging
import os

stop = set(['a', 'about', 'above', 'across', 'after', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'among', 'an', 'and', 'another', 'any', 'anybody', 'anyone', 'anything', 'anywhere', 'are', 'area', 'areas', 'around', 'as', 'ask', 'asked', 'asking', 'asks', 'at', 'away', 'b', 'back', 'backed', 'backing', 'backs', 'be', 'became', 'because', 'become', 'becomes', 'been', 'before', 'began', 'behind', 'being', 'beings', 'best', 'better', 'between', 'big', 'both', 'but', 'by', 'c', 'came', 'can', 'case', 'cases', 'certain', 'certainly', 'clear', 'clearly', 'come', 'could', 'd', 'did', 'differ', 'different', 'differently', 'do', 'does', 'done', 'down', 'downed', 'downing', 'downs', 'during', 'e', 'each', 'early', 'either', 'end', 'ended', 'ending', 'ends', 'enough', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'f', 'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'find', 'finds', 'first', 'for', 'four', 'from', 'full', 'fully', 'further', 'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally', 'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got', 'great', 'greater', 'greatest', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'herself', 'high', 'higher', 'highest', 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'important', 'in', 'interest', 'interested', 'interesting', 'interests', 'into', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kind', 'knew', 'know', 'known', 'knows', 'l', 'large', 'largely', 'last', 'later', 'latest', 'least', 'less', 'let', 'lets', 'like', 'likely', 'long', 'longer', 'longest', 'm', 'made', 'make', 'making', 'man', 'many', 'may', 'me', 'member', 'members', 'men', 'might', 'more', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'my', 'myself', 'n', 'necessary', 'need', 'needed', 'needing', 'needs', 'never', 'new', 'newer', 'newest', 'next', 'noone', 'now', 'nowhere', 'number', 'numbers', 'o', 'of', 'off', 'often', 'old', 'older', 'oldest', 'on', 'once', 'one', 'only', 'open', 'opened', 'opening', 'opens', 'or', 'order', 'ordered', 'ordering', 'orders', 'other', 'others', 'our', 'out', 'over', 'p', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 'place', 'places', 'point', 'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting', 'presents', 'problem', 'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather', 'really', 'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say', 'says', 'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 'sees', 'several', 'shall', 'she', 'should', 'show', 'showed', 'showing', 'shows', 'side', 'sides', 'since', 'small', 'smaller', 'smallest', 'so', 'some', 'somebody', 'someone', 'something', 'somewhere', 'state', 'states', 'still', 'such', 'sure', 't', 'take', 'taken', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'things', 'think', 'thinks', 'this', 'those', 'though', 'thought', 'thoughts', 'three', 'through', 'thus', 'to', 'today', 'together', 'too', 'took', 'toward', 'turn', 'turned', 'turning', 'turns', 'two', 'u', 'under', 'until', 'up', 'upon', 'us', 'use', 'used', 'uses', 'v', 'very', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', 'way', 'ways', 'we', 'well', 'wells', 'went', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'whole', 'whose', 'why', 'will', 'with', 'within', 'without', 'work', 'worked', 'working', 'works', 'would', 'x', 'y', 'year', 'years', 'yet', 'you', 'young', 'younger', 'youngest', 'your', 'yours', 'z', '#', 'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'could', 'did', 'do', 'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have', 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'she', "she'd", "she'll", "she's", 'should', 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', "we'd", "we'll", "we're", "we've", 'were', 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves'])



class PipelineLDA(object):
    
    """
    input a csv/txt file with one colume (optional column name: 'text')
    every row of that csv should be one document   
    
    """
    
    def __init__(self, path, topics, grams, passes=1):
        
        global logging
        try:
            os.mkdir('model')
        except:
            print ('model dir exists')
            
        self.passes=passes
        self.folder = './model/'
        self.path = path
        self.topics = topics
        self.grams = grams
        self.name = self.path.split('.')[-2].split('/')[-1]+'_topics_'+str(self.topics)+'_{}_gram'.format(self.grams)
        self.df =  pd.read_csv(self.path, engine='python')
        print (self.df.shape)
        try:
            self.series = self.df['text']
        except:
            self.series = self.df.iloc[:,0:1]
            
        self.stop = stopwords
        self.stop.update(stop)
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO,
                            filename=self.folder+self.name+'_log.log'.format(self.name),filemode='w')
            
    def addstop(self, wordlist):
        self.stop.update(set(wordlist))


        
        
    def clean(self, article):
        
        try:
            article = str(article).decode('unicode_escape').encode('utf-8')
        except:
            article = str(article)

        zero = "".join(i for i in article if i not in punctuation)

        one = " ".join([i for i in zero.lower().split() if i not in stopwords])

        try:
            three = " ".join(lemmatize.lemmatize(i) for i in one.split())
        except:
            three = " ".join(lemmatize.lemmatize(i.decode('unicode_escape').encode('utf-8')) for i in one.split())
        return three
    
    def split(self):
        start = time()
        n_gram = self.grams

        ap_text = self.series.apply(self.clean)
        ap_text_list = [i.split() for i in ap_text]
        print (len(ap_text_list))

        print ('used: {:.2f}s'.format(time()-start))
        if n_gram==1:
            self.prepared=ap_text_list
            
        elif n_gram==2:
            phs = Phrases(ap_text_list)
            bi_gram = Phraser(phs)
            new_bi_list = [bi_gram[i] for i in ap_text_list]
            self.prepared = new_bi_list

        else:
            phs = Phrases(ap_text_list)
            bi_gram = Phraser(phs)
            new_bi_list = [bi_gram[i] for i in ap_text_list]
                        
            
            phs3=Phrases(new_bi_list)
            tri_gram=Phraser(phs3)
            new_tri_list2 = [tri_gram[i] for i in new_bi_list]

            self.prepared=new_tri_list2


            
    def create_dictionary(self):
        # Creating the term dictionary of our courpus, where every unique term is assigned an index. dictionary = corpora.Dictionary(doc_clean)
        start = time()
        self.dictionary = corpora.Dictionary(self.prepared)
        self.dictionary.save(self.folder+self.name+'_dict.dict')
        print (len(self.dictionary))
        print ('used: {:.2f}s'.format(time()-start))

        
    def create_corpus(self):
        # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
        start = time()
        self.doc_term_matrix = [self.dictionary.doc2bow(doc) for doc in self.prepared]
        corpora.MmCorpus.serialize(self.folder+self.name+'_corpus.mm', self.doc_term_matrix)
        print (len(self.doc_term_matrix))
        #print (doc_term_matrix[100])        
        print ('used: {:.2f}s'.format(time()-start))
        
    def train(self):
        num_topics = self.topics
        
        start = time()
        # Creating the object for LDA model using gensim library
        Lda = gensim.models.ldamodel.LdaModel

        # Running and Trainign LDA model on the document term matrix.
        self.ldamodel = Lda(self.doc_term_matrix, num_topics=num_topics, id2word = self.dictionary, 
                        passes=self.passes
                      )
        
        print ('used: {:.2f}s'.format(time()-start))        
        
    def save(self):
        start = time()
        self.ldamodel.save(self.folder+self.name+'_lda.model')
        print ('used: {:.2f}s'.format(time()-start))
        
    def load(self, path):
        start = time()
        loading = gensim.models.ldamodel.load(path)
        self.ldamodel=loading
        print ('used: {:.2f}s'.format(time()-start))
        
    def visualize(self):
        import pyLDAvis
        try:
            pyLDAvis.enable_notebook()
        except:
            print ('not in jupyter notebook')
            
        start = time()

        self.viz = pyLDAvis.gensim.prepare(self.ldamodel, self.doc_term_matrix, self.dictionary)

        print ('used: {:.2f}s'.format(time()-start))
        print ('saving viz to '+self.name+'_viz.html')
        
        pyLDAvis.save_html(self.viz, self.name+'_viz.html')
        
        return self.viz

        
        
        

        
        
    def __repr__(self):
        return "name: "+ str(self.name)+ " doc numbers: "+ str(self.df.shape[0])
        

def LDA_main(x):
    try:
        path
        flag=0
    except:
        flag=1
    if flag:
        path = 'quran2.csv'
        topics = 30
        n_gram = 1
    else:
        print ('use variable exists ---:)')
    starter = time()
    
    print ('1/7: load file')
    lda = PipelineLDA(path, topics, n_gram)
    print (lda)
    print ('2/7: preprocessing docs')
    lda.split()
    print ('3/7: create doc dictionary')
    lda.create_dictionary()
    print ('4/7: create doc corpus')
    lda.create_corpus()
    print ('5/7: train LDA model')
    lda.train()
    print ('6/7: save trained LDA model')
    lda.save()
    print ('7/7: visualize LDA model result')
    print ('making Viz')
    lda.visualize()
    print ('done')
    ender = time()-starter
    print ('total used: {:.2f}s, {:.2f}mins'.format(ender, ender/60))


def main(x):
    print ('executing...')
    LDA_main(x)

main(1)
