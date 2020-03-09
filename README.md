# Avanza

Based on [https://github.com/fhqvst/avanza](https://github.com/fhqvst/avanza)

Python wrapper for Unofficial Avanza API

Code is work in progress and is only meant as "proof of concept"

Authentication is done with selenium,
which will save cookies in current working directory.

Short example of getting the current buyprice for msft stock:

```python
from avanza import avanza

avanza_run = avanza.Avanza()
msft = avanza_run.stock(3873)
buy_price = msft['buyPrice']
print(buy_price)
> 166.48
```

More examples can be found [here](https://github.com/North14/avanza-client)
