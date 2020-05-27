import re

# 需求：匹配出，一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无。

buf = ["A", "Aaaa", "AAAA", "Abc", "AaaB", "A12325"]

for tmp in buf:
    # print(tmp)
    result = re.match(r"[A-Z][a-z]*$", tmp)
    if result:
        print(result.group(), "符合要求")
    else:
        print(tmp, "不符合要求")
