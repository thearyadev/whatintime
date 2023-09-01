# whatintime
Simple package for timing a python function.

## Installation
```bash
pip install whatintime
```

## Usage
```python
import whatintime

@whatintime.whatintime(time_format=whatintime.TimeFormat.MS)
def thing_that_takes_time():
    pass
```