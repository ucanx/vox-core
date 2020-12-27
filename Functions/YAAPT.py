import amfm_decompy.pYAAPT as pYAAPT


def YAAPT_fundamental_freq(signal, frame_length=40, tda_frame_length=40, f0_min=70, f0_max=600):
    pitchY = pYAAPT.yaapt(signal, frame_length=frame_length, tda_frame_length=tda_frame_length, f0_min=f0_min,
                          f0_max=f0_max)
    data_YAAPT = pitchY.samp_values
    mean_freq = 0
    x_total = 0
    total = 0
    for i in range(len(data_YAAPT)):

        if data_YAAPT[i] > 10:
            x_total += data_YAAPT[i]
            total += 1

    mean_freq = x_total / total
    # mean_freq=mean_freq.astype(int)
    # mean_freq=int(mean_freq)
    # print('tyeper',type(mean_freq))

    # return mean frequency of wave file
    return mean_freq