\# pyutils\_pro



A lightweight Python utilities library built while learning advanced Python concepts.



\## Features (Day 2)



\- Logging decorator

\- Retry decorator with configurable attempts

\- Function execution timing

\- Closure-based design patterns



\## Example Usage



```python

from pyutils import log\_calls, time\_execution



@log\_calls

@time\_execution

def process():

&#x20;   return sum(range(1000))

