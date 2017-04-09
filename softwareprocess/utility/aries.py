class Aries:
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
        pass
    
    @staticmethod
    def __get_reference_greenwich_hour_angle():
        """
        using date 2001-01-01
        using time 0:00:00 (utc)
        using angle: 100d42.6
            
        :return: returns reference angle based on know greenwich hour angle for aries
        """
        
        pass
    
    @staticmethod
    def __get_relative_prime_meridian(year):
        """
        
        - total progression = 100d42.6 + cumulative prog + leap progs
        - cumulative progression: delta(year-2001) * -0d14.3667
        - leap progression: (leap years elapsed) * 0d59.0
        :param year: observation year
        :return: angle of prime meridian
        """
        
        pass
    
    @staticmethod
    def __get_earth_rotation_since_observation(elapsed_seconds):
        """
        convert seconds into angles
        total sec/86164.1*360d00.0
        :param elapsed_seconds: second between ref time and observed time
        :return: hour angle
        """
        pass
