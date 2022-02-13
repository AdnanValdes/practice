from utils import get_input
from sys import argv, exit

def main():
	data = get_input(argv[1], argv[2])

	with open(data) as f:
		data = [int(i) for i in f.readlines()]
	print(countDepthIncrease(data))
	print(countWindowDepthIncrease(data))

def countDepthIncrease(sonarData):
	count = 0
	for i in range(len(sonarData)):
		if i == 0:
			continue

		if sonarData[i] > sonarData[i -1]:
			count +=1
	return count

def countWindowDepthIncrease(sonarData):
	count = 0
	previous = 0
	for i in range(len(sonarData)):
		if i < 2:
			continue

		current = sum(sonarData[i-3:i])
		test = sonarData[i-2] + sonarData[i-1] + sonarData[i]
		print("TEST:", current, test)
		if current > previous:
			count += 1
		previous = current
	return count


if __name__ == "__main__":
	if len(argv) != 3:
		print("Usage: python3 ./script day part")
		exit()

	main()