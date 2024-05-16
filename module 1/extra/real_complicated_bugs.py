import re
# replace alle separators "." , ",", " en ", "omdat ", "zodat ", "want ", " wanneer " en "dat ”by a marker "|"

marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
sub_sentences = marked_text.split("|") # split de text on marker "|"
 
ego_score = 0
for sentence in sub_sentences: # repeat for every sentence in a list sentences
    sentence = sentence.strip() # remove leading and trailing spaces
    sentence = sentence.lower() # convert uppercase characters to lowercase
    if len(sentence) > 0:
      words = sentence.split(' ') # split sentence into words
      # first words of sentence equal to ik?
      if len(words) >= 2 and (words[0] in ('ik','mijn') or words[1] in ('ik','mijn')):
        ego_score += 1
 
print(ego_score)