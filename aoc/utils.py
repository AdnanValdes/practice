import requests
import os
from dotenv import load_dotenv

load_dotenv()

cookies = {'session':os.environ.get("SESSION")}
def get_input(day):
	url = f'https://adventofcode.com/2021/day/{day}/input'
	data = requests.get(url, cookies=cookies)
	print(data.text)
	return data
