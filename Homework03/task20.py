# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;D, G – 2 очка;B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;K – 5 очков;J, X – 8 очков;Q, Z – 10 очков.А русские буквы оцениваются так:А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;Б, Г, Ё, Ь, Я – 3 очка;Й, Ы – 4 очка;Ж, З, Х, Ц, Ч – 5 очков;Ш, Э, Ю – 8 очков;Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.
# Ввод: ноутбук
# Вывод: 12 

scrabble_dict = dict.fromkeys(["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"],1)
scrabble_dict.update(dict.fromkeys(["D", "G"], 2))
scrabble_dict.update(dict.fromkeys(["B", "C", "M", "P"], 3))
scrabble_dict.update(dict.fromkeys(["F", "H", "V", "W", "Y"], 4))
scrabble_dict.update(dict.fromkeys(["K"], 5))
scrabble_dict.update(dict.fromkeys(["J", "X"], 8))
scrabble_dict.update(dict.fromkeys(["Q", "Z"], 10))
scrabble_dict.update(dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)) 
scrabble_dict.update(dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2))
scrabble_dict.update(dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я'], 3))
scrabble_dict.update(dict.fromkeys(['Й', 'Ы'], 4))
scrabble_dict.update(dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5))
scrabble_dict.update(dict.fromkeys(['Ш', 'Э', 'Ю'], 8))
scrabble_dict.update(dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)) 

estimated_word = input("Введите слово: ")
word_grade = 0
for i in estimated_word:
    word_grade += int(scrabble_dict[i.upper()])
print(f"Стоимость слова {estimated_word} - {word_grade}")