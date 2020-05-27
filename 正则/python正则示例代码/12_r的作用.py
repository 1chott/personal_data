import re

# r, raw原生字符串

# 2个\代表1个\
path = "C:\\Users\\superman\\Desktop\\code\\python\\11期\\9day"

# 2个\代表1个，4个才能匹配上上面的2个
# result = re.match("C:\\\\Users\\\\superman\\\\Desktop\\\\code\\\\python\\\\11期\\\\9day", path)
result = re.match(r"C:\\Users\\superman\\Desktop\\code\\python\\11期\\9day", path)
print(result.group())