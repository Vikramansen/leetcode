from collections import Counter
def maxNumberOfBalloons(text):
    count_text = Counter(text)
    count_balloon = Counter("balloon")
    res = len(text)
    for char in count_balloon:
        if char not in count_text:
            return 0
        else:
            res = min(res, count_text[char] // count_balloon[char])
    return res
            
def main():
    text = "nlaebolkoballoons"
    print(maxNumberOfBalloons(text))
    
main()