from jaratoolbox import celldatabase
reload(celldatabase)

subject = 'd1pi041'
experiments=[]

exp0 = celldatabase.Experiment(subject, '2019-08-25', 'right_AudStr',
info=['anteriourDiI', 'TT1left', 'soundLeft', 'A4x2-tet'])
experiments.append(exp0)

#50 noiseburst, 50 laser pulse, 40 laser train, 160 tuningTest, 1760 tc, 220 AM
#Used left speaker;laser (445 nm) set to 2.0 mW; Probe C39A; Rig 2

"""
Laser Calibration
Power: Value on laser dial, value in output level
0.5: 1.5, 18.6
1.0: 2.0, 24.0
1.5: 2.6, 30.3
2.0: 3.3, 37.3
2.5: 4.0, 44.4
3.0: 4.85, 53.0
3.5: 5.85, 63.5
4.0: 6.75, 73.0
"""

# Animal in rig at: 12:43
# Probe in at: 1:36 (mouse bled a ton and had a lot of weird tissue blocking penetration)

exp0.add_site(2500, tetrodes=[2,4,6,7])
exp0.add_session('13-50-38', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('13-52-06', None, 'laserpulse', 'am_tuning_curve')

exp0.add_site(2700, tetrodes=[3,4,5,6,7,8])
exp0.add_session('13-58-53', None, 'laserpulse', 'am_tuning_curve')
exp0.add_session('14-00-14', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('14-02-14', 'a', 'tuningTest', 'am_tuning_curve')
exp0.add_session('14-05-14', None, 'lasertrain', 'am_tuning_curve')
exp0.add_session('14-07-06', 'b', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('14-35-40', 'c', 'am', 'am_tuning_curve')
exp0.add_session('14-42-01', None, 'laserpulse', 'am_tuning_curve')

exp0.add_site(2800, tetrodes=[4,5,6,7,8])
exp0.add_session('14-49-26', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('14-51-05', 'd', 'tuningTest', 'am_tuning_curve')

exp0.add_site(2900, tetrodes=[3,5,6,7,8])
exp0.add_session('15-00-45', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('15-02-03', 'e', 'tuningTest', 'am_tuning_curve')
exp0.add_session('15-05-11', 'f', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('15-33-43', 'g', 'am', 'am_tuning_curve')
exp0.add_session('15-39-47', None, 'laserpulse', 'am_tuning_curve')
exp0.add_session('15-41-10', None, 'lasertrain', 'am_tuning_curve')

exp0.add_site(3000, tetrodes=[1,3,5,6,7,8])
exp0.add_session('15-51-08', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('15-52-27', 'h', 'tuningTest', 'am_tuning_curve')
exp0.add_session('15-54-57', 'i', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('16-25-08', 'j', 'am', 'am_tuning_curve')
exp0.add_session('16-32-11', None, 'laserpulse', 'am_tuning_curve')
exp0.add_session('16-33-32', None, 'lasertrain', 'am_tuning_curve')

exp0.add_site(3100, tetrodes=[1,3,4,5,6,7,8])
exp0.add_session('16-42-17', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('16-43-36', 'k', 'tuningTest', 'am_tuning_curve')
exp0.add_session('16-46-07', 'l', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('17-14-51', 'm', 'am', 'am_tuning_curve')
exp0.add_session('17-21-04', None, 'laserpulse', 'am_tuning_curve')
exp0.add_session('17-22-09', None, 'lasertrain', 'am_tuning_curve')

exp0.add_site(3200, tetrodes=[1,3,4,5,6,7,8])
exp0.add_session('17-33-00', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('17-34-37', 'n', 'tuningTest', 'am_tuning_curve')
exp0.add_session('17-37-26', 'o', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('18-06-38', 'p', 'am', 'am_tuning_curve')
exp0.add_session('18-12-44', None, 'laserpulse', 'am_tuning_curve')
exp0.add_session('18-14-12', None, 'lasertrain', 'am_tuning_curve')

exp0.add_site(3300, tetrodes=[1,3,4,5,6,7,8])
exp0.add_session('18-40-43', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('18-42-02', 'q', 'tuningTest', 'am_tuning_curve')
exp0.add_session('18-44-44', 'r', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('19-16-14', 's', 'am', 'am_tuning_curve')
exp0.add_session('19-22-33', None, 'laserpulse', 'am_tuning_curve')
exp0.add_session('19-23-42', None, 'lasertrain', 'am_tuning_curve')

exp0.add_site(3400, tetrodes=[1,2,3,5,6,7,8])
exp0.add_session('19-35-43', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('19-37-02', 't', 'tuningTest', 'am_tuning_curve')
exp0.add_session('19-39-57', 'u', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('20-08-34', 'v', 'am', 'am_tuning_curve')
exp0.add_session('20-14-37', None, 'laserpulse', 'am_tuning_curve')
exp0.add_session('20-15-48', None, 'lasertrain', 'am_tuning_curve')

exp0.add_site(3500, tetrodes=[1,2,3,5,6,7,8])
exp0.add_session('20-31-06', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('20-32-26', 'w', 'tuningTest', 'am_tuning_curve')
exp0.add_session('20-35-00', 'x', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('21-03-33', 'y', 'am', 'am_tuning_curve')
exp0.add_session('21-09-37', None, 'laserpulse', 'am_tuning_curve')
exp0.add_session('21-10-48', None, 'lasertrain', 'am_tuning_curve')

exp0.add_site(3600, tetrodes=[1,2,4,5,6,7,8])
exp0.add_session('21-20-31', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('21-21-48', 'z', 'tuningTest', 'am_tuning_curve')
exp0.add_session('21-24-14', 'aa', 'tuningCurve', 'am_tuning_curve')
exp0.add_session('21-52-47', 'ab', 'am', 'am_tuning_curve')
exp0.add_session('21-58-51', None, 'laserpulse', 'am_tuning_curve')
exp0.add_session('22-00-02', None, 'lasertrain', 'am_tuning_curve')

exp0.add_site(3700, tetrodes=[1,2,4,5,6,7,8])
exp0.add_session('22-08-13', None, 'noiseburst', 'am_tuning_curve')
# no more sound responses

exp0.maxDepth = 3700

exp1 = celldatabase.Experiment(subject, '2019-08-27', 'right_AudStr',
info=['middleDiD', 'TT1left', 'soundLeft', 'A4x2-tet'])
experiments.append(exp1)

#50 noiseburst, 50 laser pulse, 40 laser train, 160 tuningTest, 1760 tc, 220 AM
#Used left speaker;laser (445 nm) set to 2.0 mW; Probe C39A; Rig 2

"""
Laser Calibration
Power: Value on laser dial, value in output level
0.5: 1.6, 19.9`
1.0: 2.40, 28.1
1.5: 3.25, 36.8
2.0: 4.05, 45.4
2.5: 5.17, 57.2
3.0: 6.28, 69.1
3.5: 7.50, 82.5
4.0: 9.90, 108.9
"""

# Animal in rig at: 11:08
# Probe in at: 11:24

exp1.add_site(2700, tetrodes=[1,3,6,7,8])
exp1.add_session('12-45-27', None, 'noiseburst', 'am_tuning_curve')
exp1.add_session('12-56-10', None, 'laserpulse', 'am_tuning_curve')
exp1.add_session('12-57-40', None, 'lasertrain', 'am_tuning_curve')
exp1.add_session('12-59-31', 'a', 'tuningTest', 'am_tuning_curve')

exp1.add_site(2800, tetrodes=[1,2,3,4,6,7,8])
exp1.add_session('13-18-21', None, 'noiseburst', 'am_tuning_curve')
exp1.add_session('13-20-20', None, 'laserpulse', 'am_tuning_curve')
exp1.add_session('13-21-49', None, 'lasertrain', 'am_tuning_curve')
exp1.add_session('13-23-25', 'b', 'tuningTest', 'am_tuning_curve')
exp1.add_session('13-27-40', 'c', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('13-56-26', 'd', 'am', 'am_tuning_curve')

exp1.add_site(2900, tetrodes=[1,2,6,8])
exp1.add_session('14-13-20', None, 'noiseburst', 'am_tuning_curve')
exp1.add_session('14-14-26', None, 'laserpulse', 'am_tuning_curve')
exp1.add_session('14-15-44', None, 'lasertrain', 'am_tuning_curve')
exp1.add_session('14-18-58', 'e', 'tuningTest', 'am_tuning_curve')

exp1.add_site(3000, tetrodes=[1,2,4,7,8])
exp1.add_session('14-33-45', None, 'noiseburst', 'am_tuning_curve')
exp1.add_session('14-35-03', None, 'laserpulse', 'am_tuning_curve')
exp1.add_session('14-36-32', None, 'lasertrain', 'am_tuning_curve')
exp1.add_session('14-39-11', 'f', 'tuningTest', 'am_tuning_curve')

exp1.add_site(3200, tetrodes=[1,2,4,5,7,8])
exp1.add_session('15-52-10', None, 'noiseburst', 'am_tuning_curve')
exp1.add_session('15-53-22', None, 'laserpulse', 'am_tuning_curve')
exp1.add_session('15-54-55', None, 'lasertrain', 'am_tuning_curve')
exp1.add_session('16-14-56', 'g', 'tuningTest', 'am_tuning_curve')
exp1.add_session('16-33-35', 'h', 'tuningCurve', 'am_tuning_curve')
exp1.add_session('17-29-41', 'i', 'am', 'am_tuning_curve')

exp1.add_site(3300, tetrodes=[1,2,4,5,7,8])
exp1.add_session('18-09-37', None, 'noiseburst', 'am_tuning_curve')
exp1.add_session('18-11-29', None, 'laserpulse', 'am_tuning_curve')
exp1.add_session('18-12-43', None, 'lasertrain', 'am_tuning_curve')
exp1.add_session('18-15-43', 'j', 'tuningTest', 'am_tuning_curve')

exp1.add_site(3400, tetrodes=[1,2,4,5,6,7,8])
exp1.add_session('18-28-04', None, 'noiseburst', 'am_tuning_curve')
exp1.add_session('18-29-17', None, 'laserpulse', 'am_tuning_curve')
exp1.add_session('18-30-30', None, 'lasertrain', 'am_tuning_curve')
exp1.add_session('18-32-01', 'k', 'tuningTest', 'am_tuning_curve')
exp1.add_session('18-35-30', 'l', 'tuningCurve', 'am_tuning_curve')

exp1.maxDepth = 3400
