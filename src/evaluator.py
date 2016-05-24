def evaluate(ast):
  return eval_with_env(ast, [])

def lookup(name, env):
  for pair in env:
    if pair[0] == name:
      return pair[1]

  raise Exception('Name ' + name + ' not found in environment')

def eval_with_env(ast, env):
  if ast['type'] == 'application':
    closure = eval_with_env(ast['function'], env)
    value = eval_with_env(ast['arg'], env)

    return eval_with_env(
      closure['body'],
      [(closure['arg'], value)] + closure['env'] + env
    )

  if ast['type'] == 'var':
    return lookup(ast['name'], env)

  if ast['type'] == 'lambda':
    return {
      'type': 'closure',
      'arg': ast['arg'],
      'body': ast['body'],
      'env': env
    }

  return ast
