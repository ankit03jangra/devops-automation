import openai
import os

# Replace with your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    response = openai.Completions.create(
        model="gpt-3.5-turbo",
        messages=[
                    {"role": "system", "content": "You are an expert code reviewer."},
                    {"role": "user", "content": "Analyze the following code and provide feedback:\n\n{code}"}
                ],
        max_tokens=150,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

# Example usage

feedback = analyze_code("src/main/java/com/javatechie/DevopsIntegrationApplication.java")
os.makedirs("results", exist_ok=True)  # Ensure the output directory exists
with open("{output_dir}/ai-feedback.txt", "w") as output_file:
   output_file.write(feedback)
print("AI feedback has been written to results/ai-feedback.txt")