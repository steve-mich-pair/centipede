def parse(tokens):
  if len(tokens) == 0: return None

  if tokens[0]['type'] == 'lparen':
    return {
      'type': 'application',
      'function': tokens[1],
      'arg': tokens[2]
    }
  elif tokens[0]['type'] == 'lambda':
    return {
      'type': 'lambda',
      'arg': tokens[1]['name'],
      'body': parse([tokens[3]])
    }

  return tokens[0]

def parse_single(tokens):
  if tokens[0]['type'] == 'lambda':
    body, rest = parse_single(tokens[3:])
    return ({
      'type': 'lambda',
      'arg': tokens[1]['name'],
      'body': body
    }, rest)

  return (tokens[0], tokens[1:])

if __name__ == '__main__':
  assert parse([]) == None
  assert parse([{ 'type': 'var', 'name': 'x' }]) == { 'type': 'var', 'name': 'x' }
  assert parse([
    { 'type': 'lparen' },
    { 'type': 'var', 'name': 'x' },
    { 'type': 'var', 'name': 'y' },
    { 'type': 'rparen' }
  ]) == {
    'type': 'application',
    'function': {
      'type': 'var',
      'name': 'x'
    },
    'arg': {
      'type': 'var',
      'name': 'y'
    }
  }
  assert parse([
    { 'type': 'lambda' },
    { 'type': 'var', 'name': 'x' },
    { 'type': 'dot' },
    { 'type': 'var', 'name': 'x' }
  ]) == {
    'type': 'lambda',
    'arg': 'x',
    'body': {
      'type': 'var',
      'name': 'x'
    }
  }

  # (\x.x y)
  assert parse([
    { 'type': 'lparen' },
    { 'type': 'lambda' },
    { 'type': 'var', 'name': 'x' },
    { 'type': 'dot' },
    { 'type': 'var', 'name': 'x' },
    { 'type': 'var', 'name': 'y' },
    { 'type': 'rparen' }
  ]) == {
    'type': 'application',
    'function': {
      'type': 'lambda',
      'arg': 'x',
      'body': {
        'type': 'var',
        'name': 'x'
      }
    },
    'arg': {
      'type': 'var',
      'name': 'y'
    }
  }
