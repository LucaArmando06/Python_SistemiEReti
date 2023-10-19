def print_list(l):
    print("la lista è: ")
    for elemento in l:
        print(elemento, end = " ")
    print("\n")

def main():
    a = [0, 1, 2, 3]
    b = [4, 5, 6, 7]

    print_list(a + b)
if __name__ == "__main__":
    main()