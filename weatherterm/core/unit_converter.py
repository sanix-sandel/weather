from .unit import Unit

class UnitConverter:
    def __init__(self, parser_default_unit):
        self._parser_default_unit=parser_default_unit
        self.dest_unit=dest_unit

        self._convert_functions={
            Unit.CELSIUS:self._to_celsius,
            Unit.FAHRENHEIT:self._to_fahrenheit,
        }

        @property
        def dest_unit(self):
            return self.__dest_unit

        @dest_unit.setter
        def dest_unit(self, dest_unit):    
            self._dest_unit=dest_unit

        def convert(self, temp):
            try:
                temperature=float(temp)    
                except valueError:
                    return 0
            if (self.dest._unit==self._parser_default        