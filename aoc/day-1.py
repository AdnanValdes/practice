from utils import get_input

def main():
	data = get_input(1, 1)
	with open(f"d1p1_input.txt") as f:
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