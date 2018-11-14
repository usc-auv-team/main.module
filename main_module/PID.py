class PID():
	"""
	Class PID: To store the various P, I, D values to calculate the PID output for given key
	Author: Nishanth S Hegde
	"""
	def __init__(self):
		self.PIDSystems = Dict()

	@staticmethod
	def set(key, P, I, D, kErr = 0, iErr = 0):
		# Set P, I, D values to the given key
		# If kErr and iErr are specified, find the key and update the corresponding values.
		if key not in self.PIDSystems:
			self.PIDSystems[key] = [P, I, D, kErr, iErr]
		else:
			previousKerr = self.PIDSystems[key][3]
			previousIerr = self.PIDSystems[key][4]
			self.PIDSystems[key] = [P, I, D, previousKerr, previousIerr]

	@staticmethod
	def clear(key):
		# If the key is not present in the dictionary, then set everything to zero
		# If the key exists, then reset their error values
		if key not in self.PIDSystems:
			set(key, 0, 0, 0)
		else:
			previousPID = self.PIDSystems[key]
			set(key, previousPID[0], previousPID[1], previousPID[2])

	@staticmethod
	def get(key, error, P=None, I=None, D=None):
		# If the key is specified with P, I, D values, then set the values
		# Else return the calculated the PID output  
		if P not None and I not None and D not None:
			set(key, P, I, D)
						
		if key not in self.PIDSystems:
			return 0
		else:
			currentPID = self.PIDSystems[key]
			iErr = error + currentPID[4]
			dErr = error + currentPID[3]
			pOut = error * currentPID[0]
			iOut = iErr * currentPID[1]
			dOut = dErr * currentPID[2]

			set(key, currentPID[0], currentPID[1], currentPID[2], error, iErr)

		return pOut + iOut + dOut
