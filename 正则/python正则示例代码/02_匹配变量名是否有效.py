import re

# 需求：匹配变量名是否有效
# 不能以数字开头，以后的组合为字母，数字，下划线

buf = [" A", "Aaaa", "9AAAA", "A bc", "_AaaB", "A12325 aa"]

for tmp in buf:
    # print(tmp)
    # result = re.match(r"\D\w*$", tmp)
    # [^a]  取反，只要不是a都可以
    # ^a: 以a开头
    result = re.match(r"^[a-zA-Z_]\w*$", tmp)
    if result:
        print(result.group(), "符合要求")
    else:
        print(tmp, "不符合要求")