import re

def opening():
  print("""
  **************************************
  ** Welcome to the Madlib Experience!**
  **    Please see our rues below.    **
  **
  ** To quit at any time, type "quit" **
  **************************************
  
  
  I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

  """)
def read_template(template): 
  '''
  This is the read_template function 
  it will take a .txt file as a input
  with that file it will try to read the file contents then strip any spaces at the start and end of the string then return that new file
  read_template('bTest test test "\" n') = Test test test
  '''
  try:
    with open(template, 'r') as file:
      stripped = file.read().strip()
      return stripped
  except FileNotFoundError:
    raise FileNotFoundError('File cannot be found')
  except Exception as e:
    return 'There is a problem : '+ e

def parse_template(template):
  '''
  This is the parse_template
  it will take a tuple as a input
  with that file it will format out the words Adjective and Noun to {}
  then it will go through that same tuple and find all the words that were taken out and return a list
  it will then convert that new list into a tuple
  it will then return the tuple formated and the words seperated
  parse_template("It was a {Adjective} and {Adjective} {Noun}.") = 'It was a {} and {} {}' and ('dark', 'stormy', 'night')''' 
  expected_stripped = template.format(Adjective = {}, Noun = {}) 
  expected_parts_list = re.findall(r'{([^}]*)}', template)
  expected_parts = tuple(expected_parts_list)
  return expected_stripped, expected_parts

def merge(string, words):
  '''
  This is the merge function
  it will take a string and a tuple with 3 options
  with that it will format the string to now include the options within the tuple
  then it will return that newly formed string
  merge("It was a {} and {} {}.", ("dark", "stormy", "night") = 'It was a dark and story night'
  '''
  new_string = string.format(*words)
  return new_string

# print(read_template('../assets/dark_and_stormy_night_template.txt'))
# print(read_template('../assets/make_me_a_video_game_template.txt'))
# print(parse_template("It was a {Adjective} and {Adjective} {Noun}."))
# print(merge("It was a {} and {} {}.", ("dark", "stormy", "night")))







