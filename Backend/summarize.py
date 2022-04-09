import os
import openai
import time

openai.api_key = "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"

def split_text(input, max_tokens=500):
    
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
                subresult = ' '.join(split_input[index-max_tokens: i + 1])
                index = i + 1
                output.append(subresult)
                break
            # If we are on the last loop iteration just put everything into the segment
            if i == index - max_tokens + 1:
                subresult = ' '.join(split_input[index-max_tokens: index])
                output.append(subresult)
                break
    
    return output


def summarize(input, max_tokens=200):
    parsed_input = split_text(input)
    output = []
    start_time = time.time()
    for token_segment in parsed_input:
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Summarize this for a college student:\n" + token_segment.strip(),
        temperature=0.2,
        max_tokens=max_tokens,
        top_p=1.0,
        frequency_penalty=0.4,
        presence_penalty=0.3
        )

        output.append(response['choices'][0]['text'])

    return '\n'.join(output)