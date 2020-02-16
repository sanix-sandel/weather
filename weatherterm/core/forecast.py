from datetime import date
from .forecast_type import ForecastType

class Forecast:
    def __init__(self, current_temp,
                humidity,
                wind,
                high_temp=None,
                low_temp=None,
                description='',
                forecast_date=None,
                forecast_type=ForecastType.TODAY):
        self._current_temp=current_temp
        self.high_temp=high_tempself.        
        self._low_temp = low_temp
        self._humidity = humidity
        self._wind = wind
        self._description = description
        self._forecast_type = forecast_type
        if forecast_date is None:
            self.forecast_date = date.today()
        else:
            self._forecast_date = forecast_date

    @property
    def forecast_date(self):
        return self._forecast_date

    @forecast_date.setter
    def forecast_date(self, forecast_date):
        self._forecast_date=forecast_date.strftime("%a %b %d")

    @property
                    