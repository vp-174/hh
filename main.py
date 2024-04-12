# build/0003
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
import time, random, json, requests, xlsxwriter, subprocess
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from datetime import datetime
from PySide6.QtCore import QThread, Signal

class SearchThread(QThread):
    update_count = Signal(int)
    update_msg = Signal(str)

    def __init__(self, base_url, search_mode, search_request):
        super().__init__()
        self.base_url = base_url
        self.search_mode = search_mode
        self.search_request = search_request

    def run(self):
        # количество на странице
        per_page = [20, 50, 100]

        data_list = []  # пустой список
        page = 0
        count = 1
        while True:
            if count >= 1999:
                break
            match self.search_mode:
                case 0:
                    # Параметры запроса
                    params = {
                        'text': self.search_request,
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
                    # Москва
                    params = {
                        'text': self.search_request,
                        'clusters': 'true',
                        'enable_snippets': 'true',
                        'st': 'searchVacancy',
                        'only_with_salary': 'true',
                        'specialization': '1.221',
                        'page': page,
                        'per_page': per_page[2],
                        'areas': '113',
                        'area': 1
                    }

                case 2:
                    # Санкт-Петербург
                    params = {
                        'text': self.search_request,
                        'clusters': 'true',
                        'enable_snippets': 'true',
                        'st': 'searchVacancy',
                        'only_with_salary': 'true',
                        'specialization': '1.221',
                        'page': page,
                        'per_page': per_page[2],
                        'areas': '113',
                        'area': 2
                    }

                case 3:
                    # Екатеринбург
                    params = {
                        'text': self.search_request,
                        'clusters': 'true',
                        'enable_snippets': 'true',
                        'st': 'searchVacancy',
                        'only_with_salary': 'true',
                        'specialization': '1.221',
                        'page': page,
                        'per_page': per_page[2],
                        'areas': '113',
                        'area': 3
                    }

                case 4:
                    # Новосибирск
                    params = {
                        'text': self.search_request,
                        'clusters': 'true',
                        'enable_snippets': 'true',
                        'st': 'searchVacancy',
                        'only_with_salary': 'true',
                        'specialization': '1.221',
                        'page': page,
                        'per_page': per_page[2],
                        'areas': '113',
                        'area': 4
                    }

                case 5:
                    # Барнаул
                    params = {
                        'text': self.search_request,
                        'clusters': 'true',
                        'enable_snippets': 'true',
                        'st': 'searchVacancy',
                        'only_with_salary': 'true',
                        'specialization': '1.221',
                        'page': page,
                        'per_page': per_page[2],
                        'areas': '113',
                        'area': 11
                    }

                case 6:
                    # Красноярск
                    params = {
                        'text': self.search_request,
                        'clusters': 'true',
                        'enable_snippets': 'true',
                        'st': 'searchVacancy',
                        'only_with_salary': 'true',
                        'specialization': '1.221',
                        'page': page,
                        'per_page': per_page[2],
                        'areas': '113',
                        'area': 54
                    }
                case 7:
                    # Челябинск
                    params = {
                        'text': self.search_request,
                        'clusters': 'true',
                        'enable_snippets': 'true',
                        'st': 'searchVacancy',
                        'only_with_salary': 'true',
                        'specialization': '1.221',
                        'page': page,
                        'per_page': per_page[2],
                        'areas': '113',
                        'area': 104
                    }
            ################################## Обработка запроса ###########################################
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                r = json.dumps(response.json(), indent=2, ensure_ascii=0)
                d = json.loads(r)
                try:
                    temp_list = []  # временный список для каждой страницы
                    for d1 in d['items']:
                        print(
                            f"[{count}] [{d1['area']['name']}] [{d1['schedule']['name']}] [{d1['experience']['name']}] :: {d1['name']} : {d1['salary']['from']} {d1['salary']['currency']} : {d1['alternate_url']}")
                        temp_list.append(
                            [d1['area']['name'], d1['schedule']['name'], d1['experience']['name'], d1['name'],
                             d1['salary']['from'], d1['salary']['currency'],
                             d1['alternate_url']])  # Добавляем данные во временный список

                        self.update_count.emit(count)  # Отправляем сигнал с текущим count
                        count += 1
                    if temp_list:  # Проверка наличия данных
                        temp_df = pd.DataFrame(temp_list,
                                               columns=["Город", "Тип работы", "Опыт", "Название", "Зарплата", "Валюта",
                                                        "Ссылка"])  # Создаем DataFrame из временного списка
                        data_list.append(temp_df)  # Добавляем временный DataFrame в список
                    else:
                        break
                except KeyError:
                    pass
                time.sleep(random.choice([3, 5, 7]))
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
        self.update_msg.emit("Запись в файл")
        filename = f"{self.search_request}__{date}_output.xlsx"
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

        self.update_msg.emit(f"Открытие файла {filename}")
        time.sleep(1)
        subprocess.Popen(['start', 'excel', '/max', filename], shell=True)

class HHParse(QMainWindow):
    def __init__(self):
        super(HHParse, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        base_url = "https://api.hh.ru/vacancies"
        self.ui.lineSearch.setPlaceholderText("Введите запрос для поиска и нажмите Enter")
        self.ui.lineSearch.returnPressed.connect(
            lambda: self.start_search(base_url, self.ui.comboBox.currentIndex(), self.ui.lineSearch.text()))

    def start_search(self, base_url, search_mode, search_request):
        self.thread = SearchThread(base_url, search_mode, search_request)
        self.thread.start()
        self.thread.update_count.connect(self.update_statusbar1)
        self.thread.update_msg.connect(self.update_statusbar2)

    def update_statusbar1(self, count):
        self.ui.statusbar.showMessage(f"Найдено: {count} (макс. 2000)")
    def update_statusbar2(self, msg):
        self.ui.statusbar.showMessage(f"{msg}")

app = QApplication()
window = HHParse()
window.show()
sys.exit(app.exec())