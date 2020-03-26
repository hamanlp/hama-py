# hama-py
🦛 파이썬 형태소 분석기. Python **Ha**ngul **M**orpheme **A**nalyzer

## Formatting
```
yapf -i -r -vv .
```

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
