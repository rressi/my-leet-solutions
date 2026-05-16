"""
You are given a string s and an array of strings words. All the strings of words
are of the same length.

A concatenated string is a string that exactly contains all the strings of any 
permutation of words concatenated.

- For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef",
  "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a
  concatenated string because it is not the concatenation of any permutation of
  words.
  Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Reference: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
"""

from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        orig_words: Counter = Counter(words)
        cur_words: Counter | None = None
        results: list[int] = []

        n: int = len(words[0])
        i: int = 0
        candidate_i: int = 0
        while i <= len(s) - n:
            candidate: str = s[i:i + n]
            if cur_words is None:
                match orig_words.get(candidate, 0):
                    case 0:
                        i += 1
                    case 1:
                        cur_words = orig_words.copy()
                        cur_words.pop(candidate)
                        if not cur_words:
                            results.append(i)
                            cur_words = None
                        candidate_i = i
                        i += n
                    case _:
                        cur_words = orig_words.copy()
                        cur_words[candidate] -= 1
                        candidate_i = i
                        i += n
            else:
                match cur_words.get(candidate, 0):
                    case 0:
                        cur_words = None
                        i = candidate_i + 1
                    case 1:
                        cur_words.pop(candidate)
                        if cur_words:
                            i += n
                        else:
                            results.append(candidate_i)
                            cur_words = None
                            i = candidate_i + 1
                    case _:
                        cur_words[candidate] -= 1
                        i += n

        return results


def test_solution() -> None:
    sol = Solution()

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    assert sol.findSubstring(s=s, words=words) == []

    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    assert sol.findSubstring(s=s, words=words) == [0, 9]

    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    assert sol.findSubstring(s=s, words=words) == [6, 9, 12]


if __name__ == "__main__":
    test_solution()
