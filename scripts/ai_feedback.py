import openai
import os

# Replace with your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the following code and provide feedback:\n\n{code}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
feedback = analyze_code("src/main/java/com/javatechie/DevopsIntegrationApplication.java")
with open("results/ai-feedback.txt", "w") as output_file:
    output_file.write(feedback)
