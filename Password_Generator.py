import random

def create_passwords(lengths):

    chars = "abcdefghijklmnopqrstuvwxyz"
    generated_passwords = []

    for length in lengths:
        password = ""
        for _ in range(length):
            random_index = random.randrange(len(chars))
            password += chars[random_index]
        
        password = insert_number(password)
        password = insert_uppercase(password)
        
        generated_passwords.append(password)
    
    return generated_passwords

def insert_number(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
    return pword

def insert_uppercase(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
    return pword

def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    print(f"Creating {num_passwords} passwords")
    
    lengths = []
    print("Note: Minimum password length is 3 characters.")
    
    for i in range(num_passwords):
        length = int(input(f"Specify the length for Password #{i + 1}: "))
        if length < 3:
            length = 3
        lengths.append(length)
    
    passwords = create_passwords(lengths)
    
    for i in range(num_passwords):
        print(f"Generated Password #{i + 1}: {passwords[i]}")

if __name__ == "__main__":
    main()
