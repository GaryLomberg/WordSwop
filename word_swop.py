#! /usr/bin/env python

import pyperclip

user_input = ""

while (user_input != "x"):

	print("\nPlease copy the paragraph you'd like to word swop to your clipboard now.\n")

	current_word = input("Please input the word you'd like replaced: ")
	replacement = input("Please input the word you'd like to replace it with: ")

	paragraph = pyperclip.paste()
	updated_paragraph = paragraph.replace(current_word, replacement)

	pyperclip.copy(updated_paragraph)

	user_input = input("\nPress enter to word swop the next paragraph, type x to close: \n")


