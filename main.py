import os
import sys
import threading
from openai import OpenAI
from dotenv import load_dotenv

from knowledge_integration import real_time_update
from language_proficiency import understand_language_syntax
from algorithm_generation import generate_algorithm
from adaptation_merging import merge_languages
from prompt_generation import generate_initial_prompt, refine_prompt
from complex_solving import solve_complex_problem

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def interactive_terminal():
    print("Interactive OpenAI Terminal. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = client.chat.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": user_input}
            ],
            max_tokens=150
        )
        print("AI:", response.choices[0].message['content'])

def generate_summaries():
    summaries = {}
    w3_files = os.listdir("w3")

    for file in w3_files:
        file_path = os.path.join("w3", file)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.strip():
            continue

        response = client.chat.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Summarize the following content:\n\n{content[:5000]}"}
            ],
            max_tokens=1500
        )
        summary = response.choices[0].message['content']
        summaries[file] = summary

    return summaries

def main():
    # Print Python path for debugging
    print("Python path:", sys.path)
    
    # Real-Time Knowledge Update
    urls = [
        'https://github.com/mastermindml/mastermind', 
        'https://github.com/pythaiml/automindx', 
        'https://github.com/Professor-Codephreak', 
        'https://github.com/augml/lwe-plugin-shell', 
        'https://github.com/augml/nicegui'
    ]
    interval = 3600  # Update every hour
    knowledge_update_thread = threading.Thread(target=real_time_update, args=(interval, urls))
    knowledge_update_thread.start()
    
    # Language Proficiency Example
    code_snippet = "print('Professor Codephreak sends his regards')"
    language = "Python"
    syntax_explanation = understand_language_syntax(code_snippet, language)
    print("Syntax Explanation:", syntax_explanation)
    
    # Algorithm Generation Example
    problem_statement = "Sort an array of integers."
    language = "Python"
    algorithm = generate_algorithm(problem_statement, language)
    print("Generated Algorithm:", algorithm)
    
    # Complex Problem Solving Example
    problem_statement = "Develop a sustainable energy solution for urban areas."
    domain = "Engineering"
    solution = solve_complex_problem(problem_statement, domain)
    print("Solution:", solution)
    
    # Prompt Generation and Refinement Example
    problem_context = "We need to develop a new method for real-time data analysis."
    initial_prompt = generate_initial_prompt(problem_context)
    print("Initial Prompt:", initial_prompt)
    
    refined_prompt = refine_prompt(initial_prompt)
    print("Refined Prompt:", refined_prompt)

    # Generate and print summaries
    summaries = generate_summaries()
    for file, summary in summaries.items():
        print(f"Summary for {file}:\n{summary}\n")

    # Start interactive terminal
    interactive_terminal()

if __name__ == "__main__":
    # Create necessary directories
    os.makedirs("memory", exist_ok=True)
    os.makedirs("context", exist_ok=True)
    os.makedirs("w3", exist_ok=True)
    
    main()

