class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        line = []
        num_of_letters = 0

        for word in words:
            if num_of_letters + len(line) + len(word) > maxWidth:
                spaces = maxWidth - num_of_letters
                if len(line) == 1:
                    res.append(line[0] + ' ' * spaces)
                else:
                    space_between = spaces // (len(line) - 1)
                    extra = spaces % (len(line) - 1)
                    for i in range(extra):
                        line[i] += ' '
                    res.append((' ' * space_between).join(line))
                line, num_of_letters = [], 0
            line.append(word)
            num_of_letters += len(word)

        last_line = ' '.join(line)
        res.append(last_line + ' ' * (maxWidth - len(last_line)))
        return res
