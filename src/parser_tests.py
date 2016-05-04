#!/usr/bin/env python

from parser import *

if __name__ == '__main__':
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
      'type': 'var', 'name': 'x'
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

  assert parse([
    { 'type': 'lparen' },

    { 'type': 'lambda' },
    { 'type': 'var', 'name': 'x' },
    { 'type': 'dot' },
    { 'type': 'var', 'name': 'x' },

    { 'type': 'lambda' },
    { 'type': 'var', 'name': 'y' },
    { 'type': 'dot' },
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
      'type': 'lambda',
      'arg': 'y',
      'body': {
        'type': 'var',
        'name': 'y'
      }
    }
  }

  assert parse([
    { 'type': 'lambda' },
    { 'type': 'var', 'name': 'x' },
    { 'type': 'dot' },
    { 'type': 'lambda' },
    { 'type': 'var', 'name': 'y' },
    { 'type': 'dot' },
    { 'type': 'var', 'name': 'x' } ]) == {
      'type': 'lambda',
      'arg': 'x',
      'body': {
        'type': 'lambda',
        'arg': 'y',
        'body': {
          'type': 'var',
          'name': 'x'
        }
    }
  }

  print 'all tests pass!'
