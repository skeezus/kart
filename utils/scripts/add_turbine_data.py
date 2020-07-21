from services import wind_turbine_service

from data.wind_turbines.models import WindTurbine

"""
to run:
    1: enter cli by entering `flask shell`
    2: import file: from utils.scripts import add_turbine_data
    3: run file: add_turbine_data.add_turbine_data()
"""
def add_turbine_data():
    turbines = wind_turbine_service.get_wind_turbines()

    for t in turbines:
        turbine = WindTurbine(**t)

        try:
            turbine.save()
        except Exception as e:
            print(e)
