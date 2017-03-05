names = {
# Number corresponding to point cominations, and official names as reported
# in metadata.
    0:  'None',
    1:  'Lower-left, Bottom',
    2:  'Bottom',
    3:  'Lower-right, Bottom',
    4:  'Mid-left, Center',
    5:  'Center',
    6:  'Mid-right, Center',
    7:  'Upper-left, Top',
    8:  'Top',
    9:  'Upper-right, Top',
    10: 'Right',
    11: 'Lower-left, Mid-left',
    12: 'Upper-left, Mid-left',
    13: 'Bottom, Center',
    14: 'Top, Center',
    15: 'Lower-right, Mid-right',
    16: 'Upper-right, Mid-right',
    17: 'Left',
    18: 'Mid-left',
    19: 'Center',
    20: 'Mid-right',
}
    
locations = {
# Name and location of points. x (y) centroid is with respect to the x (y) pixel
# dimension. 
#    name            xpos  ypos    shapes   
    'Left':         (0.212,0.500,['rectangle']),
    'Upper-left':   (0.353,0.341,['square']),
    'Mid-left':     (0.353,0.500,['square']),
    'Lower-left':   (0.353,0.659,['square']),
    'Top':          (0.500,0.341,['square']),
    'Center':       (0.500,0.500,['center','hole']),
    'Bottom':       (0.500,0.659,['square']),
    'Upper-right':  (0.647,0.341,['square']),
    'Mid-right':    (0.647,0.500,['square']),
    'Lower-right':  (0.647,0.659,['square']),
    'Right':        (0.788,0.500,['rectangle'])
}

interface = {
# Size (WRT to x/y pixel dimensions) of the boxes that represent the AF points.
    'rectangle':    (0.010,0.051,'color'),
    'square':       (0.016,0.024,'color'),
    'center':       (0.023,0.035,'color'),
    'hole':         (0.016,0.024,'transparent')
}
