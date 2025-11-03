def check_password():
    password = input("Please enter the password: ")
    if password != "sT#n5GXZTrfh--U":
        return False
    return True

def main():
    if check_password():
        print("Access granted")
        print("Opening...")
    else:
        print("Access denied")

if __name__ == "__main__":
    main()
