import json

try:
    with open('vacancies.json', 'r', encoding='utf-8') as f:
        vacancies = json.load(f)

        threshold = 150000
        high_salary = [vacancy for vacancy in vacancies if vacancy["salary"] > threshold]

        sorted_vacancies = sorted(high_salary, key=lambda x: x['salary'], reverse=True)

        whole_skills = set()
        for vacancy in vacancies:
            whole_skills.update(vacancy['skills'])

        company_count = {}
        for vacancy in vacancies:
            company = vacancy['company']
            if company in company_count:
                company_count[company] += 1
            else:
                company_count[company] = 1


    report = {
        "total": len(vacancies),
        "high_salary": sorted_vacancies,
        "unique_skills": list(whole_skills),
        "companies": company_count
    }

    with open('report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"Найдено вакансий: {len(vacancies)}")
    print(f"С зарплатой выше {threshold}: {len(sorted_vacancies)}")
    print(f"Уникальных навыков: {len(whole_skills)}")
    print("Отчёт сохранён в report.json")

except FileNotFoundError:
    print("Ошибка: Файл vacancies.json не найден!")

except json.JSONDecodeError as e:
    print(f"Ошибка: Неправильный формат JSON! Детали: {e}")



