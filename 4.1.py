import json

words = ["яблоко", "банан", "яблоко", "груша", "банан", "банан", "яблоко"]

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
print("--------------------------------------------")

team_a = ["Python", "SQL", "Git", "Docker"]
team_b = ["Python", "Java", "Git", "Kubernetes"]

team = team_b + team_a
team1 = set(team_b) - set(team_a)
team2 = set(team_a) - set(team_b)
common = set(team_a) & set(team_b)
print(common)
print(set(team))
print(set(team1))
print(set(team2))
print("--------------------------------------------")

numbers = [1, -3, 5, -7, 9, -11, 13, -15]
pluses = [n for n in numbers if n  > 0]
pluses1 = [n ** 2 for n in numbers ]
pluses2 = [n *2 for n in numbers if n > 0]
print(pluses)
print(pluses1)
print(pluses2)
print("--------------------------------------------")

employees = [
    {"name": "Анна", "age": 31, "salary": 120000},
    {"name": "Борис", "age": 24, "salary": 95000},
    {"name": "Вера", "age": 28, "salary": 150000},
    {"name": "Григорий", "age": 35, "salary": 95000},
]
sorted1 = sorted(employees, key=lambda x: x["salary"], reverse=True)
sorted2 = sorted(employees, key= lambda x: x["age"])
sorted3 = sorted(employees, key= lambda x: (-x["salary"],x["name"]))
print(sorted1)
print(sorted2)
print(sorted3)
print("--------------------------------------------")
data = {
    "project": "python-basics-practice",
    "author": "твоё имя",
    "topics": ["lists", "functions", "dict", "json"],
    "completed": True
}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open('data.json', 'r', encoding='utf-8') as f:
    dataforprint = json.load(f)
for key, value in dataforprint.items():
    print(f"{key}: {value}")
