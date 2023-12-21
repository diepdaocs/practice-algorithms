from collections import defaultdict
from typing import List, Dict


class Node:
    def __init__(self, char):
        self.char = char
        self.is_word = False
        self.word = ''
        self._children: Dict[str, Node] = {}

    def get_children(self, c):
        return self._children.get(c)

    def add_children(self, c, node):
        self._children[c] = node

    def children(self):
        return self._children


class Trie:
    def __init__(self, words):
        self.tree: Node = self._build_tree(words)

    @staticmethod
    def _build_tree(words):
        root = Node('')
        for w in words:
            node = root
            for c in w:
                child = node.get_children(c)
                if not child:
                    child = Node(c)
                    node.add_children(c, child)

                node = child

            node.word = w
            node.is_word = True

        return root

    def prefix_search(self, prefix):
        node = self.tree
        for c in prefix:
            node = node.get_children(c)
            if not node:
                return []

        return self._node_words(node)

    def _node_words(self, node):
        words = []

        if node.is_word:
            words.append(node.word)

        for child in node.children().values():
            words.extend(self._node_words(child))

        return words


class StreamFilter:
    def __init__(self, keywords: List[str]):
        self.ngrams = self._build_ngrams(keywords)

    @staticmethod
    def _build_ngrams(keywords):
        result = defaultdict(list)
        for kw in keywords:
            n = len(kw)
            for i in range(1, n + 1):
                ngram = kw[:i]
                result[ngram].append(kw)

        return result

    # Time Complexity: O(1)
    # Space Complexity: O(n^2)
    def search(self, prefix):
        return self.ngrams.get(prefix, [])


def main():
    keywords = ['abcd', 'abc', 'ab', 'def', 'defg', 'a', 'de']

    stream_filter = StreamFilter(keywords)
    matches = stream_filter.search('ab')
    assert matches == ['abcd', 'abc', 'ab']
    assert stream_filter.search('abcd') == ['abcd']
    assert stream_filter.search('de') == ['def', 'defg', 'de']

    trie = Trie(keywords)
    print(trie.prefix_search('ab'))
    print(trie.prefix_search('a'))
    print(trie.prefix_search('abcd'))
    print(trie.prefix_search('de'))
    print(trie.prefix_search('vz'))
    print(trie.prefix_search('dk'))


if __name__ == '__main__':
    main()
