import requests
import json 
import re
response = requests.get("https://opentdb.com/api.php?amount=10")
question_data = []


for question in response.json()["results"]:
    question["question"] = re.sub("&quot;", '"', question["question"])
    question["question"] = re.sub("&#039;", "'", question["question"])
    question_data.append({"question": question["question"], "answer": question["correct_answer"]})