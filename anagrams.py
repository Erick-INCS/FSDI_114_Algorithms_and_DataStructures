#!/usr/bin/env python3
""" Checks whether two words are anagrams """


class Counter:
    """ Count characters """
    def __init__(self, init_map=None):
        self.data = {} if not init_map else init_map

    def update(self, char):
        """ Update the counter data """
        if char not in self.data:
            self.data[char] = 1
        else:
            self.data[char] += 1

    def __getitem__(self, item):
        return self.data[item]


def anagram_checker(word1, word2):
    """ checker """
    if len(word1) != len(word2):
        return False

    c_w1, c_w2 = Counter(), Counter()

    for i in range(len(word1)):
        if word1[i] not in word2:
            return False
        c_w1.update(word1[i])
        c_w2.update(word2[i])

    for i in c_w1.data:
        if c_w1[i] != c_w2[i]:
            return False

    return True


if __name__ == '__main__':
    a_ok = ["star", 'race', 'part', 'heart', 'knee']
    b_ok = ["rats", 'care', 'trap', 'earth', 'keen']
    a_fail = ["sar", 'raze', 'part', 'hear', 'keanu']
    b_fail = ["rats", 'care', 'trapo', 'then', 'reeves']

    expected = [True] * len(a_ok) + [False] * len(a_fail)
    words = [
            a_ok + a_fail,
            b_ok + b_fail
            ]

    for i in range(len(words[0])):
        current = anagram_checker(words[0][i], words[1][i])
        print(f'Anagram("{words[0][i]}", "{words[1][i]}") = {current}')
        assert current == expected[i]

    print('\n\t', len(expected), 'tests passed!.')
