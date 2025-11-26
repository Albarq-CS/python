# check valid email
    # Here I will explain the meaning of every part
    #  r-> it means the row starting
    #  ^->the start of line 
    #  [a-zA-Z0-9._%+-]-> all this case is allowed in part like "aq.tech10"
    #  +-> it means one or more than one, I can use
    #  @->must be in every email in its location 
    #  [a-zA-Z0-9.-]->the part like " @gmail. "
    #  \. ->the \ to be sure not to ignore the dot . like a dot after Gmail
    #  [a-zA-Z]{2,}->the extension of the domain, like com,e, and must be 2 or Memor 
    #  $-> end of line
    # re->regular expressions, it is a  function in Python used for strings and like.
    # match->it is a function in Python to compare the argument. If it matches yes, return match obj; if no, then return None
    #   is not -> used it if there are compare if there is a match then True else False
