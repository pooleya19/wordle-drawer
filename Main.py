from WordlePatternSolver import WordlePatternSolver

def main():
    file_path = "ValidGuesses.txt"
    correct_word = "BULGE"
    patternSolver = WordlePatternSolver(file_path, correct_word)

    # Define patterns
    patterns1 = [
        "BBYYB",
        "BYYYY",
        "YYYGG",
        "YYYYY",
        "BYYYY",
        "BYBBY",
    ]

    patterns2 = [
        "BBBBB",
        "BBBBB",
        "BBYYY",
        "BYYYG",
        "BYYYY",
        "BBYBY"
    ]

    patterns3 = [
        "BBBBB",
        "BYYYB",
        "YYYGB",
        "YYYYB",
        "BYBYB",
        "BBBBB"
    ]

    print("Pattern 1:", patternSolver.checkAllPatterns(patterns1))
    print("Pattern 2:", patternSolver.checkAllPatterns(patterns2))
    print("Pattern 3:", patternSolver.checkAllPatterns(patterns3))

    patternSolver.printAllPatterns(patterns3)

if __name__ == "__main__":
    main()