#!/usr/bin/env python

from sys import argv

from pretty import pretty
from evaluator import evaluate
from parser import parse
from sugar import desugar
from tokenizer import tokenize

if __name__ == '__main__':
  code = argv[1]

  print pretty(evaluate(desugar(parse(tokenize(code)))))
