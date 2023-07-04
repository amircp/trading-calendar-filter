# Trading Calendar Filter
Class to check for trading availability in the markets. 

```
ts = TradingFilter()
print(ts.should_trade("NewYork"))
```

Using the method "should_trade" you can know if the market is open. 

Market Options:
- NewYork
- Sydney
- London
- Tokyo

If you pass "crypto" it will asumme the market is always open. In the case of NewYork and London it will check if it is a holiday day.
The filter will return False (market close) if the current weekday is Saturday except for crypto.
