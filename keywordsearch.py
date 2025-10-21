# keyword search
def findWord(allbooks,searchWord):
    finalSearchResults = []
    verseResult = ""
    finalList = []

    for Bbook in allbooks:
        Bfile = open(Bbook, "r")
        wordList = []
        for line in Bfile:
            tLine = line.split(" ")
            finalList.append(tLine)
        Bfile.close()
        
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
    return finalSearchResults

def findBibleverse(searchWords):
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
    finalVerseList = findWord(booksBible,searchWords)
    return finalVerseList

def searchVerse():
    try:
        keywords = keywordsValue.get()
        kwList = keywords.split(" ")
        fvList = findBibleverse(kwList)
        if len(fvList) == 0:
            results["text"] = "No Results"
        elif len(fvList) == 1:
            verse = fvList[0]
            results["text"] = f"{verse}"
        else:
            results["text"] = "Results too many"
    except ValueError:
        results["text"] = "Error"

def clearValue():
    keywordsValue.delete(0,END)
    results["text"] = ""

def exitWindow():
    window.destroy()

if __name__ == "__main__":
    import math
    from tkinter import *
    window = Tk()
    window.title("Bible Keyword Search Tool")
    window.geometry("350x85")
    window.resizable(width=True, height=True)
    
    # Add Enter keywords label
    keywords = Label(window, text = "Enter keywords")
    keywords.grid(row=0, column=1)

    # Add keywords value Entry Textbox
    keywordsValue = Entry(window, width = 35)
    keywordsValue.grid(row=0, column=2)
   
    # Add Result label
    result = Label(window,text = "Result:")
    result.grid(row=2, column=1)

    # Add Result value
    results = Label(window,text = "")
    results.grid(row=2, column = 2)

    # Add search button
    computeButton = Button(window, text = "Search", command = searchVerse)
    computeButton.grid(row=3,column=1)
    
    # Add clear button
    clearButton = Button(window, text = "Clear", command = clearValue)
    clearButton.grid(row=3,column=2)
    
    # Add exit button
    exitButton = Button(window,text = "Exit", command = exitWindow)
    exitButton.grid(row=3,column=3)
    
    window.mainloop()
