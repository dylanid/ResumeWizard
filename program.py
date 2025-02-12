import openai

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def main():
    print("Reading Input...")
    client = openai.Client()
    response = client.chat.completions.create(
        model = "gpt-4",
        messages = [
            {"role": "system", "content": read_file("Prompts/role.txt")},
            {"role": "user", "content": "INFORMATION FOR RESUME:" + read_file("UserInput/Information.txt") + " JOB DESCRIPTION: " + read_file("UserInput/JobDescription.txt") + " RESUME TEMPLATE: " + read_file("UserInput/ResumeTemplate.txt")},
        ]
    )
    write_file("Output/Resume.tex", response.choices[0].message.content)
    print("Done!")

if __name__ == '__main__':
    main()