def findShortestSubstringLen(string, target):
  min_window_len = 0
  char_dict = {}

  for i in range(len(target)):
    if target[i] not in char_dict:
      char_dict[target[i]] = 1
    else:
      char_dict[target[i]] += 1
  
  counter = 0
  ptr = 0

  for i in range(len(string)):
    if string[i] in char_dict:
      char_dict[string[i]] -= 1

      if char_dict[string[i]] >= 0:
        counter += 1
    
    while counter == len(target):
      if (i + 1 - ptr < min_window_len) or (min_window_len == 0):
        min_window_len = i + 1 - ptr
        print(string[ptr:i+1])

      if string[ptr] in char_dict:
        char_dict[string[ptr]] += 1
      
        if char_dict[string[ptr]] > 0:
          counter -= 1
          
      ptr += 1
  
  return min_window_len


print(findShortestSubstringLen("dabbcabcd", "abcd"))
