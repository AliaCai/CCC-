icu = {"CU": "see you",
       ":-)": "I'm happy ",
       ":-(": "I'm unhappy",
       ";-)": "wink",
       ":-P": "stick out my tongue",
       "(~.~)": "sleepy",
       "TA": "totally awesome",
       "CCC": "Canadian Computing Competition",
       "CUZ": "because",
       "TY": "thank-you",
       "YW": "you're welcome",
       "TTYL": "talk to you later"
       }

while True:
    q = input("");
    if q == "CU" or q == ":-)" or q == ":-(" or q == ";-)" or q == ":-P" or q == "(~.~)" or q == "TA" or q == "CCC" or q == "CUZ" or q == "TY" or q == "YW" or q == "TTYL":
        print(icu[q])
    else:
        print(q)
    if q == "TTYL":
        break









