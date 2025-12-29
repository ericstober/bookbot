def get_num_words(text):
  return len(text.split())

def get_char_counts(text):
  char_counts = {}

  for char in text.lower():
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1

  return char_counts
