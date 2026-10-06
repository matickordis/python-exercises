i = 0
scores = {}
while True:
    i += 1
    name = input("Whats your name: ")
    scores[name] = scores.get(name, 0) + 1
    if i == 5:
        break  
print("Score:")
for n,t in scores.items():
    print(f"{n} = {t}")
