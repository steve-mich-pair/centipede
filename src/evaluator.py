def evaluate(ast):
  return eval_with_env(ast, [])

def lookup(name, env):
  for pair in env:
    if pair[0] == name:
      return pair[1]

  raise Exception('Name ' + name + ' not found in environment')

def eval_with_env(ast, env):
  if ast['type'] == 'application':
    fn = ast['function']
    name = fn['arg']
    value = ast['arg']

    return eval_with_env(fn['body'], [(name, value)] + env)

  if ast['type'] == 'var':
    return lookup(ast['name'], env)

  return ast

def id(arg_name = 'x'):
  return {
    'type': 'lambda',
    'arg': arg_name,
    'body': {
      'type': 'var', 'name': arg_name
    }
  }

def app(fn, arg):
  return {
    'type': 'application',
    'function': fn,
    'arg': arg
  }

if __name__ == '__main__':
  assert evaluate(id()) == id()

  assert evaluate(app(id('x'), id('y'))) == id('y')
