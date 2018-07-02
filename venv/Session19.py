import re

def regExDemo():
    quote = "Search the candle rather than cursing the darkness"
    # result = re.match(r"the",quote)
    result = re.match(r"Search",quote)
    print(result)
    print(type(result))
    print(result.start())
    print(result.end())
    print("-------")
    result = re.search(r"the",quote)
    print(result)
    print(result.group(0))
    print("-------")
    result = re.findall(r"the",quote)
    print(result)
    print("-------")
    result = re.split(r"the",quote)
    print(result)
    print(type(result))
    print("-------")
    # result = re.sub(r"the","a", quote)
    # print(result)
    print("-------")
    pattern = re.compile("the")
    result = pattern.findall(quote)
    print(type(pattern))
    print(result)

# Pattern Examples
quote = "Work hard and Get Luckier"
result = re.findall(r".",quote)
print(result)
print("===============")

result = re.findall(r"\w",quote)
print(result)
print("===============")

result = re.findall(r"\w*",quote)
print(result)

print("===============")

result = re.findall(r"\w+",quote)
print(result)


email = "john@example.com"
# email = "@."
password = "john@123"
phone = "+91 99155 71177"

# Use Regular Expressions to check if the
# email and phone number is correctly written or not

# Split csv data using regEx Pattern
# Detect CSV is correctly formed or not
# Validate Email,Password and Phone using regEx
