# variables.py
class AppVars:
    __store_name = 'Marikina'
    __start_date = '2024-01-01'
    __end_date = '2025-01-01'

    @property
    def STORE_NAME(self):
        return self.__store_name

    @property
    def START_DATE(self):
        return self.__start_date

    @property
    def END_DATE(self):
        return self.__end_date

app_vars = AppVars()
header = ''
footer = ''