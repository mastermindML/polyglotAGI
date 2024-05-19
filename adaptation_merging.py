import openai

def generate_algorithm(problem_statement, language):
    """
    Generates an efficient algorithm for the given problem statement in the specified programming language.

    Args:
        problem_statement (str): The problem statement for which the algorithm is to be generated.
        language (str): The programming language in which the algorithm should be written.

    Returns:
        str: Generated algorithm for the problem statement.
    """
    response = openai.Completion.create(
      engine="davinci-codex",
      prompt=f"Generate an efficient algorithm for the following problem in {language}:\\n{problem_statement}",
      max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
problem_statement = "Sort an array of integers."
language = "Python"
algorithm = generate_algorithm(problem_statement, language)
print(algorithm)
