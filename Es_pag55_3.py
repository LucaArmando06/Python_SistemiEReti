def main():
    prima = 10
    seconda = 20

    print(f"prima = {prima} seconda = {seconda}")
    prima, seconda = seconda, prima
    print(f"prima = {prima} seconda = {seconda}")

if __name__ == "__main__":
    main()