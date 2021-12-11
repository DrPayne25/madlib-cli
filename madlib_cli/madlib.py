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
  with open(template, 'r') as file:
    print(file.strip())


if __name__ == "__main__":
  opening()
  read_template()
  adjective_question = ''
  first_name_question = ''






