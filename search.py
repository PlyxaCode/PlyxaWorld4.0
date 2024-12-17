import os

COLOR_CODE = {
    "RESET": "\033[0m",
    "GREEN": "\033[36m"
}


def search_phone_number_in_folder(folder_path):
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(
            f'{COLOR_CODE["GREEN"]}Ошибка: "{folder_path}" не является папкой или не существует.{COLOR_CODE["RESET"]}')
        return

    search_value = input(
        f'{COLOR_CODE["GREEN"]}Введите номер телефона для поиска (в формате 79999999999): {COLOR_CODE["RESET"]}')

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        for line in file:
                            if search_value in line:
                                print(
                                    f'{COLOR_CODE["GREEN"]}Найден номер {search_value} в файле: {file_path}{COLOR_CODE["RESET"]}')
                                print(f'{COLOR_CODE["GREEN"]}Информация о пользователе:{COLOR_CODE["RESET"]}')
                                print(line)
                                print('\n')
                except Exception as e:
                    print(f'{COLOR_CODE["GREEN"]}Ошибка при чтении файла {file_path}: {e}{COLOR_CODE["RESET"]}')

    input(f'{COLOR_CODE["GREEN"]}Нажмите Enter......{COLOR_CODE["RESET"]}')


folder_path = 'Database'
search_phone_number_in_folder(folder_path)
