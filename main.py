import random

words = ("кухня", "чобіт", "човен", "любов", "щастя", "мотор", "кожух", "геній",
         "масло", "мийка", "риска", "кішка", "сирок", "парта", "дошка", "груша",
         "курка", "заєць", "війна", "ручка", "пушка", "пишка", "мишка", "мошка",
         "байка", "варка")

hidden_word = random.choice(words)

attempts = 6
now_attempt = 0

print("ВІТАЄМО У WORDLE")
print(f"У вас є {attempts} спроб, щоб вгадати слово з 5 літер.\n")

while now_attempt < attempts:
    now_attempt += 1
    guess = input(f"Спроба {now_attempt}/{attempts}:\nВведіть слово: ").lower()

    if guess == hidden_word:
        print(f"Ви вгадали слово {hidden_word} за {now_attempt} спроб(и)!")
        break
    else:
        print("Неправильно.\n")
else:
    print(f"На жаль, ви не вгадали слово. Загадане слово: {hidden_word}")