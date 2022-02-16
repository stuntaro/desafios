import textwrap


class StringFormater:

    def __init__(self, justify: bool, width: int) -> None:
        self._justify = justify
        self._width = width

    def wrap_text(self, text: str) -> str:
        return_text = ""
        for paragraph in text.split("\n"):
            for line in textwrap.wrap(paragraph, width=self._width):
                if self._justify:
                    line = self._align_string(line)
                return_text += line + "\n"
            return_text += "\n"
        return return_text

    def _align_string(self, line: str) -> str:
        items = line.strip().split()

        white_space = self._width - (len(line) - len(items))
        while white_space > 0:
            for i, _ in enumerate(items[:-1]):
                items[i] += " "
                white_space -= 1
                if white_space < 1:
                    break
        return ''.join(items)


if __name__ == "__main__":
    text = """In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\nAnd God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day."""
    formatter = StringFormater(True, 40)
    print(formatter.wrap_text(text))
