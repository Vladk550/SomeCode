#!C:\Python27\python.exe
# -*- coding: utf-8 -*-
import re


def from_json(json_string):
    json_string.strip()
    if json_string == '[]':
        return []
    elif json_string == '{}':
        return {}
    elif json_string == "null":
        return None
    elif json_string == "":
        return ""
    elif re.match("[\"\'].*[\"\']", json_string):
        return json_string[1:-1]
    elif json_string in ('true', 'false'):
        return json_string == 'true'
    elif re.match("\[.+\]", json_string):
        json_string = json_string[1:-1] + ","
        l = r = 0
        lst = []
        count = 0
        for ch in json_string:
            if ch in ('{', '['):
                count += 1
            elif ch in ('}', ']'):
                count -= 1
            elif ch == ',' and count == 0:
                lst.append(from_json(json_string[l: r]))
                l = r + 2
            r += 1
        return lst
    elif re.match("^{.+}$", json_string):
        json_string = json_string[1:-1] + ','
        count = 0
        l = r = 0
        dct = {}
        for ch in json_string:
            if ch in ('{', '['):
                count += 1
            elif ch in ('}', ']'):
                count -= 1
            elif ch == ',' and count == 0:
                st = json_string[l:r].split(':', 1)
                dct[from_json(st[0])] = from_json(st[1])
                l = r + 2
            r += 1
        return dct
    try:
        n = int(json_string)
    except:
        n = float(json_string)
    return n

if __name__ == "__main__":
    print type(from_json('{"popa":"Nice", "kisa":{"whose":"My", "colors":[1, 2, 3], "fur":null}, "inds":[1, true, 12], "size":32}'))
    print from_json('[1, null, {"a": 1}]')