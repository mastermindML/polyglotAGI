import os
import sys
import threading
import json
import openai

from knowledge_integration import real_time_update
from language_proficiency import understand_language_syntax
from algorithm_generation import generate_algorithm
from adaptation_merging import merge_languages
from prompt_generation import generate_initial_prompt, refine_prompt
from complex_solving import solve_complex_problem

# Load API keys
with open("config/api_keys.json") as f:
    api_keys = json.load(f)

openai.api_key = api_keys["openai_api_key"]

def interactive_terminal():
    print("Interactive OpenAI Terminal. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=150
        )
        print("AI:", response.choices[0].text.strip())

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

    # Start interactive terminal
    interactive_terminal()

if __name__ == "__main__":
    # Create necessary directories
    os.makedirs("memory", exist_ok=True)
    os.makedirs("context", exist_ok=True)
    os.makedirs("w3", exist_ok=True)
    
    main()

