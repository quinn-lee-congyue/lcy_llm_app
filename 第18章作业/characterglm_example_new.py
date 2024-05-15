import time
import os
from dotenv import load_dotenv
load_dotenv()

from api import get_characterglm_response


def characterglm_example():
    character_meta = {
        "user_info": "",
        "bot_info": "小杰，性别男，17岁，曾与父亲和去世的母亲生活在一起。小杰的头发为深棕色，身高175cm，体重68kg。小杰的名字是母亲给起的，寓意他将来能够杰出非凡。小杰平时喜欢穿深色衣服，以展现出他的成熟和稳重。小杰在高中期间表现出色，因此被北京大学提前录取。\n然而，小杰的生活并不顺利。在他的母亲去世后，父亲再婚，小杰因此有了一个继母和一个弟弟。继母对弟弟偏爱有加，而对待小杰则态度冷淡。在继母的请求下，小杰答应在高考中替弟弟作弊。不幸的是，他们的计划被发现了，小杰被抓到监狱，并判处了一年的刑期。\n在监狱里，小杰深刻反思了自己的行为，并下定决心，一旦出狱，他要重新开始，用自己的努力去实现曾经的梦想。",
        "user_name": "小杰的高中",
        "bot_name": "小杰"
    }
    messages = [
        {"role": "assistant", "content": "你为什么要来看我"},
        {"role": "user", "content": "（探监）我来看看你怎么样了～你说过要和我一起上北大，为什么要这么傻替弟弟替考？"}
    ]
    for chunk in get_characterglm_response(messages, meta=character_meta):
        print(chunk)
        time.sleep(0.5)


if __name__ == "__main__":
    characterglm_example()
