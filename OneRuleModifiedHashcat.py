rules = open("OneRuleModifiedHashcatTemplate", 'r')
new = open("OneRuleModifiedHashcat.rule", 'w')

while (True):
    rule = rules.readline().strip(chr(10))
    print(rule)
    if (rule == ""):
        break

    i1 = 0
    i2 = 0
    i3 = 0
    i4 = 0

    while (i1 < 10):
        new.write(rule + '$' + chr(i1+48) + '$' + chr(i2+48) + '$' + chr(i3+48) + '$' + chr(i4+48) + '\n')

        i4 += 1
        if (i4 == 10):
            i4 = 0
            i3 += 1
        if (i3 == 10):
            i3 = 0
            i2 += 1
        if (i2 == 10):
            i2 = 0
            i1 += 1

rules.close()
new.close()
