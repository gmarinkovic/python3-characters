# Написати програм који за учитани ASCII карактер испитује да ли је мало слово, велико слово, цифра или
# нешто четврто
#
# Улаз: У једној линији стандардног улаза налази се један карактер.
#
# Излаз: У једној линији стандарног излаза приказати једну од следћих информација: MALO SLOVO, VELIKO
# SLOVO, CIFRA, OSTALO.
#
# Пример 1
# Улаз
# a
# Излаз
# MALO SLOVO
# Пример 2
# Улаз
# B
# Излаз
# VELIKO SLOVO
# Пример 3
# Улаз
# 7
# Излаз
# CIFRA
# Пример 4
# Улаз
# :
# Излаз
# OSTALO

c = input("Unesi karakter: ")

if c.islower():
    print("MALO SLOVO")
elif c.isupper():
    print("VELIKO SLOVO")
elif c.isdigit():
    print("CIFRA")
else:
    print("OSTALO")
