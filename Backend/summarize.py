import os
import openai

openai.api_key = "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"

def split_text(input, max_tokens=8):
    
    index = 0
    split_input = input.split()
    output = []
    while index < len(split_input):
        index += max_tokens
        # If we hit the end of the string with this increase
        if index >= len(split_input):
            subresult = ' '.join(split_input[index - max_tokens: index + 1])
            output.append(subresult)
            return output
        # If we want to count backwards til we hit punctuation
        for i in range(index, index - max_tokens, - 1):
            if split_input[i][-1] == '?' or split_input[i][-1] == '!' or split_input[i][-1] == '.':
                subresult = ' '.join(split_input[index-max_tokens:i])
                index = i + 1
                output.append(subresult)
                break
            if i == index - max_tokens + 1:
                subresult = ' '.join(split_input[index-max_tokens:i])
                output.append(subresult)
                break
    
    return output


def summarize(input):
    parsed_input = split_text(input)
    return parsed_input
    response = openai.Completion.create(
    engine="text-curie-001",
    prompt="Summarize this for a college student:\n\nJupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.",
    temperature=0.7,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )