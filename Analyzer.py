

unigramDataFile = open("/Users/karthik/Desktop/NLP/MovieReviewsAnalyzer/SentimentDataset/Train/pos.txt")
bigramDataFile = open("/Users/karthik/Desktop/NLP/MovieReviewsAnalyzer/SentimentDataset/Train/pos.txt")
trigramDataFile = open("/Users/karthik/Desktop/NLP/MovieReviewsAnalyzer/SentimentDataset/Train/pos.txt")

unigramCountDictionary = dict()
bigramCountDictionary = dict()
trigramCountDictionary = dict()

unigramProbabilityMap = dict()
bigramProbabilityMap = dict()
trigramProbabilityMap = dict()

unigramCount = 0

# Method to generate unigrams count from corpus
def generateUnigrams():
	unigramsList = []
	for line in unigramDataFile:
		review = "<s> " + line + " </s>"
		unigramsList = unigramsList + review.split()
	for word in unigramsList:
		if word in unigramCountDictionary:
			unigramCountDictionary[word] += 1
		else:
			unigramCountDictionary[word] = 1
	global unigramCount
	unigramCount = len(unigramsList)

# Method to generate bigrams count from corpus
def generateBigrams():
	for line in bigramDataFile:
		bigramsList = []
		review = "<s> " + line + " </s>"
		bigramsList = bigramsList + review.split()
		for i in range(0,len(bigramsList)-1):
			word  = bigramsList[i] + " " + bigramsList[i+1]
			if word in bigramCountDictionary:
					bigramCountDictionary[word] += 1
			else:
				bigramCountDictionary[word] = 1

# Method to generate trigrams count from corpus
def generateTrigrams():
	for line in trigramDataFile:
		trigramsList = []
		review = "<s> " + line + " </s>"
		trigramsList = trigramsList + review.split()
		for i in range(0,len(trigramsList)-2):
			word  = trigramsList[i] + " " + trigramsList[i+1] + " " + trigramsList[i+2]
			if word in trigramCountDictionary:
					trigramCountDictionary[word] += 1
			else:
				trigramCountDictionary[word] = 1

# Method to generate probabilities of unigrams
def unigramProbability():
	for key in unigramCountDictionary:
		probabilityValue = unigramCountDictionary[key] / unigramCount
		unigramProbabilityMap[key] = probabilityValue

# Method to generate probabilities of bigrams
def bigramProbability():
	for key in bigramCountDictionary:
		bigramWord = key.split()[0]
		probabilityValue = bigramCountDictionary[key] / unigramCountDictionary[bigramWord]
		bigramProbabilityMap[key] = probabilityValue

# Method to generate probability of trigrams
def trigramProbability():
	for key in trigramCountDictionary:
		trigramWordList = key.split()
		firstProbability = unigramProbabilityMap[trigramWordList[0]] * bigramProbabilityMap[trigramWordList[0]+" "+trigramWordList[1]]
		secondProbability = trigramCountDictionary[key] / bigramProbabilityMap[trigramWordList[0]+" "+trigramWordList[1]]
		finalProbability = firstProbability * secondProbability
		trigramProbabilityMap[key] = finalProbability

generateUnigrams()
generateBigrams()
generateTrigrams()
unigramProbability()
bigramProbability()
trigramProbability()

print (trigramProbabilityMap)