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
  with open(template, 'rb') as file:
    print(file.strip())

opening()
read_template('assets/dark_and_stormy_night_template.txt')







