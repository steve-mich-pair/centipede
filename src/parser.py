def parse(tokens):
  return parse_single(tokens)[0]

def parse_single(tokens):
  def parse_application():
    fn, rest1 = parse_single(tokens[1:])
    arg, rest2 = parse_single(rest1)

    return ({
      'type': 'application',
      'function': fn,
      'arg': arg
    }, rest2[1:])

  def parse_lambda():
    body, rest = parse_single(tokens[3:])
    return ({
      'type': 'lambda',
      'arg': tokens[1]['name'],
      'body': body
    }, rest)

  if tokens[0]['type'] == 'lparen':
    return parse_application()

  if tokens[0]['type'] == 'lambda':
    return parse_lambda()

  return (tokens[0], tokens[1:])
