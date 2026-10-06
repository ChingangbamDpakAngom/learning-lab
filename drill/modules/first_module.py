print("This will always run")

def main():
    print("This will only run if this file is executed directly")

if __name__ == "__main__":
    main()

else:
    print("Ran by importing")