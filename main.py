# build/0002

import time, random, json, requests, xlsxwriter, subprocess
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from datetime import datetime

## 0 ## для разных параметров, возможн ов будущем
mode = 0

# поиск
search_mode = int(input("Выбор режима поиска > по всей стране [0], по городам [1]: "))
if search_mode == 1:
    search_city = int(input("Выбор города > Москва[1], Санкт-Петербург[2], Екатеринбург[3], Новосибирск[4], Барнаул[11], Красноярск[54], Челябинск[104]: "))
search_request = input("Поиск вакансий: ")


# количество на странице
per_page = [20,50,100]

base_url = "https://api.hh.ru/vacancies"

def search(base_url):
    data_list = []  # пустой список
    page = 0
    count = 1
    while True:
        if count >= 1999:
            break
        match search_mode:
            case 0:
                # Параметры запроса
                params = {
                    'text': search_request,
                    'clusters': 'true',
                    'enable_snippets': 'true',
                    'st': 'searchVacancy',
                    'only_with_salary': 'true',
                    'specialization': '1.221',
                    'page': page,
                    'per_page': per_page[2],
                    'areas': '113',
                }

            case 1:
                # Параметры запроса
                params = {
                    'text': search_request,
                    'clusters': 'true',
                    'enable_snippets': 'true',
                    'st': 'searchVacancy',
                    'only_with_salary': 'true',
                    'specialization': '1.221',
                    'page': page,
                    'per_page': per_page[2],
                    'areas': '113',
                    'area' : search_city
                }

################################## Обработка запроса ###########################################

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            r = json.dumps(response.json(), indent=2, ensure_ascii=0)
            d = json.loads(r)
            # print(d)
            try:
                temp_list = []  # временный список для каждой страницы
                for d1 in d['items']:
                    print(f"[{count}] [{d1['area']['name']}] [{d1['schedule']['name']}] [{d1['experience']['name']}] :: {d1['name']} : {d1['salary']['from']} {d1['salary']['currency']} : {d1['alternate_url']}")
                    temp_list.append([d1['area']['name'], d1['schedule']['name'], d1['experience']['name'], d1['name'], d1['salary']['from'], d1['salary']['currency'], d1['alternate_url']])  # Добавляем данные во временный список
                    count += 1
                if temp_list:  # Проверка наличия данных
                    temp_df = pd.DataFrame(temp_list, columns=["Город", "Тип работы", "Опыт", "Название", "Зарплата", "Валюта", "Ссылка"])  # Создаем DataFrame из временного списка
                    data_list.append(temp_df)  # Добавляем временный DataFrame в список
                else:
                    break
            except: KeyError
            # print(f"\nCтраница > [{page}]")
            time.sleep(random.choice([3,5,7]))
            page += 1
        else:
            print("Ошибка запроса:", response.status_code)

    # Исключаем пустые DataFrame из списка
    data_list = [df for df in data_list if not df.empty]

    # Объединяем все DataFrame из списка в один
    final_df = pd.concat(data_list, ignore_index=True)

    # время
    now = datetime.now()
    date = now.strftime("%d-%m-%Y_%H-%M-%S")

    # записываем DataFrame в файл
    filename = f"{search_request}__{date}_output.xlsx"
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    final_df.to_excel(writer, sheet_name='Head_Hunter', index=False)

    workbook = writer.book
    worksheet = writer.sheets['Head_Hunter']

    # Устанавливаем ширину столбцов
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 80)
    worksheet.set_column('E:E', 10)
    worksheet.set_column('F:F', 8)
    worksheet.set_column('G:G', 30)

    writer.close()
    print(f"\n##########################################")
    print(f"# Данные поиска успешно записаны в файл! #")
    print(f"##########################################")

    # открываем созданный файл
    print(f"Открываем созданный файл '{filename}' в Excel > > >")
    time.sleep(1)
    subprocess.Popen(['start', 'excel', '/max', filename], shell=True)

# старт
search(base_url)