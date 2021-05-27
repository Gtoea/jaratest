# TODO:
#    Recordings will not have sound trigger because we need to
#    fix sound sync in jaratoolbox.SOUND_SERVER

# PLAN:
#   ISIs: for 100ms, 1.2 +/- 0.2; for 500ms, 2 +/- 0.4
#   60dB 100ms white noise, 100 trials
#   frequency tuning: 70dB 100ms pure tones, 2 to 40kHz, 16 freq, 320 trials (20 per cond)
#   frequency tuning (with laser, if see tuning): same as above but 50 and 70dB and
#                                                 0.5 proportion laser, 1320 trials (20 per cond)
#   am tuning (with laser): 9 rates from 4 to 64Hz, 60dB, 0.5 sec, 0.5 proportion with laser,
#                           360 trials (20 per cond)

from jaratoolbox import celldatabase

subject = 'arch004'
experiments=[]

exp0 = celldatabase.Experiment(subject, '2021-05-26', 'left_AudStr', info=['TT1left', 'soundRight', 'A4x2-tet'])
experiments.append(exp0)

# Used right speaker; laser (520 nm) at 5mW; Probe DD02, no dye; Rig 2

"""
Laser Calibration
Power: Value on laser dial, value in output level
1.0: 3.9, 20.5
2.0: 5.0, 36.6
3.0: 6.0, 52.1
4.0: 7.0, 68.6
5.0: 8.05, 84.8
"""

# Animal in rig at: 9:30
# Probe in at: 10:25

# probe oriented along ML axis, but gets pushed a little L due to thickness of middle glue wall
# may attempt recording with probe oriented along AP axis in future

exp0.add_site(2800, tetrodes=[2,4,5,6]) # TT3 reference
exp0.add_session('10-56-01', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('10-59-01', 'a', 'tuningTest', 'am_tuning_curve')
exp0.add_session('11-06-51', 'b', 'laserAM', 'am_tuning_curve')
exp0.add_session('11-22-48', 'c', 'laserTuningCurve', 'am_tuning_curve')

exp0.add_site(3000, tetrodes=[1,2,4,5,6]) # TT3 reference
exp0.add_session('12-01-05', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('12-04-02', 'd', 'tuningTest', 'am_tuning_curve')
exp0.add_session('12-11-34', 'e', 'laserAM', 'am_tuning_curve')
exp0.add_session('12-27-23', 'f', 'laserTuningCurve', 'am_tuning_curve')

exp0.add_site(3200, tetrodes=[1,2,4,5,6]) # TT3 reference
exp0.add_session('13-06-32', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('13-09-02', 'g', 'tuningTest', 'am_tuning_curve')
exp0.add_session('13-17-17', 'h', 'laserAM', 'am_tuning_curve')
exp0.add_session('13-33-11', 'i', 'laserTuningCurve', 'am_tuning_curve')

exp0.add_site(3400, tetrodes=[1,2,4,5,6]) # TT3 reference
exp0.add_session('14-12-28', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('14-15-22', 'j', 'tuningTest', 'am_tuning_curve')
exp0.add_session('14-23-00', 'k', 'laserAM', 'am_tuning_curve')
exp0.add_session('14-39-13', 'l', 'laserTuningCurve', 'am_tuning_curve')

exp0.add_site(3600, tetrodes=[1,2,4,5,6]) # TT3 reference
exp0.add_session('15-14-45', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('15-18-56', 'm', 'tuningTest', 'am_tuning_curve')
exp0.add_session('15-26-41', 'n', 'laserAM', 'am_tuning_curve')
exp0.add_session('15-44-14', 'o', 'laserTuningCurve', 'am_tuning_curve')

# Animal out at: 4:25
exp0.maxDepth = 3600


exp1 = celldatabase.Experiment(subject, '2021-05-27', 'left_AudStr', info=['TT1ant', 'soundRight', 'A4x2-tet'])
experiments.append(exp1)

# Used right speaker; laser (520 nm) at 5mW; Probe DD02, no dye; Rig 2

"""
Laser Calibration
Power: Value on laser dial, value in output level
1.0: 3.9, 20.0
2.0: 4.9, 35.2
3.0: 5.9, 50.9
4.0: 6.9, 66.8
5.0: 7.85, 81.8
"""

# Animal in rig at: 8:43
# Probe in at: 9:01

# probe oriented along AP axis, inserted on medial side of craniotomy
# doing 160 trials of test tuning curve (10 trials per cond) to speed it up
# other sessions same as before

exp1.add_site(3000, tetrodes=[1,2,3,5,6]) # TT4 reference
exp1.add_session('09-07-50', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('09-10-21', 'a', 'tuningTest', 'am_tuning_curve')
exp1.add_session('09-14-41', 'b', 'laserAM', 'am_tuning_curve')
exp1.add_session('09-31-28', 'c', 'laserTuningCurve', 'am_tuning_curve')

exp1.add_site(3200, tetrodes=[1,2,4,5,6]) # TT3 reference
exp1.add_session('10-11-12', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('10-13-44', 'd', 'tuningTest', 'am_tuning_curve')
exp1.add_session('10-17-45', 'e', 'laserAM', 'am_tuning_curve')

exp1.add_site(3400, tetrodes=[1,2,3,4,6]) # TT5 reference
exp1.add_session('10-41-33', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('10-44-05', 'f', 'tuningTest', 'am_tuning_curve')
exp1.add_session('10-48-08', 'g', 'laserAM', 'am_tuning_curve')
exp1.add_session('11-03-57', 'h', 'laserTuningCurve', 'am_tuning_curve')

exp1.add_site(3600, tetrodes=[1,2,3,4,5]) # TT6 reference
exp1.add_session('11-45-47', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('11-48-19', 'i', 'tuningTest', 'am_tuning_curve')
exp1.add_session('11-52-16', 'j', 'laserAM', 'am_tuning_curve')
exp1.add_session('12-08-06', 'k', 'laserTuningCurve', 'am_tuning_curve')

exp1.add_site(3700, tetrodes=[1,2,3,4,6]) # TT5 reference
exp1.add_session('12-44-47', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('12-47-22', 'l', 'tuningTest', 'am_tuning_curve')
exp1.add_session('12-51-22', 'm', 'laserAM', 'am_tuning_curve')
exp1.add_session('13-07-26', 'n', 'laserTuningCurve', 'am_tuning_curve')

# Animal out at: 1:48
exp0.maxDepth = 3700
