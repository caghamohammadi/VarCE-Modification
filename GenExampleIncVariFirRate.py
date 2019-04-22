from stgen import StGen
import numpy as np
import matplotlib.pyplot as plt

# import scipy.stats as scst
# import spikes

"""
Generating synthetic data
"""
x = StGen()

# total time in ms
ttime = 1000

# time resolution of change in firing rate in ms
timres = 110

# number of trails
ntrails = 100000

# time bins before the thinning process and the stopping time in millisecond
time = np.linspace(0, ttime, timres)
tstop = 1000

# binning the data
binsn = 11
bins = np.linspace(0, ttime, binsn)
binnedsptrain = np.zeros((ntrails, binsn-1))

# generating data

for i in xrange(ntrails):

    # firing rate in time in Hertz --- stochastic firing rate
    #frate = np.linspace(40, 41, timres) + (np.random.rand()-0.5) * np.linspace(0, 30, timres)
    frate = np.random.rand() * np.linspace(1, 30, timres)


    # parameters of inh gamma distribution in time
    phi0 = 1
    mean = 1.0 / frate
    var = phi0 * mean ** 2

    # change the parameters to normal k-theta form
    k = mean ** 2 / var
    theta = var / mean

    samplespiketrain = x.inh_gamma_generator(k, theta, time, tstop, array=True)
    q1, q2 = np.histogram(samplespiketrain, bins)
    binnedsptrain[i, :] = q1

    #plt.plot(time, frate, 'r')

TVarCE = np.linspace(0, 30, timres) **2 /12 * (0.1)**2
print "TVarCE", TVarCE

nvar = np.var(binnedsptrain, axis=0)
nmean = np.mean(binnedsptrain, axis=0)

print "nvar", nvar
print "nmean", nmean

phiest = np.min(nvar/nmean)

plt.show()
print (nvar - 1*nmean)
print phiest
print time