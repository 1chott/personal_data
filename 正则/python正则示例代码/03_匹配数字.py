import re

# 需求：匹配出，0到99之间的数字, 不是个位数的，不能以0开头

buf = ["56", "09", "1", "19", "778"]

for tmp in buf:
    # print(tmp)
    #result = re.match(r"\d{1,2}$", tmp)
    # result = re.match(r"[0-9]{1,2}$", tmp)
    # result = re.match(r"\d?\d", tmp)
    # [1-9]?可有可无，发现0不符合要求，[1-9]?不要，匹配下一个字符\d, 0是符合要求的，取了0
    # result = re.match(r"[1-9]?\d", tmp)
    result = re.match(r"[1-9]?\d$", tmp)
    if result:
        print(result.group(), "符合要求")
    else:
        print(tmp, "不符合要求")