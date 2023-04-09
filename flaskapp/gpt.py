import openai


def init_api(api_key):
    openai.api_key = api_key


def gpt_api_call(title, header, count):


    api_prompt = """For an article about "ARTICLE", make a section titled "HEADER" that is about COUNT characters long. The section is a part of a larger article about "ARTICLE".  Send only the section and omit the section's header. Write it in the style of an encyclopedia."""

    api_prompt.replace("ARTICLE", title)
    api_prompt.replace("HEADER", header)
    api_prompt.replace("COUNT", count)

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=api_prompt,
    max_tokens=count)
    return response.choices[0].text



