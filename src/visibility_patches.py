import numpy as np

#Athor: Athos M. Moraes
#Reference: https://github.com/Jaia89/Image_Visibility

def visibility_patches(I, stride, criterion):
    motif_size = 3
    pow2 = np.array([1, 2, 4, 8, 16, 32, 64, 128])

    n_rows, n_cols = I.shape[:2]

    stride = round(stride)

    if n_rows != n_cols:
        raise ValueError("Input image must be square")

    if stride >= n_rows - motif_size + 1 or stride >= n_cols - motif_size + 1:
        raise ValueError("Stride length exceeds image size")

    if criterion not in ['horizontal', 'natural']:
        raise ValueError("Criterion string must be 'natural' or 'horizontal'")

    Z = []
    I = I.astype(float)

    if criterion == 'horizontal':

        for m in range(I.shape[2]):

            Freq = np.zeros(256)
            count = 0

            for i in range(0, n_rows - motif_size + 1, stride):
                for j in range(0, n_cols - motif_size + 1, stride):

                    count += 1
                    string = np.zeros(8)
                    M = I[i:i + motif_size, j:j + motif_size, m]

                    if M[0, 0] > M[0, 1] and M[0, 2] > M[0, 1]:
                        string[0] = 1

                    if M[0, 2] > M[1, 2] and M[2, 2] > M[1, 2]:
                        string[1] = 1

                    if M[2, 0] > M[2, 1] and M[2, 2] > M[2, 1]:
                        string[2] = 1

                    if M[0, 0] > M[1, 0] and M[2, 0] > M[1, 0]:
                        string[3] = 1

                    if M[0, 1] > M[1, 1] and M[2, 1] > M[1, 1]:
                        string[4] = 1

                    if M[1, 0] > M[1, 1] and M[1, 2] > M[1, 1]:
                        string[5] = 1

                    if M[0, 0] > M[1, 1] and M[2, 2] > M[1, 1]:
                        string[6] = 1

                    if M[0, 2] > M[1, 1] and M[2, 0] > M[1, 1]:
                        string[7] = 1

                    label = int(np.sum(string * pow2))
                    Freq[label] += 1

            Freq /= count
            Z.append(Freq)

    if criterion == 'natural':

        for m in range(I.shape[2]):

            Freq = np.zeros(256)
            count = 0

            for i in range(0, n_rows - motif_size + 1, stride):
                for j in range(0, n_cols - motif_size + 1, stride):

                    count += 1
                    string = np.zeros(8)
                    M = I[i:i + motif_size, j:j + motif_size, m]

                    if M[0, 2] > 2 * M[0, 1] - M[0, 0]:
                        string[0] = 1

                    if M[2, 2] > 2 * M[1, 2] - M[0, 2]:
                        string[1] = 1

                    if M[2, 0] > 2 * M[2, 1] - M[2, 2]:
                        string[2] = 1

                    if M[0, 0] > 2 * M[1, 0] - M[2, 0]:
                        string[3] = 1

                    if M[2, 1] > 2 * M[1, 1] - M[0, 1]:
                        string[4] = 1

                    if M[1, 2] > 2 * M[1, 1] - M[1, 0]:
                        string[5] = 1

                    if M[2, 2] > 2 * M[1, 1] - M[0, 0]:
                        string[6] = 1

                    if M[2, 0] > 2 * M[1, 1] - M[0, 2]:
                        string[7] = 1

                    label = int(np.sum(string * pow2))
                    Freq[label] += 1

            Freq /= count
            Z.append(Freq)

    return np.array(Z)