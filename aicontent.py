import os
import openai
import config
from PIL import Image
import urllib.request

import requests
from io import BytesIO
openai.api_key = config.OPENAI_API_KEY



def productDescription(query):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="What is the current market trend for: {}".format(query),
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )


    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = 'Eh I got nothing....'
    else:
        answer = 'Eh I got nothing....'
    return answer

def imageDescription(queryImg):
    image = openai.Image.create(
            prompt="{}".format(queryImg),
            n=2,
            size="512x512",
            response_format='url'
        )


    if 'data' in image:
        if len(image['data']) > 0:
            ai_image = image['data'][0]['url']
            urllib.request.urlretrieve(ai_image, "aiImg.png")
            img = Image.open("aiImg.png")
            #answer_img = img.show()


        else:
            answer_img = 'Eh I got nothing....'
    else:
        answer_img = 'Eh I got nothing....'

    return img
#DEBUG
#query = 'Samsung Mobile Phone'

#productDescription(query)

def nftDescription(query):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Get an NFT trend analysis for: {}".format(query),
      temperature=0.7,
      max_tokens=2048,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )


    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = 'Eh I got nothing....'
    else:
        answer = 'Eh I got nothing....'

    return answer

def exchangeDescription(query):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Get market information for the cryptocurrency exchange including 24-hour trading volume: {}".format(query),
      temperature=0.7,
      max_tokens=2048,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )


    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = 'Eh I got nothing....'
    else:
        answer = 'Eh I got nothing....'

    return answer


def blockHistory(query):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Get the blockchain information and history for: {}".format(query),
      temperature=0.7,
      max_tokens=2048,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )


    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = 'Eh I got nothing....'
    else:
        answer = 'Eh I got nothing....'

    return answer

















###