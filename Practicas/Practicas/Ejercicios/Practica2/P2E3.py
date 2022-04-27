import string

text_1 = (open('aux_pruebas.txt').read().lower()).split()
word_set = set(text_1)

print(word_set)

c = input("Insert a character from the alphabet: ")
if c in string.ascii_letters:
    times = 0
    for word in word_set:
        if(word[0] == c.lower()):
            times += 1
            print(f"\n###     {times}_  {word}")
    if(times == 0):
        print("\nNo words starting with tahat letter!")
    # Para solo imprimirlas podriamos hacer print(if word[0] == c.lower() (f"{word} \n"))
else:
    print("\nERROR: The selected character is not valid!")