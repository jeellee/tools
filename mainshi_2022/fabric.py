# --*-- coding: utf-8 --*--
"""
递归需要出口条件，也就是你说的停止。。

一般情况在递归内部需要一个分支判断，如：

def fab(n):
  if n<2:
    return 1
  else
    return fab(n-1)+fab(n-2)
递归一定次数以后达到上面的if条件，递归就结束了。

"""


def check_unicode(data):
    """
    多层递归循环, 需要判断退出条件(按)
    所以需要 检查为True的时候退出,
    if check_unicode(v):
        return True

    和的退出条件相同
    if v and isinstance(v, unicode):
        return True
    :param data:
    :return:
    """
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, dict):
                if check_unicode(v):
                    return True
            elif isinstance(v, list):
                if check_unicode(v):
                    return True
            else:
                if v and isinstance(v, str):
                    return True
    elif isinstance(data, list):
        for v in data:
            if isinstance(v, dict):
                if check_unicode(v):
                    return True
            elif isinstance(v, list):
                if check_unicode(v):
                    return True
            else:
                if v and isinstance(v, str):
                    return True
    else:
        if data and isinstance(data, str):
            return True
    return False


data = {
    "cur_page": 0,
    "top": [
      {
        "name": "机智阿黛儿",
        "combat": 707604,
        "level": 1,
        "title_id": 0,
        "parise_flag": False,
        "rank": 1,
        "guild_name": "",
        "role": 209402,
        "uid": "robot_1"
      },
      {
        "name": "自大亚伯",
        "combat": 707604,
        "level": 1,
        "title_id": 0,
        "parise_flag": False,
        "rank": 2,
        "guild_name": "",
        "role": 209402,
        "uid": "robot_2"
      },
    ],
    "like_times": 0,
    "max_like_times": 10,
    "self_rank": 0,
    "self_score": '打',
  }


print(check_unicode(data))

