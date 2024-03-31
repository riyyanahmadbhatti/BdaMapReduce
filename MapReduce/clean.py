
import csv
from nltk.corpus import stopwords
import string

def clean_text(text):
  """
  This function cleans text by removing punctuation, converting to lowercase,
  removing stopwords, and removing single-character words.
  """
  # Remove punctuation
  translator = str.maketrans('', '', string.punctuation)
  text = text.translate(translator)

  # Convert to lowercase
  text = text.lower()

  # Load English stopwords from NLTK
  stop_words = set(stopwords.words('english'))

  # Remove stopwords and single-character words
  words = [word for word in text.split() if word not in stop_words and len(word) > 1]

  # Join the cleaned words back into text
  cleaned_text = ' '.join(words)
  return cleaned_text

def clean_csv(input_file, output_file):
  """
  This function reads a CSV file, cleans the text in a specific column,
  and saves the cleaned text to a TXT file.
  """
  with open(input_file, 'r', newline='') as csvfile, open(output_file, 'w') as txtfile:
    reader = csv.reader(csvfile)
    # Skip header row (optional, adjust based on your CSV format)
    next(reader)
    for row in reader:
      # Assuming the text column is at index 3 (adjust based on your CSV)
      text_to_clean = row[3]
      id_no=row[0]
      cleaned_text = clean_text(text_to_clean)
      txtfile.write("no:"+id_no+'\n' + cleaned_text + '\n')

# Specify your input CSV file and desired output TXT file
input_csv = 'smallerdata.csv'
output_txt = 'cleaned_data.txt'

clean_csv(input_csv, output_txt)

print(f"CSV data cleaned and saved to: {output_txt}")

