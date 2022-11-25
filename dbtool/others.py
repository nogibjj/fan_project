from decimal import Decimal
from collections import defaultdict
import re
import os


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


def calculateRel(data):
    """
    calculate the sender, receiver from records
    data: array of Money records
    return: array of relationship (sender, receiver, amount)
    """
    total = 0
    h = defaultdict(int)
    for _, _, name, target, _, amt in data:
        if target != "all":
            target = target.split(",")
            for t in target:
                h[t.strip()] += amt / Decimal(len(target))
        else:
            total += amt
        h[name] -= amt
    for k, val in h.items():
        h[k] += total / Decimal(len(h))
    calres = []
    cur = [[v, k] for k, v in h.items()]
    cur.sort()
    left, right = 0, len(cur) - 1
    calres = []
    while left < right:
        if cur[left][0] == 0:
            left += 1
        elif cur[right][0] == 0:
            right -= 1
        else:
            val = min(abs(cur[left][0]), abs(cur[right][0]))
            cur[left][0] += val
            cur[right][0] -= val
            calres.append([cur[right][1], cur[left][1], abs(val)])
    return calres


def deleteFileRegex(code, dirpath):
    for file_path, _, file_name_list in os.walk(dirpath):
        for file_name in file_name_list:
            m = r".*_{code}.*".format(code=code)
            if re.match(m, file_name):
                os.remove(file_path + file_name)
