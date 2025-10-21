# Frequency of words in book
stopwords = ['o','i', '', ' ','a','the', 'of', 'and', 'to', 'in', 'you', 'it', 'with', 'that', 'or', 'was', 'he', 'is',
             'for', 'this', 'his', 'as', 'not', 'at', 'by', 'all', 'they', 'but', 'be', 'on', 'from',
             'had', 'her', 'work', 'are', 'any', 'she', 'if', 'said', 'so', 'which', 'have', 'do', 'we',
             'no', 'my', 'were', 'them', 'their', 'him', 'one', 'will', 'me', 'there', 'who', 'up',
             'other', 'an', 'its', 'when', 'what', 'can', 'may', 'into', 'out', 'must', 'your',
             'then', 'would', 'could', 'more', 'now', 'has', 'like', 'down', 'where', 'been',
             'through', 'did', 'away', 'these', 'such', 'set', 'back', 'some', 'than', 'way',
             'made', 'our', 'after', 'well', 'should', 'get', 'even', 'am', 'go', 'saw',
             'just', 'put', 'while', 'ever', 'off', 'here', 'also']

# Initializes lists for use
sentenceList = []
punctuationList = [",",".","?",";",":","!",'"',"'"]
print("Start")
currFile = r"python\\biblesearch\\Jude.txt"

# Open a file and reads the text into a list
Bfile = open(currFile, "r")
wordList = []
finalList = []
countDict = {}
for line in Bfile:
    tLine = line.split(" ")
    sentenceList.append(tLine)
Bfile.close()
totalValue = 0
for sentence in sentenceList:
    for word in sentence:
        wordList.append(word.strip().lower())
        if word != '' and word.isalpha() == True:
            totalValue = totalValue + 1
print("Computing frequency...")

# Computes the frequency of words
for word1 in wordList:
    count = 0
    for word2 in wordList:
        if word1 == word2:
            count += 1
    countDict[word1] = count

print("Words with greatest frequency...")

# Displays the words with the greatest frequency
frequencyList = []
maxValue = 0
maxKey = ""
for currKey,currValue in countDict.items():
    if currKey not in stopwords and currKey.isalpha() is True and currValue > maxValue:
        maxValue = currValue
        maxKey = currKey
print(maxKey, maxValue)
print("Computation complete")
result = sorted(countDict.items(), key = lambda x:x[1], reverse = True)
totalValue = 0
for tupleVal in result:
    if tupleVal[0].isalpha() is True and tupleVal[0] not in stopwords:
        frequencyList.append(tupleVal)
        totalValue = totalValue + tupleVal[1]
print("Number of words in book: ", totalValue)
