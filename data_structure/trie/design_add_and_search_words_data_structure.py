# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie

        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]

        cur["."] = ""

    def search(self, word: str) -> bool:
        def helper(node, index):
            if index == len(word):
                return "." in node

            if word[index] == ".":
                for new in node.values():
                    if new == "":
                        continue
                    if helper(new, index+1):
                        return True
                return False

            else:
                if word[index] not in node:
                    return False

                return helper(node[word[index]], index+1)

        return helper(self.trie, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
