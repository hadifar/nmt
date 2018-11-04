# -*- coding: utf-8 -*-
#
# Copyright 2018 Amir Hadifar. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from collections import Counter

with open('./tmp/nmt_data2/test.src') as test_src, open(
    './tmp/nmt_data2/test.trg') as test_trg, open(
    './tmp/nmt_data2/train.src') as train_src, open(
    './tmp/nmt_data2/train.trg') as train_trg:
  # build a counter from each word in the file

  t1 = test_trg.readlines()
  t2 = test_src.readlines()
  t3 = train_src.readlines()
  t4 = train_trg.readlines()
  corpus = t1 + t2 + t3 + t4
  count = Counter(word for line in corpus for word in line.split())

  with open('./tmp/nmt_data2/vocab.vocab', 'w') as vocab_file:
    for w, c in count.most_common(80000):
      vocab_file.write(w + '\n')
