'''
Plotting the overlapped PSTHs
'''

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from jaratoolbox import settings
from jaratoolbox import celldatabase
from jaratoolbox import behavioranalysis
from jaratoolbox import spikesanalysis
from jaratoolbox import extraplots
from jaratoolbox import ephyscore
from jaratoolbox import spikesorting
import studyparams

dbPath = os.path.join(settings.FIGURES_DATA_PATH, studyparams.STUDY_NAME)
dbFilename = os.path.join(dbPath,'celldb_{}.h5'.format(studyparams.STUDY_NAME))

figFormat = 'png'
outputDir = os.path.join(settings.FIGURES_DATA_PATH, studyparams.STUDY_NAME,'reports')

# -- Load the database of cells --
celldb = celldatabase.load_hdf(dbFilename)
number_of_clusters = len(celldb) - 1

for indRow,dbRow in celldb[266:267].iterrows():
    oneCell = ephyscore.Cell(dbRow)
    timeRange = [-0.1, 0.4]  # In seconds

    '''
    Standard
    '''
    ephysDataStd, bdataStd = oneCell.load('standard')
    spikeTimesStd = ephysDataStd['spikeTimes']
    eventOnsetTimesStd = ephysDataStd['events']['stimOn']
    if len(eventOnsetTimesStd)==len(bdataStd['currentFreq'])+1:
        eventOnsetTimesStd = eventOnsetTimesStd[:-1]
    (spikeTimesFromEventOnsetStd,trialIndexForEachSpikeStd,indexLimitsEachTrialStd) = spikesanalysis.eventlocked_spiketimes(spikeTimesStd, eventOnsetTimesStd, timeRange)

    frequenciesEachTrialStd = bdataStd['currentFreq']
    numberOfTrialsStd = len(frequenciesEachTrialStd)
    arrayOfFrequenciesStd = np.unique(bdataStd['currentFreq'])
    arrayOfFrequenciesStdkHz = arrayOfFrequenciesStd/1000
    labelsForYaxis = ['%.1f' % f for f in arrayOfFrequenciesStdkHz]
    trialsEachCondStd = behavioranalysis.find_trials_each_type(frequenciesEachTrialStd,arrayOfFrequenciesStd)

    '''
    ODDBALL
    '''
    ephysDataOdd, bdataOdd = oneCell.load('oddball')
    spikeTimesOdd = ephysDataOdd['spikeTimes']
    eventOnsetTimesOdd = ephysDataOdd['events']['stimOn']
    if len(eventOnsetTimesOdd)==len(bdataOdd['currentFreq'])+1:
        eventOnsetTimesOdd = eventOnsetTimesOdd[:-1]
    (spikeTimesFromEventOnsetOdd,trialIndexForEachSpikeOdd,indexLimitsEachTrialOdd) = spikesanalysis.eventlocked_spiketimes(spikeTimesOdd, eventOnsetTimesOdd, timeRange)

    frequenciesEachTrialOdd = bdataOdd['currentFreq']
    numberOfTrialsOdd = len(frequenciesEachTrialOdd)
    arrayOfFrequenciesOdd = np.unique(bdataOdd['currentFreq'])
    arrayOfFrequenciesOddkHz = arrayOfFrequenciesOdd/1000
    labelsForYaxis = ['%.1f' % f for f in arrayOfFrequenciesOddkHz]
    trialsEachCondOdd = behavioranalysis.find_trials_each_type(frequenciesEachTrialOdd,arrayOfFrequenciesOdd)

    '''
    PSTH
    '''
    # Parameters
    binWidth = 0.010 # seconds
    timeVec = np.arange(timeRange[0],timeRange[-1],binWidth)
    smoothWinSizePsth = 5
    lwPsth = 2
    downsampleFactorPsth = 1

    iletLowFreqOddInStdPara = indexLimitsEachTrialStd[:,trialsEachCondStd[:,0]]
    spikeCountMatLowFreqOddInStdPara = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnsetStd,
                iletLowFreqOddInStdPara,timeVec)

    iletHighFreqStdInStdPara = indexLimitsEachTrialStd[:,trialsEachCondStd[:,1]]
    spikeCountMatHighFreqStdInStdPara = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnsetStd,
                iletHighFreqStdInStdPara,timeVec)

    iletLowFreqStdInOddPara = indexLimitsEachTrialOdd[:,trialsEachCondOdd[:,0]]
    spikeCountMatLowFreqStdInOddPara = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnsetOdd,
                iletLowFreqStdInOddPara,timeVec)

    iletHighFreqOddInOddPara = indexLimitsEachTrialOdd[:,trialsEachCondOdd[:,1]]
    spikeCountMatHighFreqOddInOddPara = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnsetOdd,
                iletHighFreqOddInOddPara,timeVec)

    '''
    plt.figure()
    extraplots.plot_psth(spikeCountMatHighFreqStdInStdPara/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond='r',linestyle=['dotted'],linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
    extraplots.plot_psth(spikeCountMatHighFreqOddInOddPara/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond='r',linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('Time from event onset [s]', fontsize=16)
    plt.ylabel('Firing Rate [Hz]', fontsize=16)
    plt.title('{} Hz Sound'.format(arrayOfFrequenciesOddkHz[1]))


    plt.figure()
    extraplots.plot_psth(spikeCountMatLowFreqStdInOddPara/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond=[(0.20,0.87,1.00)],linestyle=['dotted'],linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
    extraplots.plot_psth(spikeCountMatLowFreqOddInStdPara/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond=[(0.20,0.87,1.00)],linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('Time from event onset [s]', fontsize=16)
    plt.ylabel('Firing Rate [Hz]', fontsize=16)
    '''

    plt.figure()
    extraplots.plot_psth(spikeCountMatHighFreqStdInStdPara/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond='r',linestyle=['dotted'],linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
    extraplots.plot_psth(spikeCountMatHighFreqOddInOddPara/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond='r',linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
    extraplots.plot_psth(spikeCountMatLowFreqStdInOddPara/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond=[(0.20,0.87,1.00)],linestyle=['dotted'],linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
    extraplots.plot_psth(spikeCountMatLowFreqOddInStdPara/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond=[(0.20,0.87,1.00)],linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel('Time from event onset [s]', fontsize=18)
    plt.ylabel('Firing Rate [Hz]', fontsize=18)
    plt.legend(['High Freq Std', 'High Freq Odd', 'Low Freq Std', 'Low Freq Odd'])
    '''
    Saving the figure --------------------------------------------------------------
    '''
    figFilename ='{}_{}_{}um_T{}_c{}_psth.{}'.format(dbRow['subject'],dbRow['date'],dbRow['depth'],
            dbRow['tetrode'],dbRow['cluster'],figFormat)
    figFullpath = os.path.join(outputDir,figFilename)
    #plt.savefig(figFullpath,format=figFormat)
    plt.gcf().set_size_inches([6,5])
    plt.tight_layout()

    plt.show()
