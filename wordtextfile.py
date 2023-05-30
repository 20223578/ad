filename = "TheReturnOfSherlockHolmes(1).txt"
wordCount = {}

with open(filename, "r", encoding="UTF8") as f:
    text = f.readlines()

    for line in text:
        line = line.strip()
        line = line.replace(".", " ").replace("?", " ").replace("'", " ").replace("\"", " ").replace("-", " ").replace(":", " ")
        line = line.upper()
        words = line.split(' ')

        for word in words:
            if word == '':
                continue

            if word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1

sortedWordCount = sorted(wordCount.items(), key=lambda x: x[1], reverse=True)

for word, count in sortedWordCount:
    print(word, count)
