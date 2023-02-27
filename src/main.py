import discord
import datetime
from discord.ext import commands
from discord import app_commands

#discordpy の機能で一部イベントの受け取り・スルーを制御できる=>通信量の削減
intents = discord.Intents.all()  # デフォルトのIntentsオブジェクトを生成
intents.typing = False  # typingを受け取らないように
GUILD_ID = discord.Object(id=727849192361558080)

class Myclient(discord.Client):
    def __init__(self, intents: discord.Intents):
        super().__init__(
            
            intents=intents)

        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=GUILD_ID)
        await self.tree.sync(guild=GUILD_ID)


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
fara = ":shield:"
maru = ":o:"
batu = "cross mark"

#embedのVal定義
embedDefVal = "参加者は居ません"

#BOT動作に必要な定数


TOKEN = 

@client.event
async def on_ready():
    #起動後PC側にメッセージ送信
    print(datetime.datetime.now().time(),"on_ready/discordVer",discord.__version__)
    await client.change_presence(activity=discord.Activity(name="マルチ募集,name,time,comment" ,type = discord.ActivityType.playing))


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
        embed.add_field(name = "ファラ役",value = embedDefVal,inline = False)
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
        await botMsg.add_reaction('\N{SHIELD}')
        await botMsg.add_reaction('\N{HEAVY LARGE CIRCLE}')


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
    if str(payload.emoji) == "<:hi:726379564816793600>":
        targetFieldNum = 0
        targetFieldName = "火"
    elif str(payload.emoji) == "<:mizu:726379564791758848>":
        targetFieldNum = 1
        targetFieldName = "水"
    elif str(payload.emoji) == "<:thuchi:726379564623724595>":
        targetFieldNum = 2
        targetFieldName = "土"
    elif str(payload.emoji) == "<:kaze:726379564829245491>":
        targetFieldNum = 3
        targetFieldName = "風"
    elif str(payload.emoji) == "<:hikari:726379564539838465>":
        targetFieldNum = 4
        targetFieldName = "光"
    elif str(payload.emoji) == "<:yami:726379564502089780>":
        targetFieldNum = 5
        targetFieldName = "闇"
    elif str(payload.emoji) == "\N{BLACK DOWN-POINTING DOUBLE TRIANGLE}":
        targetFieldNum = 6
        targetFieldName = "弱体"
    elif str(payload.emoji) =="\N{SHIELD}":
        targetFieldNum = 7
        targetFieldName = "ファラ役"
    elif str(payload.emoji) == "\N{HEAVY LARGE CIRCLE}":
        targetFieldNum = 8
        targetFieldName = "自発可"
    elif str(payload.emoji) == "\N{cross mark}" and targetEmbeds.fields[9].value == memberObject.name:
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
    if str(payload.emoji) == "<:hi:726379564816793600>":
        targetFieldNum = 0
        targetFieldName = "火"
    elif str(payload.emoji) == "<:mizu:726379564791758848>":
        targetFieldNum = 1
        targetFieldName = "水"
    elif str(payload.emoji) == "<:thuchi:726379564623724595>":
        targetFieldNum = 2
        targetFieldName = "土"
    elif str(payload.emoji) == "<:kaze:726379564829245491>":
        targetFieldNum = 3
        targetFieldName = "風"
    elif str(payload.emoji) == "<:hikari:726379564539838465>":
        targetFieldNum = 4
        targetFieldName = "光"
    elif str(payload.emoji) == "<:yami:726379564502089780>":
        targetFieldNum = 5
        targetFieldName = "闇"
    elif str(payload.emoji) == "\N{BLACK DOWN-POINTING DOUBLE TRIANGLE}":
        targetFieldNum = 6
        targetFieldName = "弱体"
    elif str(payload.emoji) == "\N{SHIELD}":
        targetFieldNum = 7
        targetFieldName = "ファラ役"
    elif str(payload.emoji) == "\N{HEAVY LARGE CIRCLE}":
        targetFieldNum = 8
        targetFieldName = "自発可"
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

