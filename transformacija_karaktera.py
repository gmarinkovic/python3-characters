# Написати програм којим се трансформише учитани каракатер тако што се мало слово пребацује у велико,
# велико слово у мало, а остали карактери се не мењају.
#
# Улаз: У првој линији стандардног улаза налази се један карактер.
#
# Излаз: На стандардном излазу приказати трансформисан карактер.
#
# Пример
# Улаз
# t
# Излаз
# T

ch = input("Unesi karakter: ")[0]

if ch.islower():
    ch = ch.upper()
elif ch.isupper():
    ch = ch.lower()
print(ch)