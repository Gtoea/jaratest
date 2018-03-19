from jaratoolbox import celldatabase
reload(celldatabase)

subject = 'band055'
experiments=[]

exp0 = celldatabase.Experiment(subject, '2018-03-14', 'right_AC', info=['medialDiI','TT1ant','soundleft'])
experiments.append(exp0)

exp0.laserCalibration = {
    '1.0':3.4,
    '2.0':3.8,
    '3.0':4.4,
    '4.0':4.9,
    '5.0':5.4,
    '7.5':6.75,
    '10.0':8.05
}

#trying 5mW laser to start
exp0.add_site(900, tetrodes=[1,2,4,6,8])
exp0.add_session('10-57-53', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('11-01-37', None, 'lasernoisebursts', 'bandwidth_am')
#no particular difference between laser and non-laser trials

exp0.add_site(925, tetrodes=[1,2,4,6,8])
exp0.add_session('11-21-00', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('11-22-13', None, 'lasernoisebursts', 'bandwidth_am')

exp0.add_site(950, tetrodes=[1,2,4,6,8])
exp0.add_session('11-35-36', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('11-36-54', None, 'lasernoisebursts', 'bandwidth_am')
exp0.add_session('11-39-05', 'a', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('11-47-24', 'b', 'AM', 'am_tuning_curve')
exp0.add_session('11-54-25', 'c', 'laserBandwidth', 'bandwidth_am')

exp0.add_site(1000, tetrodes=[1,2,4,6,8])
exp0.add_session('12-36-24', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('12-37-52', None, 'lasernoisebursts', 'bandwidth_am')
#laser up to 7.5mW
exp0.add_session('12-40-04', None, 'lasernoisebursts', 'bandwidth_am')
exp0.add_session('12-42-31', 'd', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('12-52-35', 'e', 'AM', 'am_tuning_curve')
exp0.add_session('12-58-32', 'f', 'laserBandwidth', 'bandwidth_am')
exp0.add_session('13-22-58', 'g', 'noiseAmps', 'am_tuning_curve')

exp0.add_site(1150, tetrodes=[1,2,3,4,6,8])
exp0.add_session('14-42-08', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('14-43-22', None, 'lasernoisebursts', 'bandwidth_am')

exp0.add_site(1175, tetrodes=[1,2,3,4,6,8])
exp0.add_session('15-22-55', None, 'noisebursts', 'am_tuning_curve')

exp0.add_site(1200, tetrodes=[2,4,8])
exp0.add_session('15-41-41', None, 'noisebursts', 'am_tuning_curve')

exp0.add_site(1250, tetrodes=[1,2,4,6,7,8])
exp0.add_session('15-51-35', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('15-52-46', None, 'lasernoisebursts', 'bandwidth_am')
exp0.add_session('15-55-11', 'h', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('16-03-24', 'i', 'AM', 'am_tuning_curve')
exp0.add_session('16-09-57', 'j', 'laserBandwidth', 'bandwidth_am')
exp0.add_session('16-36-36', 'k', 'noiseAmps', 'am_tuning_curve')

exp0.add_site(1300, tetrodes=[1,2,4,6,7,8])
exp0.add_session('16-54-33', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('16-55-52', None, 'lasernoisebursts', 'bandwidth_am')
exp0.add_session('16-58-12', 'l', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('17-06-49', 'm', 'AM', 'am_tuning_curve')
exp0.add_session('17-13-49', 'n', 'laserBandwidth', 'bandwidth_am')
exp0.add_session('17-39-15', 'o', 'noiseAmps', 'am_tuning_curve')

exp0.add_site(1375, tetrodes=[1,2,4,6,7,8])
exp0.add_session('17-54-33', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('17-56-01', None, 'lasernoisebursts', 'bandwidth_am') #back to 5mW
exp0.add_session('17-58-00', 'p', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('18-06-48', 'q', 'AM', 'am_tuning_curve')
exp0.add_session('18-13-01', 'r', 'laserBandwidth', 'bandwidth_am')
exp0.add_session('18-40-19', 's', 'noiseAmps', 'am_tuning_curve')

exp0.add_site(1425, tetrodes=[1,2,4,5,6,7,8])
exp0.add_session('18-57-17', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('18-58-47', None, 'lasernoisebursts', 'bandwidth_am')
exp0.add_session('19-00-05', 't', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('19-08-18', 'u', 'AM', 'am_tuning_curve')
#looks like same cells as previous site


exp1 = celldatabase.Experiment(subject, '2018-03-15', 'right_AC', info=['middleDiD','TT1ant','soundleft'])
experiments.append(exp1)

exp1.laserCalibration = {
    '1.0':3.3,
    '2.0':3.8,
    '3.0':4.45,
    '4.0':5.05,
    '5.0':5.65,
    '7.5':7.1,
    '10.0':8.5
}

exp1.add_site(900, tetrodes=[1,2,4,6,8])
exp1.add_session('12-59-10', None, 'noisebursts', 'am_tuning_curve')

exp1.add_site(950, tetrodes=[1,2,4,6,8])
exp1.add_session('13-07-32', None, 'noisebursts', 'am_tuning_curve')

exp1.add_site(1000, tetrodes=[1,2,4,6,8])
exp1.add_session('13-17-09', None, 'noisebursts', 'am_tuning_curve')

exp1.add_site(1050, tetrodes=[1,2,4,5,6,8])
exp1.add_session('13-36-04', None, 'noisebursts', 'am_tuning_curve')

exp1.add_site(1075, tetrodes=[1,2,4,5,6,7,8])
exp1.add_session('13-55-06', None, 'noisebursts', 'am_tuning_curve')

exp1.add_site(1100, tetrodes=[1,2,4,5,6,7,8])
exp1.add_session('14-03-40', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('14-04-50', None, 'lasernoisebursts', 'bandwidth_am')

exp1.add_site(1125, tetrodes=[1,2,4,6,7,8])
exp1.add_session('14-25-05', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('14-26-28', None, 'lasernoisebursts', 'bandwidth_am')
exp1.add_session('14-28-14', 'a', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('14-36-30', 'b', 'AM', 'am_tuning_curve')
exp1.add_session('14-43-49', 'c', 'laserBandwidth', 'bandwidth_am')
exp1.add_session('15-10-18', 'd', 'noiseAmps', 'am_tuning_curve')

exp1.add_site(1200, tetrodes=[2,4,6,7,8])
exp1.add_session('15-32-45', None, 'noisebursts', 'am_tuning_curve')

exp1.add_site(1250, tetrodes=[1,2,4,6,7,8])
exp1.add_session('15-44-01', None, 'noisebursts', 'am_tuning_curve')

exp1.add_site(1275, tetrodes=[1,2,4,6,7,8])
exp1.add_session('15-50-28', None, 'noisebursts', 'am_tuning_curve')

exp1.add_site(1300, tetrodes=[1,2,4,5,6,7,8])
exp1.add_session('16-05-49', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('16-06-45', None, 'lasernoisebursts', 'bandwidth_am')
exp1.add_session('16-08-31', 'e', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('16-13-31', 'f', 'AM', 'am_tuning_curve')
exp1.add_session('16-21-52', 'g', 'laserBandwidth', 'bandwidth_am')
exp1.add_session('16-46-43', 'h', 'noiseAmps', 'am_tuning_curve')

exp1.add_site(1400, tetrodes=[1,2,4,5,6,7,8])
exp1.add_session('17-04-09', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('17-05-25', None, 'lasernoisebursts', 'bandwidth_am')
exp1.add_session('17-07-23', 'i', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('17-13-15', 'j', 'AM', 'am_tuning_curve')
exp1.add_session('17-21-30', 'k', 'laserBandwidth', 'bandwidth_am')
exp1.add_session('17-45-57', 'l', 'laserBandwidth', 'bandwidth_am')
exp1.add_session('18-10-51', 'm', 'noiseAmps', 'am_tuning_curve')

exp1.add_site(1500, tetrodes=[1,2,4,5,6,7,8])
exp1.add_session('18-31-54', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('18-33-20', None, 'lasernoisebursts', 'am_tuning_curve')
exp1.add_session('18-34-54', 'n', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('18-40-40', 'o', 'AM', 'am_tuning_curve')
exp1.add_session('18-48-05', 'p', 'laserBandwidth', 'bandwidth_am')
exp1.add_session('19-13-41', 'q', 'noiseAmps', 'am_tuning_curve')


exp2 = celldatabase.Experiment(subject, '2018-03-16', 'right_AC', info=['lateralDiI','TT1ant','soundleft'])
experiments.append(exp2)

exp2.laserCalibration = {
    '1.0':3.3,
    '2.0':3.8,
    '3.0':4.3,
    '4.0':4.85,
    '5.0':5.4,
    '7.5':6.7,
    '10.0':8.05
}

exp2.add_site(1000, tetrodes=[1,2,4,6,8])
exp2.add_session('10-19-15', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('10-20-40', None, 'lasernoisebursts', 'bandwidth_am')
exp2.add_session('10-22-52', 'a', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('10-27-52', 'b', 'AM', 'am_tuning_curve')
exp2.add_session('10-34-14', 'c', 'laserBandwidth', 'bandwidth_am')
exp2.add_session('10-59-25', 'd', 'noiseAmps', 'am_tuning_curve')

exp2.add_site(1100, tetrodes=[2,4,6,8])
exp2.add_session('11-23-17', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('11-24-29', None, 'lasernoisebursts', 'bandwidth_am')
exp2.add_session('11-26-03', 'e', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('11-31-25', 'f', 'AM', 'am_tuning_curve')
exp2.add_session('11-38-54', 'g', 'laserBandwidth', 'bandwidth_am')
exp2.add_session('12-03-01', 'h', 'noiseAmps', 'am_tuning_curve')

exp2.add_site(1200, tetrodes=[1,2,4,6,8])
exp2.add_session('12-31-55', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('12-33-40', None, 'lasernoisebursts', 'bandwidth_am')
exp2.add_session('12-35-51', 'i', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('12-40-33', 'j', 'AM', 'am_tuning_curve')
exp2.add_session('12-48-42', 'k', 'laserBandwidth', 'bandwidth_am')
exp2.add_session('13-13-51', 'l', 'noiseAmps', 'am_tuning_curve')

exp2.add_site(1300, tetrodes=[1,2,3,4,6,8])
exp2.add_session('13-34-01', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('13-35-20', None, 'lasernoisebursts', 'bandwidth_am')
exp2.add_session('13-36-41', 'm', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('13-41-33', 'n', 'AM', 'am_tuning_curve')
exp2.add_session('13-50-26', 'o', 'laserBandwidth', 'bandwidth_am')
exp2.add_session('14-14-51', 'p', 'laserBandwidth', 'bandwidth_am')
exp2.add_session('14-41-25', 'q', 'noiseAmps', 'am_tuning_curve')

exp2.add_site(1400, tetrodes=[1,2,3,4,6,8])
exp2.add_session('14-56-45', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('14-58-03', None, 'lasernoisebursts', 'bandwidth_am')
exp2.add_session('14-59-20', 'r', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('15-06-24', 's', 'tuningCurve', 'am_tuning_curve') #accidentally started moving probe cause I forgot what I was doing, moved back and rerecording
exp2.add_session('15-10-53', 't', 'AM', 'am_tuning_curve')
exp2.add_session('15-19-16', 'u', 'laserBandwidth', 'bandwidth_am')
exp2.add_session('15-43-51', 'v', 'laserBandwidth', 'bandwidth_am')
exp2.add_session('16-08-04', 'w', 'noiseAmps','am_tuning_curve')

exp2.add_site(1500, tetrodes=[1,2,3,4,5,6,8])
exp2.add_session('16-25-53', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('16-27-21', None, 'lasernoisebursts', 'bandwidth_am')
exp2.add_session('16-29-15', 'x', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('16-33-52', 'y', 'AM', 'am_tuning_curve')
exp2.add_session('16-41-51', 'z', 'laserBandwidth', 'bandwidth_am')
exp2.add_session('17-05-51', 'aa', 'laserBandwidth', 'bandwidth_am')
exp2.add_session('17-30-53', 'ab', 'noiseAmps', 'am_tuning_curve')

exp2.add_site(1600, tetrodes=[1,2,3,4,5,6,8])
exp2.add_session('17-47-15', None, 'noisebursts', 'am_tuning_curve')
exp2.add_session('17-48-37', None, 'lasernoisebursts', 'bandwidth_am')
exp2.add_session('17-50-00', 'ac', 'tuningCurve', 'am_tuning_curve')
exp2.add_session('17-55-53', 'ad', 'AM', 'am_tuning_curve')
exp2.add_session('18-03-58', 'ae', 'laserBandwidth', 'bandwidth_am')
exp2.add_session('18-28-24', 'af', 'laserBandwidth', 'bandwidth_am')
exp2.add_session('18-52-21', 'ag', 'noiseAmps', 'am_tuning_curve')
