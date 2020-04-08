# hama-py
🦛 파이썬 한글 처리 라이브러리. Python **Ha**ngul **M**orphological **A**nalyzer

[![Build Status](https://travis-ci.org/hamanlp/hama-py.svg?branch=master)](https://travis-ci.org/hamanlp/hama-py)


## Features
* 텍스트 전처리 (Text preprocessing)
    * 형태소 분석 (Morpheme analysis)


## Testing
```
coverage run -m pytest -v
coverage report -m
```


## Profiling
From the project root:
```
python -m cProfile -o profile/out.profile profile/profile.py
python profile/timing.py
```


## Formatting
```
yapf -i -r -vv .
```

