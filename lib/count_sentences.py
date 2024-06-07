#!/usr/bin/env python3

class MyString:
    def __init__(self):
        self._value = ''

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("Value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        # Split the value into sentences based on period, question mark, or exclamation mark
        sentences = filter(None, map(str.strip, self._value.split('.!?')))
        # Count the number of non-empty sentences
        return len(list(sentences))
