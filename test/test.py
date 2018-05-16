from fridump import fridump

def main():
    for ps in fridump.fridump_all():
        print(ps)
    fridump.fridump(input("ps: "))

if __name__ == "__main__":
    main()
