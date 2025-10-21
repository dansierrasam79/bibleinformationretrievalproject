# Text parsing
def findWord(allbooks):
    sentence = ""
    finalSearchResults = []
    searchWord = input("Enter three or more keywords separated by a space: ").split(" ")
    verseResult = ""
    finalList = []
    # Read books text into memory
    for Bbook in allbooks:
        Bfile = open(Bbook, "r")
        wordList = []
        for line in Bfile:
            tLine = line.split(" ")
            finalList.append(tLine)
        Bfile.close()
    # Searching for words in verse
    for sentence in finalList:
        searchResults = []
        for eachWord in searchWord:
            if eachWord.lower() in sentence[0:len(sentence)]:
                if sentence[0][0] == "1" or sentence[0][0] == "2" or sentence[0][0] == "3":
                    verseResult = sentence[0][0] + " " + sentence[0][1:len(sentence)].capitalize() + " " + sentence[1] + ":" + sentence[2]
                    if int(sentence[1]) < 10:
                       verseResult = sentence[0][0] + " " + sentence[0][1:len(sentence)].capitalize() + " " + sentence[1][1] + ":" + sentence[2]
                    if int(sentence[2]) < 10:
                        verseResult = sentence[0][0] + " " + sentence[0][1:len(sentence)].capitalize() + " " + sentence[1] + ":" + sentence[2][1]
                    if int(sentence[1]) < 10 and int(sentence[2]) < 10:
                        verseResult = sentence[0][0] + " " + sentence[0][1:len(sentence)].capitalize() + " " + sentence[1][1] + ":" + sentence[2][1]
                else:
                    verseResult = sentence[0].capitalize() + " " + sentence[1] + ":" + sentence[2]
                    if int(sentence[1]) < 10:
                       verseResult = sentence[0].capitalize() + " " + sentence[1][1] + ":" + sentence[2]
                    if int(sentence[2]) < 10:
                        verseResult = sentence[0].capitalize() + " " + sentence[1] + ":" + sentence[2][1]
                    if int(sentence[1]) < 10 and int(sentence[2]) < 10:
                        verseResult = sentence[0].capitalize() + " " + sentence[1][1] + ":" + sentence[2][1]
                    if sentence[0] == "songofsolomon":
                        verseResult = sentence[0][0:4].capitalize()+ " " + sentence[0][4:6] + " " + sentence[0][6:13].capitalize() + " " + sentence[1] + ":" +sentence[2]
                        if int(sentence[1]) < 10:
                            verseResult = sentence[0][0:4].capitalize()+ " " + sentence[0][4:6] + " " + sentence[0][6:13].capitalize() + " " + sentence[1][1] + ":" + sentence[2]
                        if int(sentence[2]) < 10:
                            verseResult = sentence[0][0:4].capitalize()+ " " + sentence[0][4:6] + " " + sentence[0][6:13].capitalize() + " " + sentence[1] + ":" + sentence[2][1]
                        if int(sentence[1]) < 10 and int(sentence[2]) < 10:
                            verseResult = sentence[0][0:4].capitalize()+ " " + sentence[0][4:6] + " " + sentence[0][6:13].capitalize() + " " + sentence[1][1] + ":" + sentence[2][1]
                searchResults.append(eachWord)
            if len(searchResults) == len(searchWord):
                finalSearchResults.append(verseResult)
    return searchWord,finalSearchResults

# Driver code
if __name__ == "__main__":
    booksBible = [r"python\biblesearch\Genesis.txt", r"python\biblesearch\Exodus.txt",r"python\biblesearch\Leviticus.txt", 
                  r"python\biblesearch\Numbers.txt", r"python\biblesearch\Deuteronomy.txt",
                  r"python\biblesearch\Joshua.txt", r"python\biblesearch\Judges.txt", r"python\biblesearch\Ruth.txt", 
                  r"python\biblesearch\1Samuel.txt", r"python\biblesearch\2Samuel.txt",
                  r"python\biblesearch\1Kings.txt", r"python\biblesearch\2Kings.txt",r"python\biblesearch\1Chronicles.txt", 
                  r"python\biblesearch\2Chronicles.txt", r"python\biblesearch\Ezra.txt",
                  r"python\biblesearch\Nehemiah.txt", r"python\biblesearch\Esther.txt",r"python\biblesearch\Job.txt", 
                  r"python\biblesearch\Psalms.txt",r"python\biblesearch\Proverbs.txt",
                   r"python\biblesearch\Ecclesiastes.txt", r"python\biblesearch\SongofSolomon.txt", r"python\biblesearch\Isaiah.txt", 
                   r"python\biblesearch\Jeremiah.txt", r"python\biblesearch\Lamentations.txt",
                   r"python\biblesearch\Ezekiel.txt", r"python\biblesearch\Daniel.txt", r"python\biblesearch\Hosea.txt", 
                   r"python\biblesearch\Joel.txt", r"python\biblesearch\Amos.txt",
                  r"python\biblesearch\Obadiah.txt", r"python\biblesearch\Jonah.txt", r"python\biblesearch\Micah.txt", 
                  r"python\biblesearch\Nahum.txt", r"python\biblesearch\Habakkuk.txt",
                   r"python\biblesearch\Zephaniah.txt", r"python\biblesearch\Haggai.txt", r"python\biblesearch\Zechariah.txt", 
                   r"python\biblesearch\Malachi.txt", r"python\biblesearch\Matthew.txt",r"python\biblesearch\Mark.txt",r"python\biblesearch\Luke.txt",
                   r"python\biblesearch\John.txt",r"python\biblesearch\Acts.txt",r"python\biblesearch\Romans.txt",
                  r"python\biblesearch\1Corinthians.txt",r"python\biblesearch\2Corinthians.txt",r"python\biblesearch\Galatians.txt",
                  r"python\biblesearch\Ephesians.txt", r"python\biblesearch\Philippians.txt",
                  r"python\biblesearch\Colossians.txt",r"python\biblesearch\1Thessalonians.txt",r"python\biblesearch\2Thessalonians.txt", 
                  r"python\biblesearch\1Timothy.txt", r"python\biblesearch\2Timothy.txt",
                  r"python\biblesearch\Titus.txt",r"python\biblesearch\Philemon.txt", r"python\biblesearch\Hebrews.txt",r"python\biblesearch\James.txt",
                  r"python\biblesearch\1Peter.txt",r"python\biblesearch\2Peter.txt",r"python\biblesearch\1John.txt",
                  r"python\biblesearch\2John.txt",r"python\biblesearch\3John.txt",r"python\biblesearch\Jude.txt",r"python\biblesearch\Revelation.txt"]
    srcphrs,finalVerseList = findWord(booksBible)
    srcString = ""
    for item in srcphrs:
        srcString = srcString + item + " "
    print("Search Results:")
    Rfile = open("results.txt", "w")
    for verse in finalVerseList:
        Rfile.write("\n")
        Rfile.write(verse)
    Rfile.close()
    results = open("results.txt", "r")
    for line in results:
        print(line)
    results.close()
    print("For the query:", srcString, "the number of results are:", len(finalVerseList))
