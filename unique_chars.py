#!/usr/bin/env python3

def has_only_unique_char(inp_str):
    for i, c in enumerate(inp_str):
        if c in inp_str[:i]:
            return False

    return True


exp = [True, False, True, False]
inp = ['abc', 'abcda', 'zxcvbn', 'xx']

for i in range(len(inp)):
    tmp = has_only_unique_char(inp[i])
    assert exp[i] == tmp, f'Why has_only_unique_char({inp[i]}) == {has_only_unique_char(inp[i])}'
    print(inp[i], '--->', tmp)