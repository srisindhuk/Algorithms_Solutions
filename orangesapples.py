def countApplesAndOranges(s, t, appletreepos, orangetreepos, fallapplespos, fallorangespos):
    applecount = 0
    orangecount = 0
    applecount = 0
    orangecount = 0
    if s > appletreepos and orangetreepos > t and t > s:
        for apples in fallapplespos:
            if s <= appletreepos + apples and appletreepos + apples <= t:
                applecount += 1

        for oranges in fallorangespos:
            if s <= orangetreepos + oranges and orangetreepos + oranges <= t:
                orangecount += 1

    print(applecount)
    print(orangecount)


s=2
t=3
a=1
b=1
apples=[2]
oranges=[-2]
countApplesAndOranges(s, t, a, b, apples, oranges)
