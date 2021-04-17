"""
Check tuning sessions, to make sure the procedure that give comment:
"Correcting ephys data to be same length as behavior data"
is applied correctly.

Now processing  d1pi041 2019-08-25 2700.0 4 1 4
/data/behavior/d1pi041/d1pi041_am_tuning_curve_20190825  ????  .h5   

"""

import os
import sys
import numpy as np
from jaratoolbox import behavioranalysis
from jaratoolbox import celldatabase
from jaratoolbox import ephyscore
from jaratoolbox import spikesanalysis
from jaratoolbox import extraplots
from matplotlib import pyplot as plt

sys.path.append('..')
import studyparams
import database_generation_funcs as funcs


CASE = 2
if CASE==0:
    cellToUse = ('d1pi041','2019-08-25',2700,4,2)
elif CASE==1:
    cellToUse = ('d1pi041','2019-08-25',3400,7,6) # Latency=14.8ms
elif CASE==2:
    cellToUse = ('d1pi041','2019-08-31',3500,8,6) # Latency=7ms

subject, date, depth, tetrode, cluster = cellToUse
dbPath = '/data/figuresdata/2019astrpi/test{}.h5'.format(subject)
basicDB = celldatabase.load_hdf(dbPath)
    
(indRow, dbRow) = celldatabase.find_cell(basicDB, subject, date, depth, tetrode, cluster)
oneCell = ephyscore.Cell(dbRow, useModifiedClusters=False)

session = 'tuningCurve'
tuningEphysData, tuningBehavData = oneCell.load(session)

baseRange = [-0.1, 0]

# Extracting information from ephys and behavior data to do calculations later with
currentFreq = tuningBehavData['currentFreq']
currentIntensity = tuningBehavData['currentIntensity']
uniqFreq = np.unique(currentFreq)
uniqueIntensity = np.unique(currentIntensity)
tuningTrialsEachCond = behavioranalysis.find_trials_each_combination(currentFreq, uniqFreq, currentIntensity, uniqueIntensity)

allIntenBase = np.array([])
respSpikeMean = np.empty((len(uniqueIntensity), len(uniqFreq)))  # same as allIntenResp
allIntenRespMedian = np.empty((len(uniqueIntensity), len(uniqFreq)))
Rsquareds = []
popts = []
tuningSpikeTimes = tuningEphysData['spikeTimes']
tuningEventOnsetTimesOrig = tuningEphysData['events']['soundDetectorOn']
tuningEventOnsetTimes = spikesanalysis.minimum_event_onset_diff(tuningEventOnsetTimesOrig, minEventOnsetDiff=0.2)

'''
amSpikeTimes = amEphysData['spikeTimes']
amEventOnsetTimesOrig = amEphysData['events']['soundDetectorOn']
amEventOnsetTimes = spikesanalysis.minimum_event_onset_diff(amEventOnsetTimesOrig, 0.2)
amCurrentFreq = amBehavData['currentFreq']
amUniqFreq = np.unique(amCurrentFreq)
amTimeRange = [-0.2, 0.7]
amTrialsEachCond = behavioranalysis.find_trials_each_type(amCurrentFreq, amUniqFreq)
'''


print('N events behav: {}', len(currentFreq))
print('N events ephys: {}', len(tuningEventOnsetTimes))

#if len(amCurrentFreq) != len(amEventOnsetTimes):
#    amEventOnsetTimes = amEventOnsetTimes[:-1]
#if len(amCurrentFreq) != len(amEventOnsetTimes):
#    print('Removing one does not align events and behavior. Skipping AM for cell')

bdata = tuningBehavData


behavStimOnEventsBool = bdata.events['nextState']==bdata.stateMatrix['statesNames']['output1On']
behavStimOnTime = bdata.events['eventTime'][behavStimOnEventsBool]


print('\nOutput of behavioranalysis.find_missing_trials()')
missingTrialsOrig = behavioranalysis.find_missing_trials(tuningEventOnsetTimesOrig,behavStimOnTime)
missingTrialsFixed = behavioranalysis.find_missing_trials(tuningEventOnsetTimes,behavStimOnTime)
print('Number of misaligned trials: Original={}, Fixed={}\n'.format(len(missingTrialsOrig),
                                                           len(missingTrialsFixed)))


plt.clf()
plt.suptitle('Stimulus events for {} (session \'{}\')'.format(oneCell, session), fontweight='bold')
for ind in [1,3]:
    plt.subplot(2,2,ind)
    pEphys, = plt.plot(tuningEventOnsetTimesOrig-tuningEventOnsetTimesOrig[0],'.')
    pBehav, = plt.plot(behavStimOnTime-behavStimOnTime[0],'o',mfc='none')
    plt.legend([pEphys,pBehav],['From ephys','From behavior'],loc='upper left')
    plt.xlabel('Event index')
    plt.ylabel('Event time (s)')
    if ind==1:
        plt.title('Before removing close events')
    else:
        plt.xlim([0,50])
        plt.ylim([0,80])
for ind in [2,4]:
    plt.subplot(2,2,ind)
    pEphys, = plt.plot(tuningEventOnsetTimes-tuningEventOnsetTimes[0],'.')
    pBehav, = plt.plot(behavStimOnTime-behavStimOnTime[0],'o',mfc='none')
    plt.legend([pEphys,pBehav],['From ephys','From behavior'],loc='upper left')
    plt.xlabel('Event index')
    plt.ylabel('Event time (s)')
    if ind==2:
        plt.title('After removing close events')
    else:
        plt.xlim([0,50])
        plt.ylim([0,80])
plt.show()

# -- Save figure --
if 0:
    extraplots.save_figure('issue_with_events', 'png', [8,8], outputDir='/tmp/', facecolor='w')


