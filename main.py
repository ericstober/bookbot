import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  # book_path = "books/frankenstein.txt"

  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  text = get_book_text(sys.argv[1])

  word_count = get_num_words(text)
  char_counts = get_char_counts(text)
  sorted_chars = sort_char_counts(char_counts)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")

  for item in sorted_chars:
      char = item["char"]
      count = item["num"]

      if char.isalpha():
          print(f"{char}: {count}")

  print("============= END ===============")

main()
