from datetime import datetime, timedelta
import math
from angle import Angle

class Aries:
    
    REFERENCE_YEAR = 2001
    def __init__(self):
        pass
    
    @staticmethod
    def get_greenwich_hour_angle(year, month, day, hour, minute, second):
        """
        = relative_prime_meridian + earth rotation
        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :param second:
        :return:
        """
        reference_datetime_str = "2001,01,01,00,00,00"
        observation_datetime_str = str(year) + ',' + str(month) + ',' + str(day) + ','
        observation_datetime_str += str(hour) + ',' + str(minute) + ',' + str(second)
        
        observation_datetime = datetime.strptime(observation_datetime_str, '%Y,%m,%d,%H,%M,%S')
        reference_datetime = datetime.strptime(reference_datetime_str, '%Y,%m,%d,%H,%M,%S')
        print(observation_datetime)
        print ((observation_datetime - reference_datetime).total_seconds())
        elapsed_sed_since_ref = (observation_datetime - reference_datetime).total_seconds()/1000.0
        
        relative_pm = Aries.__get_relative_prime_meridian(year)
        earth_rotation = Aries.__get_earth_rotation_since_observation(elapsed_sed_since_ref)
        return Angle.add(relative_pm, earth_rotation)
        
    
    
    @staticmethod
    def __get_relative_prime_meridian(year):
        """
        
        - total progression = 100d42.6 + cumulative prog + leap progs
        - cumulative progression: delta(year-2001) * -0d14.31667
        - leap progression: (leap years elapsed) * 0d59.0
        :param year: observation year
        :return: angle of prime meridian
        """
        reference_rotation = Angle.from_string("100d42.6")
        # cumulative progression: delta(year-2001) * -0d14.31667
        annual_gha_decrement = Angle.from_string("-0d14.31667")
        delta_year = year - Aries.REFERENCE_YEAR
        cumulative_progression = Angle.multiply(annual_gha_decrement,delta_year)
        
        # leap progression: (leap years elapsed) * 0d59.0
        daily_rotation = Angle.from_string("0d59.0")
        leap_years = math.floor((year - Aries.REFERENCE_YEAR)/4)
        leap_progression = Angle.multiply(daily_rotation, leap_years)
        
        # total progression = 100d42.6 + cumulative prog + leap progs
        
        total_progression = Angle.add(reference_rotation, cumulative_progression)
        total_progression = Angle.add(total_progression, leap_progression)
        return total_progression
    
    @staticmethod
    def __get_earth_rotation_since_observation(elapsed_seconds):
        """
        convert seconds into angles
        total sec/86164.1*360d00.0
        :param elapsed_seconds: second between ref time and observed time
        :return: hour angle
        """
        full_angle = Angle.from_string("360d00.0")
        rotation = math.floor(elapsed_seconds/86164.1)
        return Angle.multiply(full_angle, rotation)
