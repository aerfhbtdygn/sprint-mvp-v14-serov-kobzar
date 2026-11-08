# ===== T-1. Главное меню (общая задача) =====
TITLE = "Дневник тренировок"  # впишите название своего продукта
MENU = []  # пункты меню: (название, функция)
 
 
def ask_int(text):
    # спрашивает целое число, пока его не введут правильно
    while True:
        value = input(text).strip()
        if value.lstrip("-").isdigit():
            return int(value)
        print("Ошибка: введите целое число")
 
 
def ask_float(text):
    # спрашивает число (можно дробное), пока его не введут правильно
    while True:
        value = input(text).strip().replace(",", ".")
        try:
            return float(value)
        except ValueError:
            print("Ошибка: введите число")
 
 
def start():
    while True:
        print()
        print("=====", TITLE, "=====")
        for number, item in enumerate(MENU, start=1):
            print(number, "-", item[0])
        print("0 - Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "0":
            print("До свидания!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(MENU):
            MENU[int(choice) - 1][1]()
        else:
            print("Нет такого пункта меню")


# ===== US-2. Добавить тренировку =====
TYPES = ["Бег", "Плавание", "Тренажёрный зал", "Велосипед"]
workouts = []  # список тренировок
 
 
def add_workout():
    for number, t in enumerate(TYPES, start=1):
        print(f"{number} - {t}")
    number = ask_int("Вид тренировки: ")
    if number < 1 or number > len(TYPES):
        print("Нет такого вида")
        return
    minutes = ask_int("Длительность, мин: ")
    if minutes <= 0:
        print("Длительность должна быть больше 0")
        return
    workouts.append({"вид": TYPES[number - 1], "мин": minutes})
    print("Тренировка записана")
 
 
MENU.append(("Добавить тренировку", add_workout))


# ===== US-3. Список тренировок =====
def show_workouts():
    if len(workouts) == 0:
        print("Тренировок пока нет")
        return
    for number, w in enumerate(workouts, start=1):
        print(f"{number}. {w['вид']} — {w['мин']} мин")
 
 
MENU.append(("Список тренировок", show_workouts))


# ===== US-4. Общее время тренировок =====
def total_time():
    total = 0
    for w in workouts:
        total = total + w["мин"]
    print(f"Всего: {total} мин ({total // 60} ч {total % 60} мин)")
 
 
MENU.append(("Общее время тренировок", total_time))


# ===== US-5. Индекс массы тела =====
def body_mass_index():
    height = ask_float("Рост, см: ")
    weight = ask_float("Вес, кг: ")
    if height <= 0 or weight <= 0:
        print("Рост и вес должны быть больше 0")
        return
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5:
        category = "недостаточный вес"
    elif bmi < 25:
        category = "норма"
    elif bmi < 30:
        category = "избыточный вес"
    else:
        category = "ожирение"
    print(f"ИМТ = {bmi:.1f} — {category}")
 
 
MENU.append(("Индекс массы тела", body_mass_index))

 
# ===== US-6. Самый частый вид тренировки =====
def favorite_type():
    if len(workouts) == 0:
        print("Тренировок пока нет")
        return
    counts = {}
    for w in workouts:
        counts[w["вид"]] = counts.get(w["вид"], 0) + 1
    best = max(counts, key=counts.get)
    print(f"Чаще всего: {best} ({counts[best]} раз(а))")
 
 
MENU.append(("Самый частый вид тренировки", favorite_type))



# ===== ЗАПУСК: эта строка всегда должна быть последней =====
start()
