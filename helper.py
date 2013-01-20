#!/usr/bin/python2.7

import math

au = 1.49597870691e11
ly = 63240 * au
pc = 206265 * au

year =  31556926

G = 6.673e-11
g = 9.82 
c = 2.99792458e8 
k = 1.380648e-23 
me = 9.109382e-31
mp = 1.6726217e-27
mp_to_me_ratio = 1.836152672e3
h = 6.626069e-34
Rydberg = 1.09737315685e7
St_Boltzmann = 5.6703e-8
b = 0.0028977685
sol_const = 1.37e3

earth_m = 5.97219e24
earth_r = 6.371e6
sol_m = 1.9891e30
sol_r = 6.95508e8
sol_t = 5777
sol_l = 3.83e26

def escape_v (m, r):
    return math.sqrt(2 * G * m / r)

def thermal_v(m, t):
    return math.sqrt ((3 * k * t) /m)

def doppler_v(f_original, f_recieved):
    return c * (f_recieved - f_original) / f_original
