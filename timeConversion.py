def timeConversion(s):
    hh = s[0:2]
    if "AM" in s:
        if hh == "12":
            hh = "00"
        mm = s[3:5]
        ss = s[6:8]
        print(hh + ":" + mm + ":" + ss)
    
    if "PM" in s:
        if hh == "12":
            mm = s[3:5]
            ss = s[6:8]
            print(str(hh) + ":" + mm + ":" + ss)
        else:
            hh = int(hh) + 12
            mm = s[3:5]
            ss = s[6:8]
            print(str(hh) + ":" + mm + ":" + ss)

timeConversion("07:05:45AM")
timeConversion("12:05:45AM")
timeConversion("12:05:45PM")
timeConversion("11:59:59PM")
timeConversion("12:45:54PM")
