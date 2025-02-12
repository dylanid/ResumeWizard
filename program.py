import openai

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def main():
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = []

    )

if __name__ == '__main__':
    main()