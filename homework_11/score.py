def score():
    import combo
    combo, wheel = combo.combo()
    for value in combo:
        if combo.count(value) == 3:
            return wheel.get(value) * 10
        elif combo.count(value) == 2 and 'XXX' in combo:
            return wheel.get(value) * 2
        elif combo.count(value) == 2 and not 'XXX' in combo:
            return wheel.get(value)
        return 0
