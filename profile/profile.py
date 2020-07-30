from hama.tagging import tag
from hama.tagging.dict import Dict

print(tag("a다르고 uh다르다", zipped=True))

dict = Dict()
dict.load()
print(dict.query("자동차"))
