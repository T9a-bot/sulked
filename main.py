from highrise import BaseBot
from highrise import __main__
from collections import UserDict
from asyncio import run as arun
from highrise.models import SessionMetadata, User
from highrise.models import Position
from highrise.models import SessionMetadata, User, CurrencyItem, Item, AnchorPosition, Reaction, ModerateRoomRequest, Position
from highrise import BaseBot, User, Position, SessionMetadata
import asyncio
from highrise import BaseBot, __main__
from highrise.models import (AnchorPosition, Item, Position, User,)
from highrise import *
from highrise.models import *
import time
from asyncio import Task
from highrise.__main__ import *
from highrise.models import (AnchorPosition, CurrencyItem,Item,Position,SessionMetadata,User,)
emote_list : list[tuple[str, str]] = [('Sleep', 'idle-sleep'), ('Pouty Face', 'idle-sad'), ('Sleepy', 'idle-loop-tired'), ('Sit', 'idle-loop-sitfloor'), ('Shy', 'idle-loop-shy'), ('Enthused', 'idle-enthusiastic'), ('Feel The Beat', 'idle-dance-headbobbing'), ('Yes', 'emote-yes'), ('The Wave', 'emote-wave'), ('Tired', 'emote-tired'), ('Think', 'emote-think'), ('Theatrical', 'emote-theatrical'), ('Snow Angel', 'emote-snowangel'), ('Shy', 'emote-shy'), ('Sad', 'emote-sad'), ('Peace', 'emote-peace'), ('No', 'emote-no'), ('Model', 'emote-model'), ('Flirty Wave', 'emote-lust'), ('Amused', 'emote-laughing2'), ('Laugh', 'emote-laughing'), ('Kiss', 'emote-kiss'), ('Super Kick', 'emote-kicking'), ('Jump', 'emote-jumpb'), ('Judo Chop', 'emote-judochop'), ('Hot', 'emote-hot'), ('Hello', 'emote-hello'), ('Happy', 'emote-happy'), ('Face Palm', 'emote-exasperatedb'), ('Exasperated', 'emote-exasperated'), ('Collapse', 'emote-death2'), ('Revival', 'emote-death'), ('Dab', 'emote-dab'), ('Curtsy', 'emote-curtsy'), ('Confusion', 'emote-confused'), ('Cold', 'emote-cold'), ('Charging', 'emote-charging'), ('Bunny Hop', 'emote-bunnyhop'), ('Bow', 'emote-bow'), ('Boo', 'emote-boo'), ('Home Run!', 'emote-baseball'), ('Falling Apart', 'emote-apart'), ('Thumbs Up', 'emoji-thumbsup'), ('Point', 'emoji-there'), ('Sneeze', 'emoji-sneeze'), ('Smirk', 'emoji-smirking'), ('Sick', 'emoji-sick'), ('Gasp', 'emoji-scared'), ('Punch', 'emoji-punch'), ('Stunned', 'emoji-dizzy'), ('Cursing Emote', 'emoji-cursing'), ('Sob', 'emoji-crying'), ('Clap', 'emoji-clapping'), ('Raise The Roof', 'emoji-celebrate'), ('Arrogance', 'emoji-arrogance'), ('Angry', 'emoji-angry'), ('Vogue Hands', 'dance-voguehands'), ('Savage', 'dance-tiktok8'), ("Dontstartnow", 'dance-tiktok2'), ('Yoga Flow', 'dance-spiritual'), ("Shopping", 'dance-shoppingcart'), ('Russian', 'dance-russian'), ('Macarena', 'dance-macarena'), ('Blackpink','dance-blackpink'),]


emote_durations = {
    "Sleep": 15,
    "Pouty Face": 10,
    "Sleepy": 10,
    "Sit": 15,
    "Shy": 15,
    "Enthused": 15,
    "Feel The Beat": 15,
    "Yes": 4,
    "The Wave": 3,
    "Tired": 5,
    "Think": 5,
    "Theatrical": 10,
    "Snow Angel": 7,
    "Sad": 5,
    "Peace": 6,
    "No": 4,
    "Model": 7,
    "Flirty Wave": 5,
    "Amused": 10,
    "Laugh": 4,
    "Kiss": 4,
    "Super Kick": 10,
    "Jump": 10,
    "Judo Chop": 10,
    "Hot": 6,
    "Hello": 4,
    "Happy": 4,
    "Face Palm": 10,
    "Exasperated": 10,
    "Collapse": 10,
    "Revival": 10,
    "Dab": 10,
    "Curtsy": 3,
    "Confusion": 10,
    "Cold": 10,
    "Charging": 9,
    "Bunny Hop": 10,
    "Bow": 4,
    "Boo": 10,
    "Home Run!": 10,
    "Falling Apart": 10,
    "Thumbs Up": 4,
    "Point": 10,
    "Sneeze": 10,
    "Smirk": 10,
    "Sick": 10,
    "Gasp": 10,
    "Punch": 10,
    "Stunned": 10,
    "Cursing Emote": 10,
    "Sob": 10,
    "Clap": 10,
    "Raise The Roof": 10,
    "Arrogance": 10,
    "Angry": 10,
    "Vogue Hands": 10,
    "Savage": 10,
    "Dontstartnow": 10,
    "Yoga Flow": 10,
    "Shopping": 10,
    "Russian": 10,
    "Macarena": 10,
    "Blackpink": 10,
}
class BotDefinition:

  def __init__(self, bot, room_id, api_token):
    self.bot = bot
    self.room_id = room_id
    self.api_token = api_token

class MyBot(BaseBot):
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.following_user = None 
                self.banned_users = {} 
                self.following_username = None
                super().__init__()
                self.user_positions = {}


        



          async def loop(self: BaseBot, user: User, message: str) -> None:
               async def loop_emote(self: BaseBot, user: User, emote_name: str) -> None:
                   emote_id = ""
                   for emote in emote_list:
                       if emote[0].lower() == emote_name.lower():
                           emote_id = emote[1]
                           break
                   if emote_id == "":
                       await self.highrise.chat("Invalid emote")
                       return

                   await self.highrise.chat(f"@{user.username} is looping {emote_name}")

                   # الحصول على مدة الرقصة
                   emote_duration = emote_durations.get(emote_name, None)
                   if emote_duration is None:
                       await self.highrise.chat(f"The emote {emote_name} does not have a specified duration.")
                       return

                   while True:
                       try:
                           await self.highrise.send_emote(emote_id, user.id)
                       except:
                           await self.highrise.chat(f"Sorry, @{user.username}, this emote isn't free or you don't own it.")
                           return

                       # فترة انتظار لمدة الرقصة
                       await asyncio.sleep(emote_duration)

                       room_users = (await self.highrise.get_room_users()).content
                       user_in_room = False
                       for room_user, position in room_users:
                           if room_user.id == user.id:
                               user_in_room = True
                               break
                       if not user_in_room:
                           break

               try:
                   splited_message = message.split(" ")
                   # The emote name is every string after the first one
                   emote_name = " ".join(splited_message[1:])
               except:
                   await self.highrise.chat("Invalid command format. Please use '/loop <emote name>.")
                   return
               else:   
                   taskgroup = self.highrise.tg
                   task_list: list[Task] = list(taskgroup._tasks)
                   for task in task_list:
                       if task.get_name() == user.username:
                           # Removes the task from the task group
                           task.cancel()

                   room_users = (await self.highrise.get_room_users()).content
                   user_list = [room_user.username for room_user, pos in room_users]

                   taskgroup.create_task(coro=loop_emote(self, user, emote_name))
                   task_list: list[Task] = list(taskgroup._tasks)
                   for task in task_list:
                       if task.get_coro().__name__ == "loop_emote" and not (task.get_name() in user_list):
                           task.set_name(user.username)

          async def stop_loop(self: BaseBot, user: User, message: str) -> None:
               taskgroup = self.highrise.tg
               task_list: list[Task] = list(taskgroup._tasks)
               for task in task_list:
                   print(task.get_name())
                   if task.get_name() == user.username:
                       task.cancel()
                       await self.highrise.chat(f"Stopping your emote loop, {user.username}!")
                       return
               await self.highrise.chat(f"You're not looping any emotes, {user.username}")
               return

          

          async def run(self, room_id, token):
            definitions = [BotDefinition(self, room_id, token)]
            await __main__.main(definitions)

          async def teleport_user_next_to(self, target_username: str, requester_user: User):

                room_users = await self.highrise.get_room_users()
                requester_position = None

                for user, position in room_users.content:
                  if user.id == requester_user.id:
                      requester_position = position
                      break
                for user, position in room_users.content:
                  if user.username.lower() == target_username.lower(): 
                    z = requester_position.z 
                    new_z = z + 1 

                    user_dict = {
                      "id": user.id,
                      "position": Position(requester_position.x, requester_position.y, new_z, requester_position.facing)
                    }
                    await self.highrise.teleport(user_dict["id"], user_dict["position"])

          async def on_user_join(self, user: User, position: Position | AnchorPosition):
            await self.highrise.chat(f" Welcome to FIND A DATE💗. @{user.username},  Enjoy your stay, find new people and possibly the love of your life. If you need assistance, request a mod in chat.")

          async def get_bot_balance(self):
                try:
                   
                    wallet_info = await self.highrise.get_wallet()

                    
                    balance = wallet_info.content[0].amount

                    return balance
                except Exception as e:
                    print("حدث خطأ أثناء جلب المعلومات:", e)
                    return None

          async def teleporter(self, message: str)-> None:
              """
                  Teleports the user to the specified user or coordinate
                  Usage: /teleport <username> <x,y,z>
                                                                      """
              #separates the message into parts
              #part 1 is the command "/teleport"
              #part 2 is the name of the user to teleport to (if it exists)
              #part 3 is the coordinates to teleport to (if it exists)
              try:
                  command, username, coordinate = message.split(" ")
              except:
                  await self.highrise.chat("Incorrect format, please use /teleport <username> <x,y,z>")
                  return

              #checks if the user is in the room
              room_users = (await self.highrise.get_room_users()).content
              for user in room_users:
                  if user[0].username.lower() == username.lower():
                      user_id = user[0].id
                      break
              #if the user_id isn't defined, the user isn't in the room
              if "user_id" not in locals():
                  await self.highrise.chat("User not found, please specify a valid user and coordinate")
                  return

              #checks if the coordinate is in the correct format (x,y,z)
              try:
                  x, y, z = coordinate.split(",")
              except:
                  await self.highrise.chat("Coordinate not found or incorrect format, please use x,y,z")
                  return

              #teleports the user to the specified coordinate
              await self.highrise.teleport(user_id = user_id, dest = Position(float(x), float(y), float(z)))
    
          async def on_chat(self, user: User, message: str):
            if message == "!1":
                    await self.highrise.teleport(user.id, Position(10, 0.0, 18.0))

            if message == "!2":
                      await self.highrise.teleport(user.id, Position(13.5, 7.75 , 17.5))

            if message == "!3":
                await self.highrise.teleport(user.id, Position(14, 15 , 19.5))
            if message == "!4":
                await self.highrise.teleport(user.id, Position(13.5, 20 , 4.5))
            if message.startswith("/teleport ")and user.username in  [ "suIked", "UNlMPRESSED", "dollparts666", "Ayristaa", "sunniivaa","Tancorix", "Lil.Sushi", "bratpixie"]:
                
                    await self.teleporter(message)

            if message.lower().startswith("loop "):
                  await self.loop(user, message)
            elif message.lower().startswith("stoploop"):
                  await self.stop_loop(user, message)

            if message.startswith("0"):
                    await self.highrise.send_emote("emote-float", user.id)
            if message.startswith("2"):
                    await self.highrise.send_emote("dance-tiktok2", user.id)   
            if message.startswith("3"):
                    await self.highrise.send_emote("emote-pose1", user.id)
            if message.startswith("4"):
                    await self.highrise.send_emote("dance-shoppingcart", user.id)
            if message.startswith("5"):
                    await self.highrise.send_emote("dance-russian", user.id)
            if message.startswith("6"):
                    await self.highrise.send_emote("idle_singing", user.id)
            if message.startswith("7"):
                    await self.highrise.send_emote("idle-enthusiastic", user.id)   
            if message.startswith("8"):
                    await self.highrise.send_emote("idle-dance-casual", user.id)   
            if message.startswith("9"):
                    await self.highrise.send_emote("idle-loop-sitfloor", user.id)
            if message.startswith("10"):
                    await self.highrise.send_emote("emote-lust", user.id)
            if message.startswith("11"):
                    await self.highrise.send_emote("emote-greedy", user.id)
            if message.startswith("12"):
                    await self.highrise.send_emote("emote-bow", user.id)
            if message.startswith("13"):
                    await self.highrise.send_emote("emote-curtsy", user.id)
            if message.startswith("14"):
                    await self.highrise.send_emote("emote-snowball", user.id)
            if message.startswith("15"):
                    await self.highrise.send_emote("emote-snowangel", user.id)
            if message.startswith("16"):
                    await self.highrise.send_emote("emote-confused", user.id)
            if message.startswith("17"):
                    await self.highrise.send_emote("emote-teleporting", user.id)
            if message.startswith("18"):
                    await self.highrise.send_emote("emote-swordfight", user.id)
            if message.startswith("19"):
                    await self.highrise.send_emote("emote-energyball", user.id)
            if message.startswith("20"):
                    await self.highrise.send_emote("dance-tiktok8", user.id)
            if message.startswith("21"):
                    await self.highrise.send_emote("dance-blackpink", user.id)
            if message.startswith("22"):
                    await self.highrise.send_emote("emote-model", user.id)
            if message.startswith("23"):
                    await self.highrise.send_emote("dance-pennywise", user.id)
            if message.startswith("24"):
                    await self.highrise.send_emote("dance-tiktok10", user.id)
            if message.startswith("25"):
                    await self.highrise.send_emote("emote-telekinesis", user.id)
            if message.startswith("26"):
                    await self.highrise.send_emote("emote-hot", user.id)
            if message.startswith("27"):
                    await self.highrise.send_emote("dance-weird", user.id)
            if message.startswith("28"):
                    await self.highrise.send_emote("emote-pose7", user.id)
            if message.startswith("29"):
                    await self.highrise.send_emote("emote-pose8", user.id)
            if message.startswith("30"):
                    await self.highrise.send_emote("emote-pose3", user.id)
            if message.startswith("31"):
                    await self.highrise.send_emote("emote-pose5", user.id)
            if message.startswith("32"):
                await self.highrise.send_emote("emote-kiss", user.id)

            if message.startswith("33"):
                await self.highrise.send_emote("emote-laughing", user.id)
            if message.startswith("34"):
                await self.highrise.send_emote("emoji-cursing", user.id)
            if message.startswith("35"):
                await self.highrise.send_emote("emoji-flex", user.id)
            if message.startswith("36"):
                await self.highrise.send_emote("emoji-gagging", user.id)
            if message.startswith("37"):
                await self.highrise.send_emote("emoji-celebrate", user.id)
            if message.startswith("38"):
                await self.highrise.send_emote("dance-macarena", user.id)
            if message.startswith("39"):
                await self.highrise.send_emote("emote-charging", user.id)
            if message.startswith("40"):
                await self.highrise.send_emote("dance-shoppingcart", user.id)
            if message.startswith("41"):
                await self.highrise.send_emote("emote-maniac", user.id)
            if message.startswith("42"):
                await self.highrise.send_emote("emote-snake", user.id)
            if message.startswith("43"):
                await self.highrise.send_emote("emote-frog", user.id)
            if message.startswith("44"):
                await self.highrise.send_emote("emote-superpose", user.id)
            if message.startswith("45"):
                await self.highrise.send_emote("emote-cute", user.id)
            if message.startswith("46"):
                await self.highrise.send_emote("dance-tiktok9", user.id)
            if message.startswith("47"):
                await self.highrise.send_emote("dance-weird", user.id)
            if message.startswith("48"):
                await self.highrise.send_emote("emote-cutey", user.id)
            if message.startswith("49"):
                await self.highrise.send_emote("emote-punkguitar", user.id)
            if message.startswith("50"):
                await self.highrise.send_emote("emote-zombierun", user.id)
            if message.startswith("51"):
                await self.highrise.send_emote("emote-fashionista", user.id) 
            if message.startswith("52"):
                await self.highrise.send_emote("emote-gravity", user.id)
            if message.startswith("53"):
                await self.highrise.send_emote("dance-icecream", user.id)
            if message.startswith("54"):
                await self.highrise.send_emote("dance-wrong", user.id)
            if message.startswith("55"):
                await self.highrise.send_emote("idle-uwu", user.id)
            if message.startswith("56"):
                await self.highrise.send_emote("idle-dance-tiktok4", user.id)
            if message.startswith("57"):
                await self.highrise.send_emote("emote-shy2", user.id)
            if message.startswith("58"):
                await self.highrise.send_emote("dance-anime", user.id)

            emote_mapping = {
                "all a": "emote-float",
                "all b": "dance-tiktok2",
                "all c": "emote-pose1",
                "all d": "dance-shoppingcart",
                "all e": "dance-russian",
                "all f": "idle_singing",
                "all g": "idle-enthusiastic",
                "all h": "idle-dance-casual",
                "all i": "idle-loop-sitfloor",
                "all j": "emote-lust",
                "all k": "emote-greedy",
                "all l": "emote-bow",
                "all m": "emote-curtsy",
                "all n": "emote-snowball",
                "all o": "emote-snowangel",
                "all p": "emote-confused",
                "all q": "emote-teleporting",
                "all r": "emote-swordfight",
                "all s": "emote-energyball",
                "all t": "dance-tiktok8",
                "all u": "dance-blackpink",
                "all v": "emote-model",
                "all w": "dance-pennywise",
                "all x": "dance-tiktok10",
                "all y": "emote-telekinesis",
                "all z": "emote-hot",
                "all 1": "dance-weird",
                "all 2": "emote-pose7",
                "all 3": "emote-pose8",
                "all 4": "emote-pose3",
                "all 5": "emote-pose5"
              }
            # تحقق من البداية وقم بإرسال الرقصة المناسبة لجميع المستخدمين في الغرفة
            for key, emote in emote_mapping.items():
                if message.startswith(key) and user.username in  ["T9s", "suIked", "UNlMPRESSED", "dollparts666", "Ayristaa", "sunniivaa","Tancorix", "Lil.Sushi", "bratpixie"]:
                    roomUsers = (await self.highrise.get_room_users()).content
                    for roomUser, _ in roomUsers:
                        if isinstance(roomUser, User):
                            await self.highrise.send_emote(emote, roomUser.id)
                        else:
                            print("Ignoring non-User object in roomUsers")
                    break


            if message.startswith("!help"):
                  await self.highrise.chat("Available dance emotes are: Sleep, Pouty Face, Sleepy, Sit, Shy, Enthused, Feel The Beat, Yes, The Wave, Tired, Think, Theatrical, Snow Angel, Sad, Peace, No, Model, Flirty Wave, Amused, Laugh, Kiss")

            if message.startswith("!help"):
                  await self.highrise.chat("Super Kick, Jump, Judo Chop, Hot, Hello, Happy, Face Palm, Exasperated, Collapse, Revival, Dab, Curtsy, Confusion, Cold, Charging, Bunny Hop, Bow, Boo, Home Run!, Falling Apart")

            if message.startswith("!help"):
                  await self.highrise.chat("Thumbs Up, Point, Sneeze, Smirk, Sick, Gasp, Punch, Stunned, Cursing Emote, Sob, Clap, Raise The Roof, Arrogance, Angry, Vogue Hands, Savage, Dontstartnow, Yoga Flow, Shopping, Russian, Macarena, Blackpink")


            if message.lower().startswith("/g ") and user.username == "suIked":
                  parts = message.split(" ")
                  if len(parts) != 2:
                        await self.highrise.send_message(user.id, "Invalid command")
                        return
                  try:
                                amount = int(parts[1])
                  except:
                        await self.highrise.chat("Invalid amount")

                  roomUsers = (await self.highrise.get_room_users()).content
                  bot_wallet = await self.highrise.get_wallet()
                  bot_amount = bot_wallet.content[0].amount
                  if bot_amount <= amount:
                      await self.highrise.chat("I don't have enough Hehe")
                      return

                  bars_dictionary = {10000: "gold_bar_10k", 
                               5000: "gold_bar_5000",
                               1000: "gold_bar_1k",
                               500: "gold_bar_500",
                               100: "gold_bar_100",
                               50: "gold_bar_50",
                               10: "gold_bar_10",
                               5: "gold_bar_5",
                               1: "gold_bar_1"}
                  fees_dictionary = {10000: 1000,
                               5000: 500,
                               1000: 100,
                               500: 50,
                               100: 10,
                               50: 5,
                               10: 1,
                               5: 1,
                               1: 1}
                  tip = []
                  total = 0
                  for bar in bars_dictionary:
                      if amount >= bar:
                          bar_amount = amount // bar
                          amount = amount % bar
                          for _i in range(bar_amount):
                              tip.append(bars_dictionary[bar])
                              total = bar + fees_dictionary[bar]

                  if total > bot_amount:
                      await self.highrise.chat("I don't have enough hehe")
                      return
                  for roomUser, _ in roomUsers:
                    if isinstance(roomUser, User):
                      for bar in tip:
                        await self.highrise.tip_user(roomUser.id, bar)

              
            if message.startswith("come") and user.username in  ["T9s", "suIked", "UNlMPRESSED", "dollparts666", "Ayristaa", "sunniivaa","Tancorix", "Lil.Sushi", "bratpixie"]:
              response = await self.highrise.get_room_users()
              your_pos = None
              for content in response.content:
                if content[0].id == user.id and isinstance(content[1], Position):
                  your_pos = content[1]
                  break
              if not your_pos:
                await self.highrise.send_whisper(user.id, "احداثيات غير صالحه")
                return
              await self.highrise.chat("i am comeing")
              await self.highrise.walk_to(your_pos)


            allowed_users = ["sulked", "T9s"]
            if message.startswith("!summon") and user.username in  ["T9s", "suIked", "UNlMPRESSED", "dollparts666", "Ayristaa", "sunniivaa","Tancorix", "Lil.Sushi", "bratpixie"]:
                allowed_users = message.split("@")[-1].strip()
                if allowed_users in allowed_users:
                  await self.teleport_user_next_to(allowed_users, user)


            if message.startswith("heart ") and user.username in  ["T9s", "suIked", "UNlMPRESSED", "dollparts666", "Ayristaa", "sunniivaa","Tancorix", "Lil.Sushi", "bratpixie"]:  # تحقق من رسالة تبدأ بـ "heart "
                try:
                    # استخراج العدد المطلوب واسم المستخدم من الرسالة
                    parts = message.split()
                    num_hearts = int(parts[-1])
                    target_username = parts[1].strip('@').lower()

                    if 1 <= num_hearts <= 100:
                        for _ in range(num_hearts):
                            target_user = None
                            response = await self.highrise.get_room_users()
                            for user_info in response.content:
                                if user_info[0].username.lower() == target_username:
                                    target_user = user_info[0]
                                    break

                            if target_user:
                                await self.highrise.react("heart", target_user.id)
                            else:
                                await self.highrise.chat(f"the user {target_username} Not available in the room.")
                    else:
                        await self.highrise.chat("1  _ 100  only ")
                except ValueError:
                    await self.highrise.chat("الرجاء إدخال عدد صحيح بعد 'heart @user'.")

            if message.startswith("/heart") and user.username in ["T9s", "suIked", "UNlMPRESSED", "dollparts666", "Ayristaa", "sunniivaa","Tancorix", "Lil.Sushi", "bratpixie"]:
                try:
                      # جلب جميع المستخدمين في الغرفة
                      room_users_response = await self.highrise.get_room_users()

                      if room_users_response and room_users_response.content:
                          room_users = room_users_response.content
                      else:
                          await self.highrise.chat("لم أتمكن من جلب المستخدمين في الغرفة.")
                          return

                      # قائمة الاستثناءات
                      excluded_users = ["DaterBot","daterbot"]

                      for user_info in room_users:
                          try:
                              if isinstance(user_info, tuple) and len(user_info) == 2:
                                  target_user, position = user_info
                                  if isinstance(target_user, User):
                                      if target_user.id != user.id and target_user.username not in excluded_users:
                                          await self.highrise.react("heart", target_user.id)
                                      else:
                                          # تجاهل محاولة إرسال القلب إلى نفسك أو إلى المستخدمين المستثنين
                                          continue
                                  else:
                                      await self.highrise.chat(f"خطأ في معالجة المستخدم: {user_info}")
                              else:
                                  await self.highrise.chat(f"تنسيق غير صحيح لبيانات المستخدم: {user_info}")
                          except Exception as react_error:
                              await self.highrise.chat(f"حدث خطأ أثناء إرسال القلب إلى {target_user.username}: {str(react_error)}")

                      await self.highrise.chat("done")

                except Exception as e:
                      await self.highrise.chat(f"حدث خطأ أثناء معالجة الطلب: {str(e)}")

            if "!wallet" in message:
              balance = await self.get_bot_balance()
              if balance is not None:
                  await self.highrise.chat(f"I have  {balance} only :)")
              else:
                  await self.highrise.chat("تعذر العثور على معلومات الرصيد.")
            else:

              pass

            if message.lstrip().startswith('Move'):
                if user.username.lower() in ["t9s", "suiked", "unlmpressed", "dollparts666", "ayristaa", "sunniivaa","tancorix", "lil.sushi", "bratpixie"]:
                    response = await self.highrise.get_room_users()
                    users = [content[0] for content in response.content]
                    usernames = [user.username.lower() for user in users]

                    parts = message[1:].split()
                    args = parts[1:]

                    if len(args) < 2:
                      await self.highrise.send_whisper(user.id,"Use: Command > Name > Place ")
                      return
                    elif args[0][0] != "@":
                      await self.highrise.send_whisper(user.id,f" Incorrect format  '@username'.  ")
                      return
                    elif args[0][1:].lower() not in usernames:
                      await self.highrise.send_whisper(user.id,f"{args[0][1:]}Not in the room.")
                      return

                    position_name = " ".join(args[1:])
                    if position_name == '!1':
                      dest = Position(10, 0.0, 18.0)

                    elif position_name == '!2':
                      dest = Position(13.5, 7.75 , 17.5)

                    elif position_name == '!3':
                      dest = Position(14, 15 , 19.5)
                        
                    elif position_name == '!4':
                      dest = Position(13.5, 20 , 4.5)

                    else:
                      return await self.highrise.send_whisper(user.id,f"  The site is wrong ")
                    user_id = next(
                        (u.id for u in users if u.username.lower() == args[0][1:].lower()),
                        None)
                    if not user_id:
                      await self.highrise.send_whisper(user.id,f"User {args[0][1:]} unavailable ")
                      return

                    await self.highrise.teleport(user_id, dest)
                    await self.highrise.send_whisper(
                        user.id, f" move  {args[0][1:]} to ({dest.x}, {dest.y}, {dest.z})")
                else:
                    await self.highrise.send_whisper(user.id, " You can't fix this ")
            else:
                  pass

if __name__ == "__main__":
  room_id = "64fdf66f030eab792af7fcf8"
  token = "dea4a6999b06a46fde46186131aedee12d369fd975e665ffe9ec0ecd123831e7"
  arun(MyBot().run(room_id, token))
