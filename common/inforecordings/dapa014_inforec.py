from jaratoolbox import celldatabase
reload(celldatabase)

subject = 'dapa014'
experiments=[]


exp0 = celldatabase.Experiment(subject, '2018-04-23', 'left_AudStr', info=['FacingPosterior', 'AnteriorDiI'])
experiments.append(exp0)
#Used both speakers; 2.5 mW for laser; probe DAF4

exp0.laserCalibration = {
    '0.5':0.8,
    '1.0':1.3,
    '1.5':1.8,
    '2.0':2.3,
    '2.5':2.8,
    '3.0':3.4,
    '3.5':4.25,
    '4.0':5.05
}

#Tetrode 7 has reference; threshold set to 55mV
exp0.add_site(2900, tetrodes=[1,3,4,5,6])
exp0.add_session('16-05-43', None, 'noisebursts', 'am_tuning_curve')
#exp0.add_session('16-10-06', 'k', 'tuningCurve', 'am_tuning_curve')
#exp0.add_session('16-13-16', 'l', 'tuningCurve', 'am_tuning_curve')
#exp0.add_session('16-27-15', 'm', 'laserTuningCurve', 'laser_am_tuning_curve')

exp1 = celldatabase.Experiment(subject, '2018-04-24', 'left_AudStr', info=['FacingPosterior', 'AnteriorMidDiD'])
experiments.append(exp1)
#Used both speakers; 2.5 mW for laser; probe DAF4

exp1.laserCalibration = {
    '0.5':0.95,
    '1.0':1.55,
    '1.5':2.1,
    '2.0':2.7,
    '2.5':3.3,
    '3.0':4.3,
    '3.5':5.3,
    '4.0':6.4
}

#Tetrode 1 has reference; threshold set to 55mV
exp1.add_site(2900, tetrodes=[2,3,4,5,6])
exp1.add_session('13-03-16', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('13-05-07', 'a', 'tuningCurve', 'am_tuning_curve')

exp1.add_site(2950, tetrodes=[2,3,4,5,6])
exp1.add_session('13-11-46', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('13-14-38', 'b', 'tuningCurve', 'am_tuning_curve')

exp1.add_site(3000, tetrodes=[2,3,4,5,6])
exp1.add_session('13-21-09', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('13-23-10', 'c', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('13-29-00', 'd', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('13-43-51', 'e', 'laserTuningCurve', 'laser_am_tuning_curve')

exp1.add_site(3050, tetrodes=[2,3,4,5,6])
exp1.add_session('14-23-44', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('14-25-34', 'f', 'tuningCurve', 'am_tuning_curve')

exp1.add_site(3100, tetrodes=[2,3,4,5,6])
exp1.add_session('14-31-05', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('14-33-07', 'g', 'tuningCurve', 'am_tuning_curve')

exp1.add_site(3150, tetrodes=[2,3,4,5,6])
exp1.add_session('14-38-45', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('14-40-50', 'h', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('14-44-28', 'i', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('14-58-10', 'j', 'laserTuningCurve', 'laser_am_tuning_curve')

exp1.add_site(3200, tetrodes=[2,3,4,5,6])
exp1.add_session('15-28-33', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('15-30-14', 'k', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('15-34-13', 'l', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('15-47-23', 'm', 'laserTuningCurve', 'laser_am_tuning_curve')

exp1.add_site(3250, tetrodes=[2,3,4,5,6])
exp1.add_session('16-17-32', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('16-18-40', 'n', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('16-22-19', 'o', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('16-35-28', 'p', 'laserTuningCurve', 'laser_am_tuning_curve')

exp1.add_site(3300, tetrodes=[2,3,4,5,6])
exp1.add_session('17-04-57', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('17-06-41', 'q', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('17-09-16', 'r', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('17-22-23', 's', 'laserTuningCurve', 'laser_am_tuning_curve')


exp2 = celldatabase.Experiment(subject, '2018-04-25', 'left_AudStr', info=['FacingPosterior', 'PosteriorMidDiI'])
experiments.append(exp2)
#Used both speakers; 2.5 mW for laser; probe DAF4

exp2.laserCalibration = {
    '0.5':0.75,
    '1.0':1.1,
    '1.5':1.5,
    '2.0':1.95,
    '2.5':2.3,
    '3.0':2.8,
    '3.5':3.3,
    '4.0':4.0
}

#Tetrode 1 has reference; threshold set to 55mV
exp2.add_site(2900, tetrodes=[2,3,4,5,6])
exp2.add_session('12-09-48', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('12-11-53', 'a', 'tuningCurve', 'am_tuning_curve')

exp2.add_site(2950, tetrodes=[2,3,4,5,6])
exp2.add_session('12-17-38', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('12-19-01', 'b', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('12-22-02', 'c', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('12-35-15', 'd', 'laserTuningCurve', 'laser_am_tuning_curve')

exp2.add_site(3000, tetrodes=[2,3,4,5,6])
exp2.add_session('13-07-28', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('13-09-17', 'e', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('13-11-51', 'f', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('13-24-59', 'g', 'laserTuningCurve', 'laser_am_tuning_curve')

exp2.add_site(3050, tetrodes=[2,3,4,5,6])
exp2.add_session('13-55-45', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('13-57-37', 'h', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('14-01-11', 'i', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('14-15-19', 'j', 'laserTuningCurve', 'laser_am_tuning_curve')

exp2.add_site(3100, tetrodes=[2,3,4,5,6])
exp2.add_session('14-48-37', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('14-49-57', 'k', 'tuningCurve', 'am_tuning_curve')

exp2.add_site(3150, tetrodes=[2,3,4,5,6])
exp2.add_session('14-53-41', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('14-54-58', 'l', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('14-57-30', 'm', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('15-11-42', 'n', 'laserTuningCurve', 'laser_am_tuning_curve')

exp2.add_site(3200, tetrodes=[2,3,4,5,6])
exp2.add_session('15-42-27', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('15-43-40', 'o', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('15-45-59', 'p', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('15-59-04', 'q', 'laserTuningCurve', 'laser_am_tuning_curve')
