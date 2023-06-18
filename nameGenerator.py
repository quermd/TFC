import wonderwords
from wonderwords import RandomWord
r = RandomWord()
# Generar un nombre de carpeta aleatorio
def generate_folder_name():
    return r.word(starts_with="ru",include_parts_of_speech=["nouns"], word_min_length=6, word_max_length=10)

print("Palabras: {")
for i in range(12):
    word = generate_folder_name()
    print(word)
    print(",")
print("}")
