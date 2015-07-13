import ephem 
from math import radians, degrees, cos, sin, asin, pi

##-------------------------------------------------------------------------
## Parallactic Angle
##-------------------------------------------------------------------------
# Author: Inaki Ordonez-Etxeberria
 
# Determine the Parallactic Angle (in degress) of an object, from the Righ Ascension and Declination of the object, Latitude and Longitude of the observatory, and date of observation. 
#
# Structure: ParallacticAngle('RA', 'DEC', 'Latitude ,'Longitude','date')
# Example: ParallacticAngle('23.20972', '10.8408', '28.775867','-17.89733','2014/11/15 20:00')
# 
# You can leave empty the information about the observatory and the date of observation. In that case the default parameters will be the position of the Isaac Newton Telescope in La Palma, at the moment of execution of the function. 
#
# Changes 
# (14/12/11) Replace the function of ephem parallactic_angle by the expression:
# HA=observatory.sidereal_time()- target.ra
# ParaAngle=atan(cos(observatory.lat)*sin(HA) / (sin(observatory.lat)*cos(DEC) -  cos(observatory.lat)*sin(DEC)*cos(HA)))
# Although the results are similar, depending on the version of ephem the function parallactic_angle() doesn't work. 
# (14/11/15) Replace the expression:
# ParaAngle  = -asin((sin(Az) * cos(LATrad))  /  (cos(DECrad)))
# by the function in ephem: parallactic_angle() although the result was similar.

def ParallacticAngle(AR, DEC, lat = '28.775867', lon =  '-17.89733', date = 'now'):
    # Definition of the observatory place
    observatory = ephem.Observer()
    observatory.lon = str(lon)
    observatory.lat = str(lat)
    if date  ==  'now':
        observatory.date = ephem.now()
    else:
        observatory.date = ephem.Date(date)
    
    # Definition of the target
    target = ephem.Equatorial(AR, DEC, epoch = ephem.J2000)
    # Computing the target from and observation point and moment.
    body = ephem.FixedBody()
    body._ra = target.ra
    body._dec = target.dec
    body._epoch = target.epoch
    body.compute(observatory)
    
    # Determining the parallactic_angle()
    # ParaAngle = body.parallactic_angle()
    # Just if there is some problem with this attribute in ephem, try:
    HA=observatory.sidereal_time()- target.ra
    ParaAngle=atan(cos(observatory.lat)*sin(HA) / (sin(observatory.lat)*cos(DEC) - cos(observatory.lat)*sin(DEC)*cos(HA)))
    if ParaAngle < 0:
        ParaAngle += (2 * pi)
    return degrees(ParaAngle), degrees(body.az), degrees(body.alt)

