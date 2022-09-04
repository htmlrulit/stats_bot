import asyncio
import pandas as pd
import json
import requests
from vkbottle.bot import Bot, Message
from vkbottle import API
import os
from datetime import datetime, timedelta
import pytz
import requests
import xmltodict
bot = Bot(token="main_token")
api = API("main_token")
class VkStatsChecker:

    def __init__(self):
        self.token = ""

    def addToken(self, token : str):
        self.token = token

    def parse_cfg(self, cfg_name='test.xml'):
        cfg_path = os.path.join(os.getcwd(),cfg_name)
        with open(cfg_path) as xmlconf:
            conf = xmltodict.parse(xmlconf.read())
            api_token = conf['settings']['account']['token']
            api_version = conf['settings']['api']['version']
        return api_token, api_version

    def check_stats(self, group_id : int, timestamp_from : int, timestamp_to : int, api_ver : str):
        r = requests.get("https://api.vk.com/method/stats.get", params={"group_id": group_id,
                                                                         "timestamp_from": timestamp_from,
                                                                         "timestamp_to": timestamp_to,
                                                                         "stats_groups": "reach",
                                                                         "access_token": self.token,
                                                                         "v": api_ver})
        stats_res = r.json()
        activity_by_day = stats_res["response"][1]["activity"]
        subs_by_day = 0
        unsubs_by_day = 0
        if "subscribed" in activity_by_day:
            subs_by_day = activity_by_day["subscribed"]
        if "unsubscribed" in activity_by_day:
            unsubs_by_day = activity_by_day["unsubscribed"]
        return subs_by_day, unsubs_by_day

def main():
    BASE_CFG_NAME: str = "config.xml"
    DATE_TODAY : datetime = datetime.now(pytz.utc)
    DATE_YESTERDAY = DATE_TODAY - timedelta(days=1)

    vk_stats_checker = VkStatsChecker()
    api_token, api_ver = vk_stats_checker.parse_cfg(BASE_CFG_NAME)
    vk_stats_checker.addToken(api_token)
    timestamp_today = int(round(DATE_TODAY.timestamp()))
    timestamp_yesterday = int(round(DATE_YESTERDAY.timestamp()))
    subs_by_day, unsubs_by_day = vk_stats_checker.check_stats(169782389, timestamp_from=timestamp_yesterday, timestamp_to=timestamp_today, api_ver=api_ver)
    print(f"Subscribed by day: {subs_by_day} ; Unsubscribed by day: {unsubs_by_day}")
    solved = (subs_by_day-unsubs_by_day)
    print(f"Подписалось: {subs_by_day}\nОтписалось: {unsubs_by_day}\nИтог: {solved}")

@bot.on.message(text="test")
async def hi_handler(message: Message):
    BASE_CFG_NAME: str = "config.xml"
    DATE_TODAY : datetime = datetime.now(pytz.utc)
    DATE_YESTERDAY = DATE_TODAY - timedelta(days=1)
    vk_stats_checker = VkStatsChecker()
    api_token, api_ver = vk_stats_checker.parse_cfg(BASE_CFG_NAME)
    vk_stats_checker.addToken(api_token)
    timestamp_today = int(round(DATE_TODAY.timestamp()))
    timestamp_yesterday = int(round(DATE_YESTERDAY.timestamp()))

    subs_by_day, unsubs_by_day = vk_stats_checker.check_stats(169782389, timestamp_from=timestamp_yesterday, timestamp_to=timestamp_today, api_ver=api_ver)
    solved_1 = (subs_by_day-unsubs_by_day)
    subs_group_1 = subs_by_day
    unsubs_group_1 = unsubs_by_day

    subs_by_day, unsubs_by_day = vk_stats_checker.check_stats(192882538, timestamp_from=timestamp_yesterday, timestamp_to=timestamp_today, api_ver=api_ver)
    subs_group_2 = subs_by_day
    unsubs_group_2 = unsubs_by_day
    solved_2 = (subs_by_day-unsubs_by_day)

    subs_by_day, unsubs_by_day = vk_stats_checker.check_stats(198943951, timestamp_from=timestamp_yesterday, timestamp_to=timestamp_today, api_ver=api_ver)
    subs_group_4 = subs_by_day
    unsubs_group_4 = unsubs_by_day
    solved_4 = (subs_by_day-unsubs_by_day)

    subs_by_day, unsubs_by_day = vk_stats_checker.check_stats(122159973, timestamp_from=timestamp_yesterday, timestamp_to=timestamp_today, api_ver=api_ver)
    subs_group_5 = subs_by_day
    unsubs_group_5 = unsubs_by_day
    solved_5 = (subs_by_day-unsubs_by_day)

    subs_by_day, unsubs_by_day = vk_stats_checker.check_stats(197660967, timestamp_from=timestamp_yesterday, timestamp_to=timestamp_today, api_ver=api_ver)
    subs_group_6 = subs_by_day
    unsubs_group_6 = unsubs_by_day
    solved_6 = (subs_by_day-unsubs_by_day)

    subs_by_day, unsubs_by_day = vk_stats_checker.check_stats(192248306, timestamp_from=timestamp_yesterday, timestamp_to=timestamp_today, api_ver=api_ver)
    subs_group_7 = subs_by_day
    unsubs_group_7 = unsubs_by_day
    solved_7 = (subs_by_day-unsubs_by_day)

    subs_by_day, unsubs_by_day = vk_stats_checker.check_stats(161405371, timestamp_from=timestamp_yesterday, timestamp_to=timestamp_today, api_ver=api_ver)
    subs_group_8 = subs_by_day
    unsubs_group_8 = unsubs_by_day
    solved_8 = (subs_by_day-unsubs_by_day)

    subs_by_day, unsubs_by_day = vk_stats_checker.check_stats(195941389, timestamp_from=timestamp_yesterday, timestamp_to=timestamp_today, api_ver=api_ver)
    subs_group_9 = subs_by_day
    unsubs_group_9 = unsubs_by_day
    solved_9 = (subs_by_day-unsubs_by_day)

    subs_by_day, unsubs_by_day = vk_stats_checker.check_stats(176449226, timestamp_from=timestamp_yesterday, timestamp_to=timestamp_today, api_ver=api_ver)
    subs_group_10 = subs_by_day
    unsubs_group_10 = unsubs_by_day
    solved_10 = (subs_by_day-unsubs_by_day)


    subs_all = (subs_group_1+subs_group_2+subs_group_4+subs_group_5+subs_group_6+subs_group_7+subs_group_8+subs_group_9+subs_group_10)
    unsubs_all = (unsubs_group_1+unsubs_group_2+unsubs_group_4+unsubs_group_5+unsubs_group_6+unsubs_group_7+unsubs_group_8+unsubs_group_9+unsubs_group_10)
    solved_all = (solved_1+solved_2+solved_4+solved_5+solved_6+solved_7+solved_8+solved_9+solved_10)

    users_info = await bot.api.users.get(message.from_id)
    await message.answer(f"@oboi_bot (01): ✅ {subs_group_1}    ⛔ {unsubs_group_1} 📊 {solved_1}\n@my_lovemur (02): ✅ {subs_group_2} ⛔ {unsubs_group_2} 📊 {solved_2}\n@went_out_for__a__smoke (03): ✅ {subs_group_4}    ⛔ {unsubs_group_4} 📊 {solved_4}\n@dai_love (04): ✅ {subs_group_5}    ⛔ {unsubs_group_5} 📊 {solved_5}\n@smoked_and_died (05): ✅ {subs_group_6}    ⛔ {unsubs_group_6} 📊 {solved_6}\n@soxratop4ek (06): ✅ {subs_group_7}    ⛔ {unsubs_group_7} 📊 {solved_7}\n@poshlyamolly (07): ✅ {subs_group_8}    ⛔ {unsubs_group_8} 📊 {solved_8}\n@sad_quotes1231 (08): ✅ {subs_group_9}    ⛔ {unsubs_group_9} 📊 {solved_9}\n@notethereal (09): ✅ {subs_group_10}    ⛔ {unsubs_group_10} 📊 {solved_10}\n\n✅{subs_all}    ⛔{unsubs_all} 📊{solved_all}")

if __name__ == "__main__":
    main()

bot.run_forever()