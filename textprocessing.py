#Training Data
positiveDataFile = open("/Users/karthik/Desktop/NLP/MovieReviewsAnalyzer/SentimentDataset/Train/pos.txt")
negativeDataFile = open("/Users/karthik/Desktop/NLP/MovieReviewsAnalyzer/SentimentDataset/Train/pos.txt")

testDataFile = open("/Users/karthik/Desktop/NLP/MovieReviewsAnalyzer/SentimentDataset/Train/pos.txt")

# Returns the reviews and their corresponding category
def getTrainingData():
	positiveData = dict()
	negativeData = dict()
	trainingDataResult = dict()

	for line in positiveDataFile:
		positiveData[line] = 1

	for line in negativeDataFile:
		negativeData[line] = 0

	trainingDataResult["Positive"] = positiveData
	trainingDataResult["Negative"] = negativeData

	return trainingDataResult

# Returns the number of reviews in both positive and negative categories
def getTrainingResults():
	positiveCount = 0
	negativeCount = 0
	trainingResults = dict()
	for line in positiveDataFile:
		positiveCount += 1
	for line in negativeDataFile:
		negativeCount += 1
	trainingResults["Positive Count"] = positiveCount
	trainingResults["Negative Count"] = negativeCount

	return trainingResults

# Processes and returns a list containing test Data
def getTestData():
	testDatalist = list()
	for line in testDataFile:
		line = "<s> " + line + " </s>"
		testDatalist.append(line)
	return testDatalist