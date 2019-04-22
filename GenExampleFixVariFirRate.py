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
timres = 11

# number of trails
ntrails = 10000

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
    #frate = np.linspace(1, 2, timres) + 10*np.random.rand()
    frate = np.zeros((timres)) + 17 * np.random.rand()

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
    #print binnedsptrain[i,:]



TVarCE = 17**2/12  * (0.1)**2
print TVarCE
nvar = np.var(binnedsptrain, axis=0)
nmean = np.mean(binnedsptrain, axis=0)

phiest = np.min(nvar/nmean)


print (nvar - 1*nmean)
print phiest
print time