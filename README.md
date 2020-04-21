<p align="center">
    <img src="https://raw.githubusercontent.com/hamanlp/hama-py/master/logo.png" height="100px" width="100px" alt="hama logo" align="center">
</p>

🦛 파이썬 한글 처리 라이브러리. Python **Ha**ngul **M**orphological **A**nalyzer
[![Build Status](https://travis-ci.org/hamanlp/hama-py.svg?branch=master)](https://travis-ci.org/hamanlp/hama-py)

## Features
* 텍스트 전처리 (Text preprocessing)
    * 형태소 분석 (Morpheme analysis)
    * 품사 태깅 (Part-of-speech tagging)


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

