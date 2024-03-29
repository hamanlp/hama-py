from collections import deque


class AhoCorasickAutomaton:
    """Aho-Corasick automation.

    Attributes:
        self.root (Node): Root node.
        self.size  (int): Number of nodes.
    """

    def __init__(self):
        """Initialize automaton."""
        self.root = Node(parent=None, id=0)
        self.size = 1

    def add_words(self, words):
        """
        Add a list of words.

        Args:
            words (list): List of string words.
        """
        for word in words:
            self.add_word(word)
        self.set_failure_links()

    def add_word(self, word):
        """
        Add a single word.

        Args:
            word (str): String word.
        """

        curr_node = self.root

        for i, c in enumerate(word):
            next_node = curr_node.goto.get(c)

            if next_node is None:
                next_node = Node(parent=curr_node, id=self.size)
                self.size += 1
                curr_node.goto[c] = next_node
                # set failure node.

            if i == len(word) - 1:
                next_node.out.add(word)

            curr_node = next_node

    def set_failure_links(self):
        """
        Set failure link for every node.
        Also sets output dictionary links.
        """

        queue = deque()

        # Add failure links for nodes at depth 1.
        # self.root.failure_node = self.root
        for node in self.root.children:
            node.failure_node = self.root
            queue.append(node)

        # Add failure links to remaining nodes.
        while queue:
            node = queue.popleft()
            for char, child in node.goto.items():
                queue.append(child)
                candidate_node = node.failure_node
                while (
                    not candidate_node.goto.get(char) and not candidate_node.is_root()
                ):
                    candidate_node = candidate_node.failure_node
                child_failure_node = candidate_node.goto.get(char)
                child.failure_node = (
                    child_failure_node if child_failure_node else self.root
                )
                child.out = child.failure_node.out.union(child.out)

    def search(self, text):
        """
        Search for stored keywords in input text.
        In case of overlap (e.g. "C" and "GC" are both keywords),
        return order is not guaranteed.

        Args:
            text (str): String to search in.

        Returns:
            generator: Generator of tuples of format:
                       (word_found, start index, end index)
        """

        curr = self.root

        for i, c in enumerate(text):

            while curr.goto.get(c) is None and curr != self.root:
                curr = curr.next(c)
            # print('in while', c)

            curr = curr.next(c)
            # print('switch', c)

            for hit in curr.out:
                yield hit, i - len(hit) + 1, i

    def visualize(self):
        """Print automaton to console."""
        self.root.visualize(depth=0, char_to=None)


class Node:
    """
    Class representing a single node in Aho-Corasick automation.

    Attributes:
        parent       (Node): Parent node. None if root node.
        failure_node (Node): Node at the end of failure link.
        goto         (dict): Map of character to next state.
        out           (str): Keyword found at this node.
        children     (list): List of children Nodes.
        _id           (int): Node id. Used mostly for debugging.
    """

    def __init__(self, parent, id, failure_node=None, out=None):
        """Initialize Node class"""
        self.parent = parent
        self.failure_node = failure_node if parent else self
        self.goto = {}
        self.out = set()
        if out:
            self.out.add(out)
        self._id = id

    def is_root(self):
        """
        Determines if a Node instance is the root node.

        Returns:
            bool: Whether a node is the root.
        """
        return self.parent is None

    def next(self, c):
        """
        Return the next progression along the automation from the current node 
        upon receiving the input character.

        Args:
            c (str): Next character in text to search.

        Returns:
            Node: Node in the goto function or, if such Node is not defined for input c, 
                  Node from the failure link.
        """
        next_node = self.goto.get(c)
        return next_node if next_node else self.failure_node

    @property
    def children(self):
        """ 
        Getter for list of children nodes.

        Returns:
            list: List of children nodes.
        """
        return self.goto.values()

    def visualize(self, depth, char_to):
        """
        Print node and all its children

        Args:
            depth   (str): Depth of current node.
            char_to (str): Character that led to this node from its parent.

        """
        caret = "ㄴ" if depth else ""
        failure_node = int(self.failure_node._id) if self.failure_node else "DNE"
        print(
            "\t" * depth,
            f"{caret}{char_to} ->",
            self.out,
            f"id: {self._id}, fn: {failure_node}",
        )
        for c, child in self.goto.items():
            child.visualize(depth + 1, c)
