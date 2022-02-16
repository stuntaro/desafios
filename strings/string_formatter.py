import argparse
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
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--limit", default=40, type=int)
    parser.add_argument("--justify", default=False, type=bool)
    args = parser.parse_args()
    with open(args.path) as f:
        text = f.read()
    formatter = StringFormater(args.justify, args.limit)
    print(formatter.wrap_text(text))
