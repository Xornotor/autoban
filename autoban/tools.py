from collections import deque
from time import sleep

from pynput.keyboard import Controller, Key


def read_file(name: str) -> list[str]:
    """Reads the target file as read only"""
    with open(name, "r") as file:
        stream = file.readlines()
        lines = clear_lines(stream)

        return lines


def clear_lines(lines: list[str]) -> list[str]:
    """Removes new lines `\n` from the end of lines"""

    no_newlines = deque(map(lambda line: line.replace("\n", ""), lines))
    return no_newlines


def type_these(lines: list[str]) -> None:
    """Type lines from a given list"""
    controller = Controller()

    def type_line(line: str) -> None:
        controller.type(line)
        controller.press(Key.enter)
        controller.release(Key.enter)
        sleep(0.3)

    deque(map(type_line, lines))
