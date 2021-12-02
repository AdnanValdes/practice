import requests
import os
from dotenv import load_dotenv

load_dotenv()

cookies = {'session':os.environ.get("SESSION")}
def get_input(day, part):
	url = f'https://adventofcode.com/2021/day/{day}/input'
	data = requests.get(url, cookies=cookies)
	with open(f"d{day}p{part}_input.txt", mode="wb") as localfile:
		localfile.write(data.content)
	return data.content
