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


def sort_char_counts(char_counts):
  char_list = []

  for char, count in char_counts.items():
    char_list.append({"char": char, "num": count})

  def sort_on(item):
    return item["num"]

  char_list.sort(reverse=True, key=sort_on)
  return char_list
