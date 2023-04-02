import discord
import datetime, os, math, pytz
from discord.ext import commands
from discord import app_commands

#discordpy の機能で一部イベントの受け取り・スルーを制御できる=>通信量の削減
intents = discord.Intents.all()  # デフォルトのIntentsオブジェクトを生成
intents.typing = False  # typingを受け取らないように
GUILD_ID = discord.Object(id=726304962639953921)

class Myclient(discord.Client):
    def __init__(self, intents: discord.Intents):
        super().__init__(
            
            intents=intents)

        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=GUILD_ID)
        await self.tree.sync(guild=GUILD_ID)

class DayofWeek:
    def Zeller(self):
        y = self.year
        m = self.month
        if m < 3:
            m = m + 12
            y = y - 1
        d = self.day
        ans = (y + math.floor(y/4) - math.floor(y/100) + math.floor(y/400) + math.floor(((13 * m)+ 8)/5) + d) % 7
        return ans
    
    def checkMonth(self):
        if (self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12) and self.day > 31:
            self.month += 1
            self.day = 1
            self.checkYear()
            return

        elif (self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11) and self.day > 30:
            self.month += 1
            self.day = 1
            return
        
        elif (self.month == 2 and self.day > self.checkLeap):
            self.month += 1
            self.day = 1
            return
        
        else:
            return

    def checkYear(self):
        if self.month > 12:
            self.month = 1
            self.day = 1
    
    def checkLeap(self):
        if self.year % 400 == 0:
            return 29
        
        elif self.year % 100 != 0 and self.year % 4 == 0:
            return 29
        
        else:
            return 28

client = Myclient(intents=intents)
#起動確認
print(intents.members)

#リアクション定義(ユニコード絵文字は直接貼り付け、カスタムスタンプは<:stumpName:stumpId>)
hi = "<:hi:726379564816793600>"
mizu = "<:mizu:726379564791758848>"
thuchi = "<:thuchi:726379564623724595>"
kaze = "<:kaze:726379564829245491>"
hikari = "<:hikari:726379564539838465>"
yami = "<:yami:726379564502089780>"
debuff = "<:arrow_double_down:>"
fara = ":KEYCAP TEN:"
maru = ":o:"
batu = "cross mark"


getu ="<:w_getu:1091758148622221472>"
ka = "<:w_ka:1091758139902275745>"
sui = "<:w_sui:1091758127906570291>"
moku = "<:w_moku:1091758119345987664>"
kin = "<:w_kin:1091758107450949744>"
do = "<:w_do:1091758168134131857>"
niti = "<:w_niti:1091758158701150268>"

#embedのVal定義
embedDefVal = "参加者は居ません"

#BOT動作に必要な定数
TOKEN =os.environ.get("DISCORD_TOKEN")

@client.event
async def on_ready():
    #起動後PC側にメッセージ送信
    print(datetime.datetime.now().time(),"on_ready/discordVer",discord.__version__)
    await client.change_presence(activity=discord.Activity(name="/マルチ募集" ,type = discord.ActivityType.playing))

@client.tree.command(name="マルチ募集", description="マルチ募集用コマンド")
async def ping(interaction: discord.Integration, name:str, date:str="", comment:str=""):
    #name=クエスト名,date=日時,comment=コメント
        embed = discord.Embed( # Embedを定義する
                        title=name,# タイトル　将来的にここにコメントのmessageを取得して編集して代入
                        color=0x00ff00, # フレーム色指定(今回は緑)
                        description=name+"のマルチ募集です\n開始時間:"+date+"~\n"+comment, # Embedの説明文 必要に応じて
                        url="" # これを設定すると、タイトルが指定URLへのリンクになる
                        )
        embed.set_author(name=client.user, # Botのユーザー名
                    #url="", # titleのurlのようにnameをリンクにできる。botのWebサイトとかGithubとか
                    icon_url=client.user.display_avatar.url# Botのアイコンを設定してみる
                    )

        embed.add_field(name = "火",value = embedDefVal,inline = False) # フィールドを追加。
        embed.add_field(name = "水",value = embedDefVal,inline = False)
        embed.add_field(name = "土",value = embedDefVal,inline = False)
        embed.add_field(name = "風",value = embedDefVal,inline = False)
        embed.add_field(name = "光",value = embedDefVal,inline = False)
        embed.add_field(name = "闇",value = embedDefVal,inline = False)
        embed.add_field(name = "弱体",value = embedDefVal,inline = False)
        embed.add_field(name = "10飛ばし",value = embedDefVal,inline = False)
        embed.add_field(name = "自発可",value = embedDefVal,inline = False)
        embed.add_field(name = "募集取り消し",value = interaction.user.name,inline = False)
        #embedの送信
        await interaction.response.send_message(embed=embed)
        
        #インタラクションに関連付けられたメッセージの取得(ここではsendしたメッセージ)
        botMsg = await interaction.original_response()
        
        #取得したコメントに属性などのスタンプを送信
        await botMsg.add_reaction(hi)
        await botMsg.add_reaction(mizu)
        await botMsg.add_reaction(thuchi)
        await botMsg.add_reaction(kaze)
        await botMsg.add_reaction(hikari)
        await botMsg.add_reaction(yami)
        await botMsg.add_reaction('\N{BLACK DOWN-POINTING DOUBLE TRIANGLE}')
        await botMsg.add_reaction('\N{KEYCAP TEN}')
        await botMsg.add_reaction('\N{HEAVY LARGE CIRCLE}')

@client.tree.command(name="spbh", description="スパバハ募集用コマンド")
async def ping(interaction: discord.Integration,date:str="", comment:str=""):
    #name=クエスト名,date=日時,comment=コメント
        embed = discord.Embed( # Embedを定義する
                        title="SPBH",# タイトル　将来的にここにコメントのmessageを取得して編集して代入
                        color=0x00ff00, # フレーム色指定(今回は緑)
                        description="SPBHのマルチ募集です\n開始時間:"+date+"~\n"+comment, # Embedの説明文 必要に応じて
                        url="" # これを設定すると、タイトルが指定URLへのリンクになる
                        )
        embed.set_author(name=client.user, # Botのユーザー名
                    #url="", # titleのurlのようにnameをリンクにできる。botのWebサイトとかGithubとか
                    icon_url=client.user.display_avatar.url# Botのアイコンを設定してみる
                    )

        embed.add_field(name = "火",value = embedDefVal,inline = False) # フィールドを追加。
        embed.add_field(name = "水",value = embedDefVal,inline = False)
        embed.add_field(name = "土",value = embedDefVal,inline = False)
        embed.add_field(name = "風",value = embedDefVal,inline = False)
        embed.add_field(name = "光",value = embedDefVal,inline = False)
        embed.add_field(name = "闇",value = embedDefVal,inline = False)
        embed.add_field(name = "弱体",value = embedDefVal,inline = False)
        embed.add_field(name = "10飛ばし",value = embedDefVal,inline = False)
        embed.add_field(name = "自発可",value = embedDefVal,inline = False)
        embed.add_field(name = "募集取り消し",value = interaction.user.name,inline = False)
        #embedの送信
        await interaction.response.send_message(embed=embed)
        
        #インタラクションに関連付けられたメッセージの取得(ここではsendしたメッセージ)
        botMsg = await interaction.original_response()
        
        #取得したコメントに属性などのスタンプを送信
        await botMsg.add_reaction(hi)
        await botMsg.add_reaction(mizu)
        await botMsg.add_reaction(thuchi)
        await botMsg.add_reaction(kaze)
        await botMsg.add_reaction(hikari)
        await botMsg.add_reaction(yami)
        await botMsg.add_reaction('\N{BLACK DOWN-POINTING DOUBLE TRIANGLE}')
        await botMsg.add_reaction('\N{KEYCAP TEN}')
        await botMsg.add_reaction('\N{HEAVY LARGE CIRCLE}')

@client.tree.command(name="spbh_date", description="スパバハ放置狩りスケジュール調整")
async def spbhdate(interaction: discord.Integration,date:int, comment:str=""):
    await interaction.response.defer()
    #name=クエスト名,date=日時,comment=コメント
    nw_day = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    DoW = DayofWeek()
    DoW.day = date
    DoW.month = nw_day.month
    DoW.year = nw_day.year
    DoW.ZellerCount = DoW.Zeller()
    DoW.check = 0
    DoW.Count = 0
    if DoW.day > 28:
        DoW.checkMonth()

    d1 = DayofWeek()
    d2 = DayofWeek()
    d3 = DayofWeek()
    d4 = DayofWeek()
    d5 = DayofWeek()
    d6 = DayofWeek()
    d7 = DayofWeek()
    
    embed = discord.Embed( # Embedを定義する
                    title="スパバハ放置狩りスケジュール",# タイトル　将来的にここにコメントのmessageを取得して編集して代入
                    color=0xeae8e1, # フレーム色指定
                    description="スパバハの放置狩り日程合わせです\n"+comment, # Embedの説明文 必要に応じて
                    url="" # これを設定すると、タイトルが指定URLへのリンクになる
                    )
    embed.set_author(name=client.user, # Botのユーザー名
                #url="", # titleのurlのようにnameをリンクにできる。botのWebサイトとかGithubとか
                icon_url=client.user.display_avatar.url# Botのアイコンを設定してみる
                )
            
    for temp in [d1, d2, d3, d4, d5, d6, d7]:
        temp.day = DoW.day
        temp.month = DoW.month
        temp.ZellerCount = DoW.ZellerCount
        #元の日付を一日ずらして繰り上げ確認
        DoW.day += 1
        DoW.ZellerCount += 1
        DoW.Count += 1
        DoW.checkMonth()
    
    daylist = [d1, d2, d3, d4, d5, d6, d7]
    daylist = sorted(daylist, key=lambda x: x.ZellerCount % 7)
    
    #日曜処理
    embed.add_field(name =(f"{str(daylist[0].month)}/{str(daylist[0].day)} 日 22:00〜"),value = embedDefVal,inline = False)
    #月曜処理 
    embed.add_field(name =(f"{str(daylist[1].month)}/{str(daylist[1].day)} 月 22:00〜"),value = embedDefVal,inline = False)
    #火曜処理 
    embed.add_field(name =(f"{str(daylist[2].month)}/{str(daylist[2].day)} 火 22:00〜"),value = embedDefVal,inline = False)
    #水曜処理 
    embed.add_field(name =(f"{str(daylist[3].month)}/{str(daylist[3].day)} 水 22:00〜"),value = embedDefVal,inline = False)
    #木曜処理 
    embed.add_field(name =(f"{str(daylist[4].month)}/{str(daylist[4].day)} 木 22:00〜"),value = embedDefVal,inline = False)
    #金曜処理 
    embed.add_field(name =(f"{str(daylist[5].month)}/{str(daylist[5].day)} 金 22:00〜"),value = embedDefVal,inline = False)
    #土曜処理
    embed.add_field(name =(f"{str(daylist[6].month)}/{str(daylist[6].day)} 土 22:00〜"),value = embedDefVal,inline = False)

    #取り消し用フィールド(なくてもいいかも)
    embed.add_field(name = "募集取り消し",value = interaction.user.name,inline = False)
    #embedの送信
    await interaction.followup.send(embed=embed)
    
    #インタラクションに関連付けられたメッセージの取得(ここではfollowup.sendしたメッセージ)
    botMsg = await interaction.original_response()

    #曜日スタンプ送信
    await botMsg.add_reaction(getu)
    await botMsg.add_reaction(ka)
    await botMsg.add_reaction(sui)
    await botMsg.add_reaction(moku)
    await botMsg.add_reaction(kin)
    await botMsg.add_reaction(do)
    await botMsg.add_reaction(niti)

    #classの削除
    del DoW, d1, d2, d3, d4, d5, d6, d7

@client.event
#スタンプが追加されたときの処理
async def on_raw_reaction_add(payload) :

    #addではpayloadからmemberが取得できるけどremoveでは取れないので揃える為に
    #payload.user_idから取得
    guildObject = client.get_guild(payload.guild_id)
    memberObject = guildObject.get_member(payload.user_id)

    # channel_id から Channel オブジェクトを取得
    channel = client.get_channel(payload.channel_id)

    # 該当のチャンネル、BOT自身以外はスルー
    if memberObject.bot == True:
        return
    #message_idを元に編集対象のmessageオブジェクトを取得

    targetMessage = await channel.fetch_message(payload.message_id)
    
    #embed取得時にエラー吐くとエラーとして返す
    try :
        #対象のembedを取得(埋め込み)
        targetEmbeds = targetMessage.embeds[0]
    except :   
        print ("add_error")
        return
    
    #押したユーザの取得
    print (payload.member.name,"がスタンプ",payload.emoji.name,"を押しました/time",datetime.datetime.now().time())

    #スタンプが押された場合のスタンプ種類の認識
    if str(payload.emoji) == "<:hi:726379564816793600>" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 0
        targetFieldName = "火"
    elif str(payload.emoji) == "<:mizu:726379564791758848>" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 1
        targetFieldName = "水"
    elif str(payload.emoji) == "<:thuchi:726379564623724595>" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 2
        targetFieldName = "土"
    elif str(payload.emoji) == "<:kaze:726379564829245491>" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 3
        targetFieldName = "風"
    elif str(payload.emoji) == "<:hikari:726379564539838465>" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 4
        targetFieldName = "光"
    elif str(payload.emoji) == "<:yami:726379564502089780>" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 5
        targetFieldName = "闇"
    elif str(payload.emoji) == "\N{BLACK DOWN-POINTING DOUBLE TRIANGLE}" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 6
        targetFieldName = "弱体"
    elif str(payload.emoji) =="\N{KEYCAP TEN}" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 7
        targetFieldName = "ファラ役"
    elif str(payload.emoji) == "\N{HEAVY LARGE CIRCLE}" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 8
        targetFieldName = "自発可"
    elif str(payload.emoji) == "<:w_getu:1091758148622221472>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 1
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    elif str(payload.emoji) == "<:w_ka:1091758139902275745>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 2
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    elif str(payload.emoji) == "<:w_sui:1091758127906570291>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 3
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    elif str(payload.emoji) == "<:w_moku:1091758119345987664>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 4
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    elif str(payload.emoji) == "<:w_kin:1091758107450949744>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 5
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    elif str(payload.emoji) == "<:w_do:1091758168134131857>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 6
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    elif str(payload.emoji) == "<:w_niti:1091758158701150268>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 0
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    elif str(payload.emoji) == "\N{cross mark}" and targetEmbeds.fields[-1].value == memberObject.name:
        await targetMessage.delete() 
        return
    else:
        print("対象外のスタンプです")
        return

    #既存フィールドの確認
    if targetEmbeds.fields[targetFieldNum].value == "参加者は居ません":

        #参加者がいない場合はスタンプ押したユーザのみ追加 (.nameとすることでstrとして認識可能)
        editFieldValue = payload.member.name
    elif targetEmbeds.fields[targetFieldNum].value not in payload.member.name:
            editFieldValue = targetEmbeds.fields[targetFieldNum].value + "," + memberObject.name
    else:
        print(payload.member.name,"is already there.")
        return  
    
    #既存フィールドの編集 エラーの場合ログを吐いてreturn
    ####消すな####
    try :
        targetEmbeds.set_field_at(targetFieldNum, name=targetFieldName, value=editFieldValue, inline=False)
        await targetMessage.edit(embed=targetEmbeds)
    except :   
        print ("add_embed_error",datetime.datetime.now().time())
        return
    
@client.event
async def on_raw_reaction_remove(payload):

    #payloadからmember_id取得してgildに問い合わせしてmemberを取得
    guildObject = client.get_guild(payload.guild_id)
    memberObject = guildObject.get_member(payload.user_id)

    # channel_id から Channel オブジェクトを取得
    channel = client.get_channel(payload.channel_id)
    # 該当のチャンネル、BOT自身以外はスルー
    if memberObject.bot == True:
        return

    #message_idを元に編集対象のmessageオブジェクトを取得
    targetMessage = await channel.fetch_message(payload.message_id)

    #embed取得エラーでエラーと返す(対象外メッセージの除外)
    try:
        #対象のembedを取得(埋め込み)
        targetEmbeds = targetMessage.embeds[0]  
    except:
        print("remove_error")
        return
    
    print (memberObject.name,"がスタンプ",payload.emoji.name,"を取り消しました/time",datetime.datetime.now().time())

    #スタンプが押された場合のスタンプ種類の認識
    if str(payload.emoji) == "<:hi:726379564816793600>" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 0
        targetFieldName = "火"
    elif str(payload.emoji) == "<:mizu:726379564791758848>" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 1
        targetFieldName = "水"
    elif str(payload.emoji) == "<:thuchi:726379564623724595>" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 2
        targetFieldName = "土"
    elif str(payload.emoji) == "<:kaze:726379564829245491>" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 3
        targetFieldName = "風"
    elif str(payload.emoji) == "<:hikari:726379564539838465>" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 4
        targetFieldName = "光"
    elif str(payload.emoji) == "<:yami:726379564502089780>" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 5
        targetFieldName = "闇"
    elif str(payload.emoji) == "\N{BLACK DOWN-POINTING DOUBLE TRIANGLE}" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 6
        targetFieldName = "弱体"
    elif str(payload.emoji) =="\N{KEYCAP TEN}" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 7
        targetFieldName = "ファラ役"
    elif str(payload.emoji) == "\N{HEAVY LARGE CIRCLE}" and targetEmbeds.title != "スパバハ放置狩りスケジュール":
        targetFieldNum = 8
        targetFieldName = "自発可"
    elif str(payload.emoji) == "<:w_getu:1091758148622221472>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 1
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    elif str(payload.emoji) == "<:w_ka:1091758139902275745>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 2
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    elif str(payload.emoji) == "<:w_sui:1091758127906570291>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 3
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    elif str(payload.emoji) == "<:w_moku:1091758119345987664>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 4
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    elif str(payload.emoji) == "<:w_kin:1091758107450949744>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 5
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    elif str(payload.emoji) == "<:w_do:1091758168134131857>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 6
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    elif str(payload.emoji) == "<:w_niti:1091758158701150268>" and targetEmbeds.title == "スパバハ放置狩りスケジュール":
        targetFieldNum = 0
        targetFieldName = targetEmbeds.fields[targetFieldNum].name
    else:
        print("対象外のスタンプです")
        return
    

    #res = 現在スタンプを押してある名前の中から今回消した人の位置を左から数えた値を格納している
    #com = ","　がvalueの中に存在するかどうか確認している。
    res = targetEmbeds.fields[targetFieldNum].value.find(memberObject.name)
    com = targetEmbeds.fields[targetFieldNum].value.find(",")

    if res == 0:
        if com != -1:
        #,の文字数を数えて判断するif文
        #複数人中の1人目 ==
            editFieldValue = targetEmbeds.fields[targetFieldNum].value.replace(memberObject.name+",", '')
        elif com == -1:
            editFieldValue = embedDefVal
        else:
            print("searchError")
            return
    elif res != -1:
        #(複数)
        editFieldValue = targetEmbeds.fields[targetFieldNum].value.replace(","+memberObject.name, '')

    #エラーの場合ログを吐いてreturn
    try :
        targetEmbeds.set_field_at(targetFieldNum, name=targetFieldName, value=editFieldValue, inline=False)
        await targetMessage.edit(embed = targetEmbeds)

    except :   
        print ("remove_embed_error",datetime.datetime.now().time())
        return

client.run(TOKEN)

