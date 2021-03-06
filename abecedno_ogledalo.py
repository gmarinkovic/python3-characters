# Катарина је одлучила да својој другарици пошаље шифровану поруку, која садржи само слова енглеске абецеде,
# цифре и интерпункцијске знаке. Свако слово ће шифровати посебно на основу наредних правила.
# Мала слова се шифрују великим словима тако што се слово a шифрује словом Z, слово b шифрује словом Y, c словом X итд.,
# све до слова y које се шифрује словом B и z које се шифрује словом A. Велика слова се шифрују
# потпуно аналогно - од A које се шифрује са z до Z које се шифрује са a. Остали карактери се не мењају.
#
# Улаз: Са стандардног улаза уноси се једна линија текста, завршена карактером тачка (карактером .).
#
# Излаз: На стандардни излаз исписати шифровани текст (без карактера тачка).
#
# Пример
# Улаз
# Zdravo svima.
# Излаз
# aWIZEL HERNZ

for c in input():
    if c == '.':
        break

    if c.islower():
        tc = chr(ord('Z') - (ord(c) - ord('a')))
    elif c.isupper():
        tc = chr(ord('z') - (ord(c) - ord('A')))
    else:
        tc = c

    print(tc, end='')
