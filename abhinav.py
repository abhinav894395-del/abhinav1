def greet(name):
    return f"Hello, {name}! 👋"

def main():
    name = input("Enter your name: ")
    
    if name.strip() == "":
        print("You didn't enter a name.")
    else:
        message = greet(name)
        print(message)

    # Simple loop example
    print("\nCounting to 5:")
    for i in range(1, 6):
        print(i)

if
