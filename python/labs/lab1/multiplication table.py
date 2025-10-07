# Function 1: Using for loop
def table_for(num):
    print("\nMultiplication Table using for loop:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Function 2: Using while loop
def table_while(num):
    print("\nMultiplication Table using while loop:")
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1

# Function 3: Simulating do-while loop
def table_do_while(num):
    print("\nMultiplication Table using simulated do-while loop:")
    i = 1
    while True:
        print(f"{num} x {i} = {num * i}")
        i += 1
        if i > 10:
            break

# --- Test ---
n = int(input("Enter a number: "))
table_for(n)
table_while(n)
table_do_while(n)
