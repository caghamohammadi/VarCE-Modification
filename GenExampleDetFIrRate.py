from stgen import StGen
import numpy as np
# import scipy.stats as scst
# import spikes

"""
Generating synthetic data
"""
x = StGen()

# total time in ms
ttime = 1000

# time resolution of change in firing rate in ms
timres = 10

# number of trails
ntrails = 10000

# firing rate in time in Hertz --- deterministic
frate = np.linspace(10, 20, timres)

# parameters of inh gamma distribution in time
phi0 = 0.6
mean = 1.0/frate
var = phi0 * mean**2


# change the parameters to normal k-theta form
k = mean**2/var
theta = var/mean


# time bins before the thinning process and the stopping time in millisecond
time = np.linspace(1, ttime, timres)
tstop = 1000

# binning the data

binsn = 50
bins = np.linspace(0, ttime, binsn)
binnedsptrain = np.zeros((ntrails, binsn-1))

# generating data

for i in xrange(ntrails):
    samplespiketrain = x.inh_gamma_generator(k, theta, time, tstop, array=True)
    q1, q2 = np.histogram(samplespiketrain, bins)
    binnedsptrain[i, :] = q1
    # print binnedsptrain[i,:]

print binnedsptrain


nvar = np.var(binnedsptrain, axis=0)
nmean = np.mean(binnedsptrain, axis=0)

phiest = np.min(nvar/nmean)

print nvar-phiest*nmean
