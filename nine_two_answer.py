#numwords will represent the number of words
numwords = 0

#has_no_e is a function that looks at a word and says "true" if it does not have an e
def has_no_e(word):
        result = False
        if ("e" not in word):
            result = True
        return(result)

file1 = open("words.txt", 'r')

#linelist is the contents of the file with one line per list item
linelist = file1.readlines()
linelist_without_e = []

#this prints entire list (all words)
print("total number of words: ", len(linelist))
#this searches the list with the has_no_e function
for word in linelist:
          if(has_no_e(word)):
#everytime word without e found in search, this adds one to numwords and adds words without e into linelist_without_e
              numwords += 1
              linelist_without_e.append(word)
#outputs finalnumber
print("total number of words that do not contain e: ", numwords)
percent = (numwords/len(linelist))*100.0
print("percentage of words that do not contain e: ",  str(round(percent,4)),"%")
print("list of all words without e in file")
print ("=====")
print(linelist_without_e)
