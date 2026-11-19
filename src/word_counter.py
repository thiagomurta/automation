words = {}
with open("teste.txt", "r", encoding="utf-8") as file:
    for line in file:
        for word in line.split():
            word = word.lower().strip(".,:;!\"'()")
            words[word] = words.get(word, 0) + 1

top = sorted(words.items(), key=lambda item: item[1], reverse=True)[:10]

print("Top words:")
for word, qtd in top:
    print(f"{word}: {qtd}")
