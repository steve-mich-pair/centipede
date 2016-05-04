def tokenize(code):

  current_char = 0
  new_token = 0
  tokens = []
  
  for i in xrange(len(code)):
    
    new_token = 0
    current_char = code[i]

    if(current_char.isalpha() == True):
      new_token = {'type': 'var', 'name': current_char}

    if(current_char == '('):
      new_token = {'type': 'lparen'}
  
    if(current_char == ')'):
      new_token = {'type': 'rparen'}

    if(current_char == '.'):
      new_token = {'type': 'dot'}

    if(current_char == '\\'):
      new_token = {'type': 'lambda'}

    if(new_token != 0):
      tokens.append(new_token)

  return tokens

if __name__ == '__main__':
  print tokenize('\\x.y   123    y')
  
