from typing import Dict


class Node(object):
    def __init__(self, char):
        self.char = char
        self.children: Dict[str, Node] = {}
        self.word_finished = False
        self.count = 1

    def print(self):
        print('---------------------------')
        print('Node:', self.char)
        print('Children:', list(self.children.keys()))
        print('Word:', self.word_finished)
        for node in self.children.values():
            node.print()


class Trie(object):
    def __init__(self):
        self.root = Node(None)

    def find(self, phrase):
        node = self.root
        for char in phrase:
            if char in node.children:
                node = node.children[char]
            else:
                return 0

        return node.count

    def keys_with_prefix(self, prefix):
        keys = []
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return keys

        return self.collect_phrases(node, prefix[:-1])

    def collect_phrases(self, node, prefix):
        phrases = []
        if node.word_finished:
            phrases.append(prefix + node.char)

        for child in node.children.values():
            phrases.extend(self.collect_phrases(child, prefix + node.char))

        return phrases

    def add(self, phrase):
        node = self.root
        for char in phrase:
            if char in node.children:
                node = node.children[char]
                node.count += 1
            else:
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node

        node.word_finished = True


if __name__ == '__main__':
    trie = Trie()
    trie.add('hack')
    trie.add('hacker')
    trie.add('hackerrank')
    trie.add('app')
    trie.add('application')
    trie.add('apple')
    trie.add('banana')
    trie.add('band')
    print(trie.keys_with_prefix('hack'))
    print(trie.keys_with_prefix('appl'))
    print(trie.keys_with_prefix('ba'))

    trie.root.print()
