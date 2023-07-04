import pandas_market_calendars as mcal
from pytz import timezone
from datetime import datetime
import pandas as pd


class TradingFilter:
    """
    This class determines if a given market is currently open for trading.
    It uses the pandas_market_calendars library for some markets, and
    hard-coded hours for others.
    """
    def __init__(self):
        self.calendars = {
            'NewYork': mcal.get_calendar('NYSE'),
            'London': mcal.get_calendar('LSE'),
            # Other calendars are not provided by pandas_market_calendars
            # Need to use custom calendars or other means
        }

        self.always_open_markets = ['crypto']

        self.market_hours = {
            'Sydney': {
                'start': 22,  # GMT Time
                'end': 7
            },
            'Tokyo': {
                'start': 23,
                'end': 8
            },
        }

    def should_trade(self, market: str) -> bool:
        """
        Determines if the given market is currently open for trading.
        """
        now = datetime.now(timezone('UTC'))

        if market.lower() in self.always_open_markets:
            return True

        # Check if the current day is Saturday.
        if now.weekday() == 5:
            return False

        if market in self.calendars:
            calendar = self.calendars[market]

            market_schedule = calendar.schedule(start_date=now.date(), end_date=now.date())

            if market_schedule.empty:
                return False  # Market is not open on this day

		
            return calendar.open_at_time(market_schedule, pd.Timestamp(now))

        elif market in self.market_hours:
            current_utc_time = datetime.now(timezone('UTC'))
            return self.market_hours[market]['start'] <= current_utc_time.hour < self.market_hours[market]['end']

        else:
            raise ValueError(f"Unknown market: '{market}'")


ts=TradingFilter()
print(ts.should_trade("NewYork"))
