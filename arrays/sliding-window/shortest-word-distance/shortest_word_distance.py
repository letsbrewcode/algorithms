# You are given a list of words. Find the shortest distance between the two
# words anywhere in the list.

# Example 1
# -----------
# Input
# words = ['can', 'this', 'problem', 'be', 'solved', 'problem']
# w1 = 'can'
# w2 = 'solved'
# -----------
# Output = 4

# Example 2
# -----------
# Input
# words = ['can', 'this', 'problem', 'be', 'solved', 'problem']
# w1 = 'problem'
# w2 = 'solved'
# -----------
# Output = 1


def brute_force(words, w1, w2):
    L = len(words)
    result = float('inf')
    
    for x in range(L):
        if words[x] == w1:
            for y in range(L):
                if words[y] == w2:
                    result = min(result, abs(y - x))
    
    return result if result != float('inf') else -1


def sliding_window(words, w1, w2):
    L = len(words)
    result = float('inf')
    
    left = -1
    right = -1
    
    for x in range(L):
        if words[x] == w1:
            left = x
        if words[x] == w2:
            right = x
        
        if left >= 0 and right >= 0:
            result = min(result, abs(right - left))

    return result if result != float('inf') else -1


if __name__ == "__main__":
    words = ['can', 'this', 'problem', 'be', 'solved', 'problem']
    print(brute_force(words, 'can', 'solved'))
    print(brute_force(words, 'problem', 'solved'))
    print(brute_force(words, 'can', 'this'))
    print(brute_force(words, 'can', ''))
    
    print(sliding_window(words, 'can', 'solved'))
    print(sliding_window(words, 'problem', 'solved'))
    print(sliding_window(words, 'can', 'this'))
    print(sliding_window(words, 'can', ''))