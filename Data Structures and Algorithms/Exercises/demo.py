import openai

import openai

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "what wish for my friend Emin who is turning 17 tomorrow"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)