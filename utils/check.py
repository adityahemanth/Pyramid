class check:

	def _validate_word(self, word):

		for letter in word:
			if not ord(letter) < 128:
				return False


		return True



	def _clean_word(self, word):

		new_word = ''
		for letter in word:
			if letter.isalpha() or letter.isdigit():
				new_word += letter

		return new_word