Author: Inaki Ordonez-Etxeberria
 
Determine the Parallactic Angle (in degress) of an object, from the Righ Ascension and Declination of the object, Latitude and Longitude of the observatory, and date of observation. 

Structure: ParallacticAngle('RA', 'DEC', 'Latitude ,'Longitude','date')
Example: ParallacticAngle('23.20972', '10.8408', '28.775867','-17.89733','2014/11/15 20:00')

You can leave empty the information about the observatory and the date of observation. In that case the default parameters will be the position of the Isaac Newton Telescope in La Palma, at the moment of execution of the function. 

