import math

def ArdenBuckEquation(T):
	# https://en.wikipedia.org/wiki/Arden_Buck_equation
	return 0.61121 * math.exp((18.678 - T / 234.5) * (T / (257.14 + T))) # KPa

def WaterVapourMass(T):
	# Based on ideal gas low, n = pV/RT
	R = 8.31446261815324 # J / (K * mol), J = Pa * m^3
	water_molar_mass = 18015 # mg/mol
	mol_per_L = ArdenBuckEquation(T) * 1000 / (R * 1000 * (273.15 + T)) # mol/L
	return mol_per_L * water_molar_mass # mg/L

