class WordlePatternSolver:

    def __init__(self, file_path, correct_word : str):

        # Save correct word
        self.correct_word = correct_word.strip().lower()
        print("Initializing Pattern Solver for \"", self.correct_word, "\".", sep='')

        # Define tile codes
        self.tile_incorrect = "B"
        self.tile_miss = "Y"
        self.tile_correct = "G"

        # Load words
        file = open(file_path, 'r')
        if file.closed:
            print("Failed to open file_path:", file_path)
            exit

        file_content = file.readlines()
        words = [file_content[i].strip().lower() for i in range(len(file_content))]
        print("Loaded ", len(words), " valid guesses.", sep='')

        # Parse into patterns
        self.patterns = {}
        for i in range(len(words)):
            word = words[i]
            pattern = self.getPattern(word)
            if pattern not in self.patterns:
                self.patterns[pattern] = word
        print("Parsed ", len(self.patterns), " unique patterns.", sep='')


    def getPattern(self, guess):
        N = len(guess)
        pattern = list(self.tile_incorrect * N)

        # Check for correct letters
        not_correct_counts = {}
        for i in range(N):
            correct_letter = self.correct_word[i]
            if guess[i] == correct_letter:
                # If guessed letter is correct, set tile to correct
                pattern[i] = self.tile_correct
            else:
                # If guessed letter is not correct, increment count in dictionary
                if correct_letter in not_correct_counts:
                    not_correct_counts[correct_letter] += 1
                else:
                    not_correct_counts[correct_letter] = 1

        # Check for misses or incorrect letters
        for i in range(N):
            # Skip correct letters
            if pattern[i] == self.tile_correct:
                continue

            not_correct_letter = guess[i]
            if not_correct_letter in not_correct_counts:
                if not_correct_counts[not_correct_letter] > 0:
                    # If letter is somewhere else in word, decrement count in dictionay and mark tile as missed
                    not_correct_counts[not_correct_letter] -= 1
                    pattern[i] = self.tile_miss

        pattern_str = ''.join(pattern)
        return pattern_str


    def solvePattern(self, pattern):
        if pattern in self.patterns:
            return self.patterns[pattern]
        else:
            print("No word found for pattern \"", pattern, "\".", sep='')
            return None
    

    def checkAllPatterns(self, patterns):
        valid = True
        for pattern in patterns:
            valid = self.solvePattern(pattern) and valid
        return valid
    

    def printAllPatterns(self, patterns):
        for pattern in patterns:
            guess = self.solvePattern(pattern)
            print(pattern, " => ", guess, sep='')