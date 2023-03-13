
kus_vas={""} 
import random

# Открываем файл с вопросами и ответами
with open('kusimised_vastused.txt', 'r') as f:
    lines = f.readlines()

# Создаем список для хранения вопросов и ответов
questions = []
answers = []

# Проходимся по строкам файла и заполняем списки вопросов и ответов
for i, line in enumerate(lines):
    if i % 2 == 0:
        # Вопросы находятся на четных строках
        questions.append(line.strip())
    else:
        # Ответы находятся на нечетных строках
        answers.append(line.strip())

# Выбираем случайный вопрос
index = random.randint(0, len(questions)-1)
question = questions[index]
answer = answers[index]

# Выводим вопрос и ждем ответа от пользователя
print(question)
user_answer = input()

# Проверяем ответ пользователя
if user_answer == answer:
    print("Верно!")
else:
    print("Неверно. Правильный ответ:", answer)


def kusimus_vastused_1(n):
    """
    """    
    print(f"Tere, {n}! Alustame küsitlust.")
    punktid=0    
    for kusimus, vastus in kus_vas.items():
        kasutaja_vastus=input(kusimus)
        if kasutaja_vastus.lower()==vastus.lower():
            print("Õige vastus!")
            punktid+=1
        else:
            print("Vale vastus!")    
    if punktid>3:
        print(f"Tubli töö, {n}! Teie skoor oli {punktid}/5.")
        with open("oiged.txt", "a", encoding="utf-8") as f:
            f.write(f"{n}: {punktid}/5\n")
    else:
        print(f"Pole paha, {n}. Teie skoor oli {punktid}/5.")
        with open("valed.txt", "a", encoding="utf-8") as f:
            f.write(f"{n}: {punktid}/5\n")
"""
def kusimus_vastused_2(n):        
    print(f"Tere, {n}! Alustame küsitlust.")
    punktid=0    
    for kusimus, vastus in kus_vas.items():
        kasutaja_vastus=input(kusimus)
        if kasutaja_vastus.lower()==vastus.lower():
            print("Õige vastus!")
            punktid+=1
        else:
            print("Vale vastus!")    
    if punktid > 3:
        print(f"Tubli töö, {n}! Teie skoor oli {punktid}/5.")
        with open("oiged.txt", "a", encoding="utf-8") as f:
            f.write(f"{n}: {punktid}/5\n")
    else:
        print(f"Pole paha, {n}. Teie skoor oli {punktid}/7.")
        with open("valed.txt", "a", encoding="utf-8") as f:
            f.write(f"{n}: {punktid}/5\n")
"""
