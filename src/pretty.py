def pretty(ast):
  if ast['type'] == 'var':
    return ast['name']
  if ast['type'] == 'application':
    return '(' + pretty(ast['function']) + ' ' + pretty(ast['arg']) + ')'

  return '\\' + ast['arg'] + '.' + pretty(ast['body'])
