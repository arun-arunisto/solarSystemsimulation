gravity = 6.67e-11
mass_sun = 1.989e30
mass_mercury = 3.285e23
mass_venus = 4.867e24
mass_earth = 5.972e24
mass_mars = 6.39e23
mass_jupiter = 1.898e27
mass_saturn = 5.683e26
mass_uranus = 83.681e25
mass_neptune = 1.024e26
astronomical_unit = 1.5e11
day_sec = 24.0*60*60


#aphelion velocity  ["aphelion" refers to the point in a planet's orbit when it is farthest from the Sun]
mer_apv = 38860
ven_apv = 34290
ear_apv = 29290
mar_apv = 26500
jup_apv = 13070
sat_apv = 9690
ura_apv = 6800
nep_apv = 5430


#gravitational constant for planets
grav_const_mer = gravity*mass_mercury*mass_sun
grav_const_ven = gravity*mass_venus*mass_sun
grav_const_ear = gravity*mass_earth*mass_sun
grav_const_mar = gravity*mass_mars*mass_sun
grav_const_jup = gravity*mass_jupiter*mass_sun
grav_const_sat = gravity*mass_saturn*mass_sun
grav_const_ura = gravity*mass_uranus*mass_sun
grav_const_nep = gravity*mass_neptune*mass_sun


#setup the starting condition
#mercury
xmer, ymer, zmer = 0.387*astronomical_unit, 0, 0
xvmer, yvmer, zvmer = 0, mer_apv, 0

#venus
xven, yven, zven = 0.723*astronomical_unit, 0, 0
xvven, yvven, zvven = 0, ven_apv, 0

#Earth
xear, year, zear = 1.00*astronomical_unit, 0, 0
xvear, yvear, zvear = 0, ear_apv, 0

#Mars
xmar, ymar, zmar = 1.524*astronomical_unit, 0, 0
xvmar, yvmar, zvmar = 0, mar_apv, 0

#Jupiter
xjup, yjup, zjup = 5.203*astronomical_unit, 0, 0
xvjup, yvjup, zvjup = 0, jup_apv, 0

#Saturn
xsat, ysat, zsat = 9.539*astronomical_unit, 0, 0
xvsat, yvsat, zvsat = 0, sat_apv, 0

#Uranus
xura, yura, zura = 19.18*astronomical_unit, 0, 0
xvura, yvura, zvura = 0, ura_apv, 0

#Neptune
xnep, ynep, znep = 30.07*astronomical_unit, 0, 0
xvnep, yvnep, zvnep = 0, nep_apv, 0


#Sun
xsun, ysun, zsun = 0, 0, 0
xvsun, yvsun, zvsun = 0, 0, 0

t = 0.0
dt = 1*day_sec #every frame move this time

xmerlist, ymerlist, zmerlist = [], [], []
xvenlist, yvenlist, zvenlist = [], [], []
xearlist, yearlist, zearlist = [], [], []
xmarlist, ymarlist, zmarlist = [], [], []
xjuplist, yjuplist, zjuplist = [], [], []
xsatlist, ysatlist, zsatlist = [], [], []
xuralist, yuralist, zuralist = [], [], []
xneplist, yneplist, zneplist = [], [], []
xsunlist, ysunlist, zsunlist = [], [], []


#simulation
while t<5*365*day_sec:

    ######## mercury ###########
    rx_mer, ry_mer,rz_mer = xmer - xsun, ymer - ysun, zmer - zsun
    modr3_mer = (rx_mer**2+ry_mer**2+rz_mer**2)**1.5
    fx_mer = -grav_const_mer*rx_mer/modr3_mer
    fy_mer = -grav_const_mer*ry_mer/modr3_mer
    fz_mer = -grav_const_mer*rz_mer/modr3_mer

    #update quantites
    xvmer += fx_mer*dt/mass_mercury
    yvmer += fy_mer*dt/mass_mercury
    zvmer += fz_mer*dt/mass_mercury

    #update position
    xmer += xvmer*dt
    ymer += yvmer*dt
    zmer += zvmer*dt

    #saving the position in list
    xmerlist.append(xmer)
    ymerlist.append(ymer)
    zmerlist.append(zmer)

    ######## venus   ###########
    rx_ven, ry_ven, rz_ven = xven - xsun, yven - ysun, zven - zsun
    modr3_ven = (rx_ven ** 2 + ry_ven ** 2 + rz_ven ** 2) ** 1.5
    fx_ven = -grav_const_ven * rx_ven / modr3_ven
    fy_ven = -grav_const_ven * ry_ven / modr3_ven
    fz_ven = -grav_const_ven * rz_ven / modr3_ven

    # update quantites
    xvven += fx_ven * dt / mass_venus
    yvven += fy_ven * dt / mass_venus
    zvven += fz_ven * dt / mass_venus

    # update position
    xven += xvven * dt
    yven += yvven * dt
    zven += zvven * dt

    # saving the position in list
    xvenlist.append(xven)
    yvenlist.append(yven)
    zvenlist.append(zven)

    ######## earth   ###########
    rx_ear, ry_ear, rz_ear = xear - xsun, year - ysun, zear - zsun
    modr3_ear = (rx_ear ** 2 + ry_ear ** 2 + rz_ear ** 2) ** 1.5
    fx_ear = -grav_const_ear * rx_ear / modr3_ear
    fy_ear = -grav_const_ear * ry_ear / modr3_ear
    fz_ear = -grav_const_ear * rz_ear / modr3_ear

    # update quantites
    xvear += fx_ear * dt / mass_earth
    yvear += fy_ear * dt / mass_earth
    zvear += fz_ear * dt / mass_earth

    # update position
    xear += xvear * dt
    year += yvear * dt
    zear += zvear * dt

    # saving the position in list
    xearlist.append(xear)
    yearlist.append(year)
    zearlist.append(zear)


    ######## mars    ###########
    rx_mar, ry_mar, rz_mar = xmar - xsun, ymar - ysun, zmar - zsun
    modr3_mar = (rx_mar ** 2 + ry_mar ** 2 + rz_mar ** 2) ** 1.5
    fx_mar = -grav_const_mar * rx_mar / modr3_mar
    fy_mar = -grav_const_mar * ry_mar / modr3_mar
    fz_mar = -grav_const_mar * rz_mar / modr3_mar

    # update quantites
    xvmar += fx_mar * dt / mass_mars
    yvmar += fy_mar * dt / mass_mars
    zvmar += fz_mar * dt / mass_mars

    # update position
    xmar += xvmar * dt
    ymar += yvmar * dt
    zmar += zvmar * dt

    # saving the position in list
    xmarlist.append(xmar)
    ymarlist.append(ymar)
    zmarlist.append(zmar)


    ######## jupiter ###########
    rx_jup, ry_jup, rz_jup = xjup - xsun, yjup - ysun, zjup - zsun
    modr3_jup = (rx_jup ** 2 + ry_jup ** 2 + rz_jup ** 2) ** 1.5
    fx_jup = -grav_const_jup * rx_jup / modr3_jup
    fy_jup = -grav_const_jup * ry_jup / modr3_jup
    fz_jup = -grav_const_jup * rz_jup / modr3_jup

    # update quantites
    xvjup += fx_jup * dt / mass_jupiter
    yvjup += fy_jup * dt / mass_jupiter
    zvjup += fz_jup * dt / mass_jupiter

    # update position
    xjup += xvjup * dt
    yjup += yvjup * dt
    zjup += zvjup * dt

    # saving the position in list
    xjuplist.append(xjup)
    yjuplist.append(yjup)
    zjuplist.append(zjup)

    
    ######## saturn  ###########
    rx_sat, ry_sat, rz_sat = xsat - xsun, ysat - ysun, zsat - zsun
    modr3_sat = (rx_sat ** 2 + ry_sat ** 2 + rz_sat ** 2) ** 1.5
    fx_sat = -grav_const_sat * rx_sat / modr3_sat
    fy_sat = -grav_const_sat * ry_sat / modr3_sat
    fz_sat = -grav_const_sat * rz_sat / modr3_sat

    # update quantites
    xvsat += fx_sat * dt / mass_saturn
    yvsat += fy_sat * dt / mass_saturn
    zvsat += fz_sat * dt / mass_saturn

    # update position
    xsat += xvsat * dt
    ysat += yvsat * dt
    zsat += zvsat * dt

    # saving the position in list
    xsatlist.append(xsat)
    ysatlist.append(ysat)
    zsatlist.append(zsat)


    ######## uranus  ###########
    rx_ura, ry_ura, rz_ura = xura - xsun, yura - ysun, zura - zsun
    modr3_ura = (rx_ura ** 2 + ry_ura ** 2 + rz_ura ** 2) ** 1.5
    fx_ura = -grav_const_ura * rx_ura / modr3_ura
    fy_ura = -grav_const_ura * ry_ura / modr3_ura
    fz_ura = -grav_const_ura * rz_ura / modr3_ura

    # update quantites
    xvura += fx_ura * dt / mass_uranus
    yvura += fy_ura * dt / mass_uranus
    zvura += fz_ura * dt / mass_uranus

    # update position
    xura += xvura * dt
    yura += yvura * dt
    zura += zvura * dt

    # saving the position in list
    xuralist.append(xura)
    yuralist.append(yura)
    zuralist.append(zura)


    ######## neptune ###########
    rx_nep, ry_nep, rz_nep = xnep - xsun, ynep - ysun, znep - zsun
    modr3_nep = (rx_nep ** 2 + ry_nep ** 2 + rz_nep ** 2) ** 1.5
    fx_nep = -grav_const_nep * rx_nep / modr3_nep
    fy_nep = -grav_const_nep * ry_nep / modr3_nep
    fz_nep = -grav_const_nep * rz_nep / modr3_nep

    # update quantites
    xvnep += fx_nep * dt / mass_neptune
    yvnep += fy_nep * dt / mass_neptune
    zvnep += fz_nep * dt / mass_neptune

    # update position
    xnep += xvnep * dt
    ynep += yvnep * dt
    znep += zvnep * dt

    # saving the position in list
    xneplist.append(xnep)
    yneplist.append(ynep)
    zneplist.append(znep)


    ########## sun ###############
    # update quantites
    xvsun += -(fx_mer+fx_ven+fx_ear+fx_mar+fx_jup+fx_sat+fx_ura+fx_nep) * dt / mass_sun
    yvsun += -(fy_mer+fy_ven+fy_ear+fy_mar+fy_jup+fy_sat+fy_ura+fy_nep) * dt / mass_sun
    zvsun += -(fz_mer+fz_ven+fz_ear+fz_mar+fz_jup+fz_sat+fz_ura+fz_nep) * dt / mass_sun

    # update position
    xsun += xvsun * dt
    ysun += yvsun * dt
    zsun += zvsun * dt

    # saving the position in list
    xsunlist.append(xsun)
    ysunlist.append(ysun)
    zsunlist.append(zsun)


    #date update
    t += dt

print("Data Ready")


##simulation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure(figsize=(100,100), facecolor="black")
ax = plt.axes(projection='3d')
ax.axis('auto')
ax.set_facecolor("black")
axis_size = 2.5

ax.set_xlim(-axis_size*astronomical_unit, axis_size*astronomical_unit)
ax.set_ylim(-axis_size*astronomical_unit, axis_size*astronomical_unit)
ax.set_zlim(-axis_size*astronomical_unit, axis_size*astronomical_unit)

datadict = {}
dataset_sun = [xsunlist, ysunlist, zsunlist]
dataset_mer = [xmerlist, ymerlist, zmerlist]
dataset_ven = [xvenlist, yvenlist, zvenlist]
dataset_ear = [xearlist, yearlist, zearlist]
dataset_mar = [xmarlist, ymarlist, zmarlist]
dataset_jup = [xjuplist, yjuplist, zjuplist]
dataset_sat = [xsatlist, ysatlist, zsatlist]
dataset_ura = [xuralist, yuralist, zuralist]
dataset_nep = [xneplist, yneplist, zneplist]
datadict["sun"] = dataset_sun
datadict["mer"] = dataset_mer
datadict["ven"] = dataset_ven
datadict["ear"] = dataset_ear
datadict["mar"] = dataset_mar
datadict["jup"] = dataset_jup
datadict["sat"] = dataset_sat
datadict["ura"] = dataset_ura
datadict["nep"] = dataset_nep


vis_dict = {}
####### sun
line_sun, = ax.plot([0], [0], [0], '-g', lw=1)
point_sun, = ax.plot([astronomical_unit], [0], [0], marker="o",markersize=15, markeredgecolor="yellow", markerfacecolor="yellow")
text_sun = ax.text(astronomical_unit, 0, 0, "Sun", color="white")
vis_dict["sun"] = [line_sun, point_sun, text_sun]

####### mercury
line_mer, = ax.plot([0], [0], [0], '-g', lw=1)
point_mer, = ax.plot([astronomical_unit], [0], [0], marker="o",markersize=1, markeredgecolor="gray", markerfacecolor="gray")
text_mer = ax.text(astronomical_unit, 0, 0, "Mercury", color="white")
vis_dict["mer"] = [line_mer, point_mer, text_mer]

####### venus
line_ven, = ax.plot([0], [0], [0], '-g', lw=1)
point_ven, = ax.plot([astronomical_unit], [0], [0], marker="o",markersize=3, markeredgecolor="yellow", markerfacecolor="yellow")
text_ven = ax.text(astronomical_unit, 0, 0, "Venus", color="white")
vis_dict["ven"] = [line_ven, point_ven, text_ven]

####### earth
line_ear, = ax.plot([0], [0], [0], '-g', lw=1)
point_ear, = ax.plot([astronomical_unit], [0], [0], marker="o",markersize=4, markeredgecolor="blue", markerfacecolor="blue")
text_ear = ax.text(astronomical_unit, 0, 0, "Earth", color="white")
vis_dict["ear"] = [line_ear, point_ear, text_ear]

####### mars
line_mar, = ax.plot([0], [0], [0], '-g', lw=1)
point_mar, = ax.plot([astronomical_unit], [0], [0], marker="o",markersize=2, markeredgecolor="red", markerfacecolor="red")
text_mar = ax.text(astronomical_unit, 0, 0, "Mars", color="white")
vis_dict["mar"] = [line_mar, point_mar, text_mar]

####### jupiter
line_jup, = ax.plot([0], [0], [0], '-g', lw=1)
point_jup, = ax.plot([astronomical_unit], [0], [0], marker="o",markersize=8, markeredgecolor="orange", markerfacecolor="orange")
text_jup = ax.text(astronomical_unit, 0, 0, "Jupiter", color="white")
vis_dict["jup"] = [line_jup, point_jup, text_jup]

######## saturn
line_sat, = ax.plot([0], [0], [0], '-g', lw=1)
point_sat, = ax.plot([astronomical_unit], [0], [0], marker="o",markersize=7, markeredgecolor="yellow", markerfacecolor="yellow")
text_sat = ax.text(astronomical_unit, 0, 0, "Saturn", color="white")
vis_dict["sat"] = [line_sat, point_sat, text_sat]

######## uranus
line_ura, = ax.plot([0], [0], [0], '-g', lw=1)
point_ura, = ax.plot([astronomical_unit], [0], [0], marker="o",markersize=6, markeredgecolor="green", markerfacecolor="green")
text_ura = ax.text(astronomical_unit, 0, 0, "Uranus", color="white")
vis_dict["ura"] = [line_ura, point_ura, text_ura]

######## neptune
line_nep, = ax.plot([0], [0], [0], '-g', lw=1)
point_nep, = ax.plot([astronomical_unit], [0], [0], marker="o",markersize=5, markeredgecolor="blue", markerfacecolor="blue")
text_nep = ax.text(astronomical_unit, 0, 0, "Neptune", color="white")
vis_dict["nep"] = [line_nep, point_nep, text_nep]

def update(num, data_dict, vis_dict):
    #sun
    dataset_sun = data_dict["sun"]
    line_sun, point_sun, text_sun = vis_dict["sun"][0], vis_dict["sun"][1], vis_dict["sun"][2]
    line_sun.set_data_3d(dataset_sun[0][:num], dataset_sun[1][:num], dataset_sun[2][:num])
    """line_sun.set_data(dataset_sun[0][:num], dataset_sun[1][:num])
    line_sun.set_3d_properties(dataset_sun[2][:num])"""
    point_sun.set_data_3d(dataset_sun[0][num], dataset_sun[1][num], dataset_sun[2][num])
    text_sun.set_position((dataset_sun[0][num], dataset_sun[1][num], dataset_sun[2][num]))

    #mercury
    dataset_mer = data_dict["mer"]
    line_mer, point_mer, text_mer = vis_dict["mer"][0], vis_dict["mer"][1], vis_dict["mer"][2]
    line_mer.set_data_3d(dataset_mer[0][:num], dataset_mer[1][:num], dataset_mer[2][:num])
    point_mer.set_data_3d(dataset_mer[0][num], dataset_mer[1][num], dataset_mer[2][num])
    text_mer.set_position((dataset_mer[0][num], dataset_mer[1][num], dataset_mer[2][num]))

    #venus
    dataset_ven = data_dict["ven"]
    line_ven, point_ven, text_ven = vis_dict["ven"][0], vis_dict["ven"][1], vis_dict["ven"][2]
    line_ven.set_data_3d(dataset_ven[0][:num], dataset_ven[1][:num], dataset_ven[2][:num])
    point_ven.set_data_3d(dataset_ven[0][num], dataset_ven[1][num], dataset_ven[2][num])
    text_ven.set_position((dataset_ven[0][num], dataset_ven[1][num], dataset_ven[2][num]))

    #earth
    dataset_ear = data_dict["ear"]
    line_ear, point_ear, text_ear = vis_dict["ear"][0], vis_dict["ear"][1], vis_dict["ear"][2]
    line_ear.set_data_3d(dataset_ear[0][:num], dataset_ear[1][:num], dataset_ear[2][:num])
    point_ear.set_data_3d(dataset_ear[0][num], dataset_ear[1][num], dataset_ear[2][num])
    text_ear.set_position((dataset_ear[0][num], dataset_ear[1][num], dataset_ear[2][num]))

    #mars
    dataset_mar = data_dict["mar"]
    line_mar, point_mar, text_mar = vis_dict["mar"][0], vis_dict["mar"][1], vis_dict["mar"][2]
    line_mar.set_data_3d(dataset_mar[0][:num], dataset_mar[1][:num], dataset_mar[2][:num])
    point_mar.set_data_3d(dataset_mar[0][num], dataset_mar[1][num], dataset_mar[2][num])
    text_mar.set_position((dataset_mar[0][num], dataset_mar[1][num], dataset_mar[2][num]))

    #jupiter
    dataset_jup = data_dict["jup"]
    line_jup, point_jup, text_jup = vis_dict["jup"][0], vis_dict["jup"][1], vis_dict["jup"][2]
    line_jup.set_data_3d(dataset_jup[0][:num], dataset_jup[1][:num], dataset_jup[2][:num])
    point_jup.set_data_3d(dataset_jup[0][num], dataset_jup[1][num], dataset_jup[2][num])
    text_jup.set_position((dataset_jup[0][num], dataset_jup[1][num], dataset_jup[2][num]))

    #saturn
    dataset_sat = data_dict["sat"]
    line_sat, point_sat, text_sat = vis_dict["sat"][0], vis_dict["sat"][1], vis_dict["sat"][2]
    line_sat.set_data_3d(dataset_sat[0][:num], dataset_sat[1][:num], dataset_sat[2][:num])
    point_sat.set_data_3d(dataset_sat[0][num], dataset_sat[1][num], dataset_sat[2][num])
    text_sat.set_position((dataset_sat[0][num], dataset_sat[1][num], dataset_sat[2][num]))

    #uranus
    dataset_ura = data_dict["ura"]
    line_ura, point_ura, text_ura = vis_dict["ura"][0], vis_dict["ura"][1], vis_dict["ura"][2]
    line_ura.set_data_3d(dataset_ura[0][:num], dataset_ura[1][:num], dataset_ura[2][:num])
    point_ura.set_data_3d(dataset_ura[0][num], dataset_ura[1][num], dataset_ura[2][num])
    text_ura.set_position((dataset_ura[0][num], dataset_ura[1][num], dataset_ura[2][num]))

    #neptune
    dataset_nep = data_dict["nep"]
    line_nep, point_nep, text_nep = vis_dict["nep"][0], vis_dict["nep"][1], vis_dict["nep"][2]
    line_nep.set_data_3d(dataset_nep[0][:num], dataset_nep[1][:num], dataset_nep[2][:num])
    point_nep.set_data_3d(dataset_nep[0][num], dataset_nep[1][num], dataset_nep[2][num])
    text_nep.set_position((dataset_nep[0][num], dataset_nep[1][num], dataset_nep[2][num]))


ani = animation.FuncAnimation(
    fig, update, len(xearlist), fargs=(datadict, vis_dict), interval=1
)


plt.axis("off")
plt.show()
