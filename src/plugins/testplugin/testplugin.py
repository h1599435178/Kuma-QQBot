import httpx
import nonebot.exception
import requests
from nonebot import on_command, on_regex, Bot, on_notice
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.params import CommandArg


testmmm = on_command("你好",rule=to_me(), aliases={"hello","/你好"})


@testmmm.handle()
async def _(message: Message = CommandArg()):
    if any((not seg.is_text()) or str(seg) for seg in message):
        await testmmm.send("nihao!")
