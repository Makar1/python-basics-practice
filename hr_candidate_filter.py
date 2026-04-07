# HR candidate filter
# Filters candidates by experience, salary and required skill

candidates = [
    ["Алексей Смирнов", 28, 3, 120000.0, "Python,SQL,Git"],
    ["Мария Иванова", 34, 7, 180000.0, "Python,Django,PostgreSQL,Git"],
    ["Дмитрий Козлов", 24, 1, 85000.0, "Python,Git,HTML"],
    ["Анна Петрова", 31, 5, 150000.0, "SQL,Excel,Git,Tableau"],
    ["Сергей Новиков", 27, 2, 95000.0, "Python,SQL,Git,Docker"],
    ["Елена Морозова", 40, 12, 250000.0, "Python,SQL,Git,ML,Spark"],
    ["Игорь Волков", 22, 0, 70000.0, "Python,HTML,CSS"],
    ["Ольга Соколова", 29, 4, 130000.0, "SQL,Git,Java,Spring"],
    ["Павел Лебедев", 35, 8, 200000.0, "Python,SQL,Git,Airflow,Docker"],
    ["Юлия Захарова", 26, 2, 110000.0, "Python,Git,FastAPI,SQL"],
]

def check_candidate(candidate, min_exp,max_salary, required_skill) -> bool:
    return (candidate[2] >= min_exp and candidate[3] <= max_salary and required_skill in candidate[4])

def filter_candidates(candidates, min_exp=None, max_salary=None, required_skill=None) -> list:
    result = []
    for person in candidates:
        if check_candidate(person, min_exp,max_salary, required_skill):
            result.append(person)
    return result

def average_stats(result):
    years_old = 0
    exp = 0
    for i in result:
        years_old += i[1]
        exp += i[2]
    avg_years_old = years_old / len(result)
    avg_exp = exp / len(result)
    return avg_exp, avg_years_old


min_exp = int(input("Введите минимальный опыт: "))
max_salary = float(input("Введите максимальную зарплату: "))
required_skill = input("Введите навык: ")

result = filter_candidates(candidates, min_exp, max_salary, required_skill)

while not result:
    print("Никто не подошел.")
    max_salary = float(input("Новая максимальная зарплата: "))
    result = filter_candidates(candidates, min_exp, max_salary, required_skill)

for i in range(len(result)):
    person = result[i]
    print(f"{i+1}. {person[0]} - опыт {person[2]} года - {person[3]} ₽")

avg_exp, avg_age = average_stats(result)
print(f"Средний возраст: {avg_age:.1f} лет")
print(f"Средний опыт: {avg_exp:.1f} лет")


