# A simple Python program

def greet(name):
    """Return a personalized greeting."""
    return f"Hello, {name}! Welcome to Python."

# Main program
if __name__ == "__main__":
    user_name = "Saikumar"
    message = greet(user_name)
    print(message)
