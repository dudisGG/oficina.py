pontos = []
for i in range(5):
    pontos.append(int(input("pontos:  ")))

media = sum(pontos) / len(pontos)

print(f"\nA média dos pontos é: {media}")
print("Pontuações acima da média:")

contador = 0
for p in pontos:
    if p > media:
        print(p)
        contador += 1

print(f"Total de pontuações acima da média: {contador}")