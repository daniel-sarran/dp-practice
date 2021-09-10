"""
>>> all_construct('hello', ['cat', 'dog', 'mouse'])
[]
Empty array means there are no ways to construct our target.

>>> all_construct('', ['cat', 'dog', 'mouse'])
[[]]
Can construct empty string with no choices

>>> all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])


                abcdef
        ab      abc     abcd
        'cdef'   'def'    'ef'

    cd  def     def     ef


"""


def all_construct(target, word_bank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    # If we've created the target the problem is trivially solved
    if not target:
        return [[]]

    result = []

    for word in word_bank:
        # check if word is a prefix
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank, memo)
            target_ways = list(map(lambda way: [word] + way, suffix_ways))
            result.extend(target_ways)

    memo[target] = result
    return result


if __name__ == '__main__':
    print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(all_construct(
        'abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
    print(all_construct('aaaaaaaaaaaaaaaz', [
          'a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
