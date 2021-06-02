import wikipedia, time, string, random
import numpy as np
import matplotlib.pyplot as plt

#####Loading hello world page
search = wikipedia.search("Hello World")
page = wikipedia.wikipedia.page(search[0])
print (page.summary)

####FREQUENCY ANALYSIS
Search = wikipedia.search("Oxford")
Page = wikipedia.wikipedia.page(Search[0])
Text = Page.content
FEL=[8.16,1.49,2.78,4.25,12.70,2.23,2.02,6.09,6.97,0.15,0.77,4.02,2.40,
 6.74,7.50,1.92,0.09,5.98,6.32,9.05,2.75,0.97,2.36,0.15,1.97,0.07]

relFreq = dict.fromkeys(string.ascii_uppercase, 0)

no_letters=0
for letter in relFreq.keys():
    LetterN = Text.upper().count(letter)                ####### COUNTS AMOUNT OF EACH LETTER 
    relFreq[letter] = LetterN
    no_letters = no_letters + LetterN
realFreqText = 100*np.array(list(relFreq.values()))/no_letters

######PLOTS CHART COMPARING 2 SETS FO VALUES
plt.bar(np.arange(26)-0.25,FEL,width=0.3,label='E.L. Freq.')
plt.bar(np.arange(26)+0.25,realFreqText,width=0.3,label='\'Oxford\'')
plt.xticks(np.arange(26),labels=relFreq.keys())
plt.ylabel('Relative Frequency, \%'); plt.legend()
plt.show()

####### CREATING WORDCLOUD OF CONTENT FROM PAGE
from wordcloud import WordCloud
from random import random
wordcloud = WordCloud().generate(Text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.show()
