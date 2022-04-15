while True:
    w = input()
    if len(w) in range(1, 10**3):
        break
if not w[0].isupper():
    w = w.capitalize()
print(w)