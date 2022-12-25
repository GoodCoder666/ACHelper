# -*- coding: utf-8 -*-
# https://github.com/PaddlePaddle/PaddleNLP/blob/develop/examples/code_generation/codegen/README.md
# https://gitee.com/paddlepaddle/PaddleNLP/blob/develop/examples/code_generation/codegen/README.md
from paddlenlp import Taskflow

# import logging
# logging.disable(logging.INFO)

prompt = '# Read N from stdin, then print all non-negative integers less than or equal to N in descending order.'
codegen = Taskflow('code_generation', use_faster=True, model='Salesforce/codegen-350M-mono', decode_strategy='greedy_search', repetition_penalty=1.0)
for line in codegen(prompt):
    print(line)