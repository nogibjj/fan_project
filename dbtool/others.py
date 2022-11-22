def beautify(res):
    s = []
    for _, index, name, target, item, amt in res:
        s.append(
            str(index)
            + ": "
            + name
            + " pay "
            + target
            + " "
            + str(amt)
            + " for "
            + item
        )
    return s
