import json

def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def add_definition(word, definition):
    data = load_data()
    data[word] = definition
    save_data(data)

def search_word(word):
    data = load_data()
    return data.get(word, "Word not found in the dictionary.")

def main():
    print("Interactive Dictionary Application")
    while True:
        user_input = input("Enter a word to search (type 'exit' to quit): ").lower()
        if user_input == "exit":
            print("Goodbye!")
            break

        definition = search_word(user_input)
        print(definition)

if __name__ == "__main__":
    main()
