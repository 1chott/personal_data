import re

# buf = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", "<a><b>hello</b></a>").group()
buf = re.match(r"<(?P<mike>\w*)><(?P<python>\w*)>.*</(?P=python)></(?P=mike)>", "<a><b>hello</b></a>").group()
print(buf)