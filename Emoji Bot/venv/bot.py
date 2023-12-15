import discord
import responses
from urllib import request
from colorama import Fore, Back, Style

async def send_message(message, user_message, is_private):
    try :
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e :
        print(e)

def run_discord_bot():
    TOKEN = 'MTE3MjU0NDU1ODY5ODA3ODMwOQ.GxS7hA._jl4ksrnP5V1LwBMmJY7ibDBa0urIPTEuJF9HU'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    image_types = ["png", "jpeg", "gif", "jpg", "mp4", "mov"]

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(username, " write " ,user_message, " in " ,channel)
        print(message)
        if len(user_message) != 0:
            if user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=True)
            else :
                if user_message[0] == '!' :
                    user_message = user_message[1:]
                    await send_message(message, user_message, is_private=False)
        else :
            #EXPERIMENTAL USED FOR IMAGE CLASSIFIER
            counter = 0
            for attachment in message.attachments:
                    if any(attachment.filename.lower().endswith(image) for image in image_types):
                        counter += 1
                        name = str(counter) + attachment.filename
                        await attachment.save(f'C:/Users/Jansen/Desktop/CODING/phyton/ML/Final Project/Emoji Bot/attachments/{name}') # 'attachments/{{attachment.filename}' is the PATH to where the attachmets/images will be saved. Example: home/you/Desktop/attachments/{{attachment.filename}
                        print(f'Attachment {attachment.filename} has been saved to directory/folder > attachments.')

            print("picture")



    client.run(TOKEN)