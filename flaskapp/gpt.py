import openai


def init_api(api_key):
    openai.api_key = api_key


def gpt_api_call(title, header, count):


    api_prompt = """For an article about "ARTICLE", make a section titled "HEADER" that is about COUNT characters long. The section is a part of a larger article about "ARTICLE".  Send only the section and omit the section's header. Write it in the style of an encyclopedia."""

    api_prompt = api_prompt.replace("ARTICLE", title)
    api_prompt = api_prompt.replace("HEADER", header)
    api_prompt = api_prompt.replace("COUNT", str(count))

    #print("API PROMPT: ", api_prompt)

    response = openai.ChatCompletion.create(
    model= "gpt-3.5-turbo-0301",
    messages=[
        {"role": "user", "content": api_prompt}
    ],
    max_tokens=count)
    return response.choices[0].message.content

