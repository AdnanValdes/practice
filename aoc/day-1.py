from utils import get_input
from sys import argv

def main():
	if len(argv) != 3:
		print("Usage: python3 ./script day part")
		return 1

	data = get_input(argv[1], argv[2])
	with open(data) as f:
		data = [int(i) for i in f.readlines()]
	print(countDepthIncrease(data))


def countDepthIncrease(sonarData):

	count = 0
	for i in range(len(sonarData)):
		if i == 0:
			continue

		if sonarData[i] > sonarData[i -1]:
			count +=1
	return count


if __name__ == "__main__":
	main()