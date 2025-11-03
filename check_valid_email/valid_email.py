    #here i will explaine the meaning for every part
    #  r-> it is mean the row starting
    #  ^->the start of line 
    #  [a-zA-Z0-9._%+-]-> all this case is allowed in part like "aq.tech10"
    #  +-> it s mean one or more then one i can Use
    #  @->must be in every email in the its location 
    #  [a-zA-Z0-9.-]->the part like " @gmail. "
    #  \. ->the \ to sure not ignore the dot . like dot after gmail
    #  [a-zA-Z]{2,}->the extention of domain like come and must be 2 or Memor 
    #  $-> end of line
    # re->regular expressions it is function in python used for string and like that
    # match->it is function in python to compare the arg is match if yes return match obj if not then return None
    #   is not -> used it if there are compare if there is match then True alse False
    
import re

def is_valid_email(email):
    # ex-> aq.tech10@gmail.com
    model= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(model,email) is not None
emails=["aq.tech10@gmail.com","wrong-email@","user@.com"]
for e in emails:
    if is_valid_email(e) ==True:
        print("{e} it is valid ")
    else:
        print("{e} it is not valid ")
        
    