from fridump import fridump

def main():
    ps_list = fridump.fridump_all()
    for p in ps_list:
        fridump.fridump(p)

if __name__ == "__main__":
    main()