# chapter look up

def chapterLookUp(bName, cNum):
    verseList = []
    booksBible = {"Genesis":r"python\\biblesearch\\Genesis.txt", "Exodus":r"python\\biblesearch\\Exodus.txt",
    "Leviticus":r"python\\biblesearch\\Leviticus.txt", "Numbers":r"python\\biblesearch\\Numbers.txt", 
    "Deuteronomy": r"python\\biblesearch\\Deuteronomy.txt", "Joshua":r"python\\biblesearch\\Joshua.txt", 
	"Judges":r"python\\biblesearch\\Judges.txt", "Ruth":r"python\\biblesearch\\Ruth.txt", "1 Samuel":r"python\\biblesearch\\1Samuel.txt", 
	"2 Samuel":r"python\\biblesearch\\2Samuel.txt","1 Kings":r"python\\biblesearch\\1Kings.txt", "2 Kings":r"python\\biblesearch\\2Kings.txt",
	"1 Chronicles":r"python\\biblesearch\\1Chronicles.txt", "2 Chronicles":r"python\\biblesearch\\2Chronicles.txt", "Ezra":r"python\\biblesearch\\Ezra.txt",
    "Nehemiah":r"python\\biblesearch\\Nehemiah.txt", "Esther":r"python\\biblesearch\\Esther.txt", "Job":r"python\\biblesearch\\Job.txt", 
	"Psalms":r"python\\biblesearch\\Psalms.txt","Proverbs":r"python\\biblesearch\\Proverbs.txt","Ecclesiastes":r"python\\biblesearch\\Ecclesiastes.txt", 
	"Song of Solomon":r"python\\biblesearch\\SongofSolomon.txt", "Isaiah":r"python\\biblesearch\\Isaiah.txt", "Jeremiah":r"python\\biblesearch\\Jeremiah.txt",
	"Lamentations":r"python\\biblesearch\\Lamentations.txt","Ezekiel":r"python\\biblesearch\\Ezekiel.txt", "Daniel":r"python\\biblesearch\\Daniel.txt", 
	"Hosea":r"python\\biblesearch\\Hosea.txt", "Joel":r"python\\biblesearch\\Joel.txt", "Amos":r"python\\biblesearch\\Amos.txt",
    "Obadiah":r"python\\biblesearch\\Obadiah.txt", "Jonah":r"python\\biblesearch\\Jonah.txt", "Micah":r"python\\biblesearch\\Micah.txt", 
	"Nahum":r"python\\biblesearch\\Nahum.txt", "Habakkuk":r"python\\biblesearch\\Habakkuk.txt", "Zephaniah":r"python\\biblesearch\\Zephaniah.txt", 
	"Haggai":r"python\\biblesearch\\Haggai.txt", "Zechariah":r"python\\biblesearch\\Zechariah.txt", "Malachi":r"python\\biblesearch\\Malachi.txt", 
	"Matthew":r"python\\biblesearch\\Matthew.txt","Mark":r"python\\biblesearch\\Mark.txt","Luke":r"python\\biblesearch\\Luke.txt",
	"John": r"python\\biblesearch\\John.txt","Acts":r"python\\biblesearch\\Acts.txt","Romans":r"python\\biblesearch\\Romans.txt",
    "1 Corinthians":r"python\\biblesearch\\1Corinthians.txt","2 Corinthians":r"python\\biblesearch\\2Corinthians.txt","Galatians":r"python\\biblesearch\\Galatians.txt",			
    "Ephesians":r"python\\biblesearch\\Ephesians.txt", "Philippians":r"python\\biblesearch\\Philippians.txt",
    "Colossians":r"python\\biblesearch\\Colossians.txt","1 Thessalonians":r"python\\biblesearch\\1Thessalonians.txt","2 Thessalonians":r"python\\biblesearch\\2Thessalonians.txt", 
    "1 Timothy":r"python\\biblesearch\\1Timothy.txt", "2 Timothy": r"python\\biblesearch\\2Timothy.txt","Titus": r"python\\biblesearch\\Titus.txt","Philemon": r"python\\biblesearch\\Philemon.txt", 
	"Hebrews": r"python\\biblesearch\\Hebrews.txt","James":r"python\\biblesearch\\James.txt","1 Peter": r"python\\biblesearch\\1Peter.txt",
	"2 Peter":r"python\\biblesearch\\2Peter.txt","1 John":r"python\\biblesearch\\1John.txt","2 John":r"python\\biblesearch\\2John.txt",
	"3 John":r"python\\biblesearch\\3John.txt","Jude":r"python\\biblesearch\\Jude.txt","Revelation":r"python\\biblesearch\\Revelation.txt"}
    book = ""
    for bookname,booklink in booksBible.items():
        if bName == bookname:
            book = booklink
            break;
    if book == "":
        return "Book not found"
    # Open bookname and reads into bList list into memory from persistent storage
    Bfile = open(book, "r")
    bList = []
    for line in Bfile:
        tLine = line.split(" ")
        bList.append(tLine)
    Bfile.close()
    for verseLine in bList:
        verseString = ""
        if int(verseLine[1]) == int(cNum):
            for i in range(2, len(verseLine)):
                verseString = verseString + verseLine[i] + " "
            verseList.append(verseString)
    if len(verseList) == 0:
        return
    return verseList
if __name__ == "__main__":
    bookName = input("Enter the book: ")
    chapNumStart = input("Enter the chapter number: ")
    vList = chapterLookUp(bookName,chapNumStart)
    if vList:
        for verse in vList:
            print(verse)
    else:
        print("Book and Chapter does not exist")
