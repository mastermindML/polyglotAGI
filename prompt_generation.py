import openai

def generate_initial_prompt(problem_context):
    """
    Generates an initial prompt based on the provided context.

    Args:
        problem_context (str): The context or problem statement.

    Returns:
        str: Generated initial prompt.
    """
    response = openai.Completion.create(
      engine="gpt-4o",
      prompt=f"Generate an initial prompt for the following context:\\n{problem_context}",
      max_tokens=1500
    )
    return response.choices[0].text.strip()

def refine_prompt(initial_prompt):
    """
    Refines the initial prompt to be more specific and effective.

    Args:
        initial_prompt (str): The initial generated prompt.

    Returns:
        str: Refined prompt.
    """
    response = openai.Completion.create(
      engine="davinci-codex",
      prompt=f"Refine the following prompt to be more specific:\\n{initial_prompt}",
      max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
problem_context = "We need to develop a new method for real-time data analysis."
initial_prompt = generate_initial_prompt(problem_context)
print(initial_prompt)

refined_prompt = refine_prompt(initial_prompt)
print(refined_prompt)
