def split_and_len(s):
    return [f"{word} {len(word)}" for word in s.split()]
    
print(split_and_len("Ahmad is the best coder"))