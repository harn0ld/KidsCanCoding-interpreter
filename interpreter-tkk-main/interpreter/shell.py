import basic

# Run the program
while True:
    input_text = input('basic > ')
    if input_text.lower().strip() == "hello world":
        print("Hello, world!")
    else:
        print("Unknown command: ", input_text)
