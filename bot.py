import discord

TOKEN = "Paste your token here."
CMD_TEXT = "!t"

def InitCommands():
    CommandEntry("ping", cmdPing)
    CommandEntry("say", cmdSay)
    # You can add as many as you like

async def cmdPing(message, args):
    await message.reply("pong!")

async def cmdSay(message, args):
    await message.channel.send(args[0])

commands = []
cmdCallbacks = []

def CommandEntry(cmdName, funcCallbk):
    global commands
    global cmdCallbacks
    commands.append(cmdName)
    cmdCallbacks.append(funcCallbk)

async def ExecuteCommand(message, text):
    for i in range(len(commands)):
        args = text.split(" ")
        if args[0] == commands[i]:
            await cmdCallbacks[i](message, args[1:])

client = discord.Client()

@client.event
async def on_ready():
    InitCommands()

@client.event
async def on_message(message):
    if not message.author.bot and message.content.startswith(CMD_TEXT + " "):
        await ExecuteCommand(message, message.content[len(CMD_TEXT) + 1:])

client.run(TOKEN)
