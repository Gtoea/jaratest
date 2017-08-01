import os
import pandas as pd
import numpy as np
from jaratoolbox import settings
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pdb
import itertools

animalLists = ['adap042', 'adap043','adap044', 'adap046','adap047'] #adap041 did not have enough data

#plotAll = True
#normalized = False
logscaled = True

tuningIntensities = [40, 50, 60, 70]
astrRegions = ['medial','lateral']
qualityThreshold = 3 
maxZThreshold = 2
ISIcutoff = 0.02
intensityToPlot = 60 # The intensity that showed the most diff between 'medial' and 'lateral' cells
#responsiveFreqs = {}

# Tetrode to shank mappings
ttsToShank = {'1':[1,2],
              '2':[3,4],
              '3':[5,6],
              '4':[7,8]}

# -- Make composite celldb -- #
allMiceDfs = []
for animal in animalLists:
    databaseFullPath = os.path.join(settings.DATABASE_PATH, '{}_database.h5'.format(animal))
    key = 'head_fixed'
    celldbThisMouse = pd.read_hdf(databaseFullPath, key=key)
    allMiceDfs.append(celldbThisMouse)
    
celldb = pd.concat(allMiceDfs, ignore_index=True)

# -- Plot histogram of responsive freqs by medial-lateral location -- #
goodQualCells = celldb.query("isiViolations<{} and shapeQuality>{} and astrRegion!='undefined' and astrRegion!='undetermined'".format(ISIcutoff, qualityThreshold))

maxZscore = goodQualCells.ZscoreEachIntensity.apply(lambda x : np.max(np.abs(x)))
goodRespCells=goodQualCells[maxZscore >= maxZThreshold]


outputDir = '/home/languo/data/ephys/head_fixed_astr/all_mice/responsive_freqs_by_location/'
if not os.path.exists(outputDir):
    os.mkdir(outputDir)
#freqs = goodQualCells.tuningFreqs.iloc[0]

#if plotAll:
cellsToPlot = goodQualCells
#else:
#   cellsToPlot = goodRespCells

# -- Calculate responsive freqs for each cell and add it as a column to cellsToPlot-- #
indi = tuningIntensities.index(intensityToPlot)
zScoresThisIntensity = cellsToPlot.tuningZscoreEachIntEachFreq.apply(lambda x: x[indi]) #select just the zScores for that intensity
   
responseEachFreqThisIntensity = zScoresThisIntensity.apply(lambda x: (np.abs(x)>=maxZThreshold))
tuningFreqsThisIntensity = cellsToPlot.tuningFreqs.to_frame()
    
def selectFreqs(row):
    #print row.name, row.tuningFreqs.values
    #print row.name, responseEachFreqThisIntensity.loc[row.name].values
    freqs = tuple(row.tuningFreqs.values[responseEachFreqThisIntensity.loc[row.name].values])
    print freqs
    return freqs

def selectZscores(row):
    zScores = tuple(np.array(row.tuningZscoreEachIntEachFreq)[responseEachFreqThisIntensity.loc[row.name].values])
    print zScores
    return zScores

responsiveFreqsThisIntensity = pd.Series(dtype=object)
responsiveFreqsThisIntensity = tuningFreqsThisIntensity.apply(selectFreqs, axis=1) #This is a pd series where each cell is a tuple containing the responsive freqs (if none then it's an empty tuple)
zScoresThisIntensity = zScoresThisIntensity.to_frame()
zScoresEachRespFreq = zScoresThisIntensity.apply(selectZscores, axis=1)

if logscaled:
    responsiveFreqsThisIntensity = responsiveFreqsThisIntensity.apply(lambda x: np.log2(x))
cellsToPlot['responsiveFreqs60dB'] = responsiveFreqsThisIntensity
cellsToPlot['zScores60dBEachRespFreq'] = zScoresEachRespFreq
cellsToPlot['zThreshold'] = maxZThreshold

outputDf = pd.DataFrame(columns=['animal','brainArea','expInd','shank1_freq','shank2_freq','shank3_freq','shank4_freq','shank1_zScore','shank2_zScore','shank3_zScore','shank4_zScore','shank1_weightedFreq','shank2_weightedFreq','shank3_weightedFreq','shank4_weightedFreq'])
#outputDf.astype(dtype={})
for inda, brainArea in enumerate(np.unique(cellsToPlot.brainarea)): 
    thisArea = cellsToPlot.loc[cellsToPlot.brainarea==brainArea]
    for animal in np.unique(thisArea.animalName):
        thisAnimal = thisArea.loc[thisArea.animalName == animal]
        experiments = np.unique(thisAnimal.indExperiment)
        numExps = len(experiments)
        plt.gcf()
        fig, axes = plt.subplots(nrows=1, ncols=numExps, sharex=True, sharey='row')
        for inde,exp in enumerate(experiments):
            thisExp = thisAnimal.loc[thisAnimal.indExperiment == exp]
            dictThisExp = {'animal':animal, 'brainArea':brainArea, 'expInd':inde}
            for shank in ttsToShank.keys():
                ttsThisShank = ttsToShank[shank]
                cellsThisShank = thisExp.loc[thisExp.tetrode.isin(ttsThisShank)]
                if len(cellsThisShank):
                    freqsThisShank = np.concatenate(cellsThisShank.responsiveFreqs60dB.values)
                    zScoresThisShank = np.concatenate(cellsThisShank.zScores60dBEachRespFreq.values)
                    dictThisExp['shank{}_freq'.format(shank)] = freqsThisShank
                    dictThisExp['shank{}_zScore'.format(shank)] = zScoresThisShank
                    print 'shank {} has these freqs:'.format(shank),len(freqsThisShank)
                    ax = axes[inde]
                    randOffset = 0.2*(np.random.rand(len(freqsThisShank))-0.5)
                    ax.scatter(int(shank)+randOffset, freqsThisShank)
                    ax.plot(0.2*np.array([-0.5,0.5])+int(shank), np.tile(np.mean(freqsThisShank),2), lw=1.5, color='grey')
                    ax.set_xticks([1,2,3,4])
                    ax.set_xticklabels(['shank1', 'shank2', 'shank3', 'shank4'])
                    ax.set_title('Exp {}'.format(inde))
                    ax.set_xlim([0,5])
                else:
                    dictThisExp['shank{}_freq'.format(shank)] = np.array([])
                    dictThisExp['shank{}_zScore'.format(shank)] = np.array([])
            outputDf = outputDf.append(dictThisExp, ignore_index=True)
            fig.set_tight_layout({'rect': [0.02, 0.02, 1, 0.95], 'w_pad': 0.06, 'h_pad': 0.05})  
            fig.text(0.5, 0.02, 'Experiments', ha='center', va='center')
            fig.text(0.02, 0.5, 'Preferred frequency (logscaled)', ha='center', va='center', rotation='vertical')
            plt.suptitle(animal+'_'+brainArea)
            #pdb.set_trace()
            #plt.show()
            figname = 'freqs_by_shanks'+animal+'_'+brainArea
            figFullPath = os.path.join(outputDir, figname)
            plt.savefig(figFullPath, format='png')

shanks = ['shank1','shank2','shank3','shank4']
for indr, row in outputDf.iterrows():
    for shank in shanks:
        if np.any(row[shank+'_freq']):
            row[shank+'_weightedFreq'] = sum(row[shank+'_freq'].values * row[shank+'_zScore'].values)/sum(row[shank+'_zScore'].values)
        else:
            row[shank+'_weightedFreq'] = np.NaN

plt.gcf()
plt.clf()
increaseCount = 0
decreaseCount = 0
for indr, row in outputDf.iterrows():
    for pairOfShanks in [list(x) for x in itertools.combinations(['shank1_weightedFreq','shank2_weightedFreq','shank3_weightedFreq','shank4_weightedFreq'],2)]:
        pairOfFreqs = row[pairOfShanks].values.astype(float)
        if not np.isnan(pairOfFreqs).any():
            line = plt.plot([1,2],pairOfFreqs, 'o-', mfc='k', mec='none')
            if pairOfFreqs[1] > pairOfFreqs[0]:
                increaseCount += 1
            elif pairOfFreqs[1] < pairOfFreqs[0]:
                decreaseCount += 1
            plt.setp(line, color='k', linewidth=1.5)
plt.xticks([1,2], ['left shank', 'right shank'])       
plt.xlim([0.5,2.5])
print 'number of pairs with increase:', increaseCount, 'number of pairs with decrease:', decreaseCount
figname = 'responsive_freqs_left_vs_right_shank'
figFullPath = os.path.join(outputDir, figname)
plt.savefig(figFullPath, format='svg')
#plt.show()


outputDf['zThreshold'] = maxZThreshold
outputDf['script'] = os.path.realpath(__file__)
dfName = 'responsive_freqs_each_shank_by_exp_headfixed_astr.h5'
outputDf.to_hdf(os.path.join(outputDir, dfName), key='headfixed')
