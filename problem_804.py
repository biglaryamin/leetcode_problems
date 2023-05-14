def uniqueMorseRepresentations(words) -> int:
    s = set()
    mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    for w in words:                         # Iterate through every word.
        m = ''
        for l in w:                         # Iterate through every letter in current word.
            m += mos[ord(l) - ord('a')]     # Change the letter into morse code.
        s.add(m)                            # Use set to avoid replicate answer.
    
    return len(s)