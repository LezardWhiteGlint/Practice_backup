liquid_fuel_mass = 0.005
oxidizer_mass = 0.005
ore_mass = 0.01
kerbin_acceleration = 9.8

import pylab


class Rocket(object):
    def __init__(self,initial_mass,liquid_fuel_mass,liquid_fuel_consumption,oxidizer_mass,oxidizer_consumption,booster_force):
        self.initial_mass = initial_mass
        self.liquid_fuel_mass = liquid_fuel_mass
        self.liquid_fuel_consumption = liquid_fuel_consumption
        self.oxidizer_consumption = oxidizer_consumption
        self.oxidizer_mass = oxidizer_mass
        self.booster_force = booster_force
        self.mass_change = []
        self.acceleration_change = []
        self.velocity_change = []
        self.distance_change = []

    def getInitialMass(self):
        return self.initial_mass

    def getLiquidFuelMass(self):
        return self.liquid_fuel_mass

    def getLiquidFuelConsumption(self):
        return self.liquid_fuel_consumption

    def getOxidizerMass(self):
        return self.oxidizer_mass

    def getOxidizerConsumption(self):
        return self.oxidizer_consumption

    def getBoosterForce(self):
        return self.booster_force

    def getMassChange(self):
        return self.mass_change

    def getAccelerationChange(self):
        return self.acceleration_change

    def getVelocityChange(self):
        return self.velocity_change

    def getDistanceChange(self):
        return self.distance_change

    def setMassChange(self,change):
        self.mass_change = change

    def setAccelerationChange(self,change):
        self.acceleration_change = change

    def setVelocityChange(self,change):
        self.velocity_change = change

    def setDistanceChange(self,change):
        self.distance_change = change

    def burnTime(self):
        return int(self.getLiquidFuelMass()/self.getLiquidFuelConsumption())

    def mass(self):
        #return a list, record each second acceleration
        #lfc: liquid fuel consumption
        #oc: oxidizer consumption
        result = []
        current_mass = self.getInitialMass()
        for i in range(self.burnTime()):
            current_mass = self.getInitialMass() - (self.getLiquidFuelConsumption() + self.getOxidizerConsumption())*liquid_fuel_mass*i
            result.append(current_mass)
        self.setMassChange(result)
        
    def acceleration(self,body_acceleration):
        #return a list, record each second acceleration
        result = []
        for i in range(self.burnTime()):
            result.append(self.getBoosterForce()/self.getMassChange()[i]-body_acceleration)
        self.setAccelerationChange(result)
        

    def velocity(self):
        #return a list, record each second velocityi
        result = []
        total = 0
        for i in range(self.burnTime()):
            result.append(total)
            total += self.getAccelerationChange()[i]
        self.setVelocityChange(result)

    def burnEndTravelDistance(self):
        #return a list, record each second total travelled distance
        result = []
        total = 0
        for i in range(self.burnTime()):
            total += self.getVelocityChange()[i]
            result.append(total)
        self.setDistanceChange(result)

    def plotAll(self):
        pylab.figure(1)
        pylab.title('Mass Change')
        pylab.plot(self.getMassChange())
        pylab.figure(2)
        pylab.title('Acceleration Change')
        pylab.plot(self.getAccelerationChange())
        pylab.figure(3)
        pylab.title('Velocity Change')
        pylab.plot(self.getVelocityChange())
        pylab.figure(4)
        pylab.title('Distance Change')
        pylab.plot(self.getDistanceChange())
        pylab.show()

    def calculation(self,body_acceleration):
        self.mass()
        self.acceleration(body_acceleration)
        self.velocity()
        self.burnEndTravelDistance()
        self.plotAll()
        
#Rocket(initial_mass,liquid_fuel_mass,liquid_fuel_consumption,
        #oxidizer_mass,oxidizer_consumption,booster_force)
##secondPhase= Rocket(70.257,720+1440,29.135,1760+880,35.609,936.508)
##secondPhase.calculation(0)

firstPhase = Rocket(170.490,1440*6,61.183,1760*6,74.779,1866.667)
firstPhase.calculation(9.8)

secondPhase = Rocket(89.940,1440*2,44.407,1760*2,54.275,1500)
#secondPhase.calulation(0)
