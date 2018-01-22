import sys
import random

def main(argv):
	file = str(argv)
	print(file)
	draw(file)

def draw(file):
	inputNames = readInput(file)
	shuffleNames(inputNames)

	resultFile = open('winners.csv', 'a')
	remainingFile = open('nonwinners.csv', 'w')

	#frames
	inputNames = sample(inputNames, 12, 1, "Crystal Photo Frames (4x6)", resultFile)
	inputNames = sample(inputNames, 5, 2, "Paper Weight", resultFile)
	inputNames = sample(inputNames, 7, 3, "Mirror Trinket Box", resultFile)

	remainingFile.write(convertToCsv(inputNames))
	resultFile.close()
	remainingFile.close()
	return


def readInput(filename):
	input = open(filename, "r")
	names = input.read().split('\n')
	names = [x for x in names[1:] if x]
	splitnames =list(map(lambda x: x.split(','), names))
	input.close()
	return splitnames

def shuffleNames(names):
	for i in range(0,10):
		random.shuffle(names)
	return


def sample(nameList, noOfPicks, index, typeText, fileHandle):
	interestedPpl = [x for x in nameList if x[index] == str(1)]
	winners = interestedPpl
	if noOfPicks <= len(interestedPpl):
		winners = random.sample(nameList, noOfPicks)

	fileHandle.write("\n\n" + typeText + ": \n")
	fileHandle.write(convertToCsv(winners))
	return [x for x in nameList if x not in winners]

def convertToCsv(list):
	str = ""
	for item in list:
		for index in range(0, len(item)):
			str += item[index]
			if(index<len(item)-1):
				str += ','

		str+='\n'

	return str;

if __name__ == "__main__":
   main(sys.argv[1])