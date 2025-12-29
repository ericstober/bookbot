from stats import get_num_words, get_char_counts

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  book_text = get_book_text("./books/frankenstein.txt")
  num_words = get_num_words(book_text)
  char_counts = get_char_counts(book_text)

  print(f"Found {num_words} total words")
  print(char_counts)

main()
