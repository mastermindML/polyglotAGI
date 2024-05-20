import sys
import threading
from knowledge_integration import real_time_update
from language_proficiency import understand_language_syntax
from algorithm_generation import generate_algorithm
from adaptation_merging import merge_languages
from prompt_generation import generate_initial_prompt, refine_prompt
from complex_solving import solve_complex_problem  # Import the new module

def main():
    # Print Python path for debugging
    print("Python path:", sys.path)
    
    # Real-Time Knowledge Update
    urls = [
        'https://github.com/mastermindML/mastermind', 
        'https://github.com/pythaiml/automindx', 
        'https://github.com/augml/nicegui', 
        'https://github.com/augml/lwe-plugin-shell', 
        'https://github.com/augml/ollama-python'
    ]
    interval = 3600  # Update every hour
    knowledge_update_thread = threading.Thread(target=real_time_update, args=(interval, urls))
    knowledge_update_thread.start()
    
    # Language Proficiency Example
    code_snippet = "print('codephreak is ...')"
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

if __name__ == "__main__":
    main()
