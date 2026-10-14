# Problem Link : https://www.hackerrank.com/challenges/words-score/problem?isFullScreen=true
if __name__ == '__main__':
    count = input()
    words = input()
    words = words.split()
    total_score = 0

    # list of all the words
    for word in words:
      word_score = 0
    #iterate over the individual letter   
      for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
          word_score += 1   
      if word_score % 2 == 0:
        total_score += 2
      else:
        total_score +=1
        
    print(total_score)