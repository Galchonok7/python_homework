proc = 1
while proc < 100:
    if proc > 4:
        word = 'процентов'
    else:
        if proc != 1:
            word = 'процента'
        else:
            word = 'процент'
    print(proc, word)
    proc = proc + 1

