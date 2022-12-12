#numwords will represent the number of words that are more than 20
numwords = 0

#file1 is the original file
file1 = open("words.txt", 'r')

#linelist is the contents of the file with one line per list item
linelist = file1.readlines()

#this prints entire list (all words)
print("total number of words: ", len(linelist))
#this search counts words longer than 20 characters in the list
for word in linelist:
          if (len(word)>20):
#everytime something found in search, this adds one to numwords
              numwords += 1
#outputs finalnumber
print("total number of words with length greater than 20: ", numwords)
