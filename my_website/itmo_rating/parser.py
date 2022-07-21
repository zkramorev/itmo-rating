import requests
import json
from fake_useragent import UserAgent
from datetime import datetime
from typing import Union


def get_update_time_from_string(date_time: str) -> datetime:
    return datetime.fromisoformat(date_time)


def parsing() -> Union[dict[str, int], str, int]:
    headers = {"user-agent": UserAgent().random,
                "x-requested-with": "XMLHttpRequest"}
    url = "https://abitlk.itmo.ru/api/v1/"\
            "9e2eee80b266b31c8d65f1dd3992fa26eb8b4c118ca9633550889a8ff2cac429/"\
            "rating/bachelor/contract?program_id=15999&manager_key="

    response = requests.get(url=url, headers=headers).json()
    #with open("my_website/itmo_rating/page.json", "w", encoding="UTF-8") as file:
        #json.dump(response, file)

    with open("my_website/itmo_rating/page.json", 'r', encoding='UTF-8') as file:  
        data = json.load(file)  



    # спсики: общий, есть оригиналы документов и согласия, только оригиналы, только согласие, ничего
    common = list()
    original_agreement = list()
    original = list()
    agreement = list()
    nothing = list()
    my_snils = "18868033624"
    my_position = 0
    for item in data["result"]["items"]:
        common.append(item["position"])
        position = item["position"]
        if item["snils"] == my_snils:
            my_position = position
        if item["send_agreement"] and item["is_send_original"]:
            original_agreement.append(position)
        elif item["send_agreement"]: 
            agreement.append(position)
        elif item["is_send_original"]:
            original.append(position)
        else:
            nothing.append(position)


    # место в общем рейтинге
    common_position = common.index(my_position) + 1

    # место в рейтинге с иключением (нет:нет)
    common_set = set(common)
    common_set.difference_update(nothing)
    whithout_nothing = sorted(list(common_set))
    whithout_nothing_position = whithout_nothing.index(my_position) + 1

    # место в рейтинге только с (да:да)
    original_agreement_position = original_agreement.index(my_position) + 1

    # место в рейтинге с (да: да) и (да: нет)
    original_agreement_set = set(original_agreement)
    original_agreement_set.update(set(agreement))
    original_agreement_or_agreement_position = \
        sorted(list(original_agreement_set)).index(my_position) + 1

    # место в рейтинге с (да: да) и (нет: да)
    original_agreement_set = set(original_agreement)
    original_agreement_set.update(set(original))
    original_agreement_or_original_position = \
        sorted(list(original_agreement_set)).index(my_position) + 1


    information = {
        "<span>Все</span> заявления": 
                common_position,
        "<span>Кроме</span> тех, кто <span>без</span> согласия <span>и без</span> оригиналов": 
                whithout_nothing_position,
        "<span>Только с</span> согласием <span>и с</span> оригиналами": 
                original_agreement_position,
        "<span>Всё</span> <span>или</span> <span>только</span> согласие": 
                original_agreement_or_agreement_position,
        "<span>Всё</span> <span>или только</span> оригиналы": 
                original_agreement_or_original_position
                }
    update_time = get_update_time_from_string(data["result"]["update_time"]).strftime("%m/%d/%Y, %H:%M:%S")
    count_statements = len(common)
    return information, update_time, count_statements
