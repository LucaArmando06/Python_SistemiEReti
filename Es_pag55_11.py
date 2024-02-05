def print_list(l):
    print("la lista è: ")
    for elemento in l:
        print(elemento, end = " ")
    print("\n")

def main():
    x = [0, 1, 2, 3, 5, 6, 7, 8]
    
    x1 = x[:len(x) // 2] 
    x2 = x[len(x) // 2:]  

    x1.append(x2[0])

    print_list(x)
    print_list(x1)
    print_list(x2)

if __name__ == "__main__":
    main()
