import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_pred, y_true, label_names):
    cm = confusion_matrix(y_true, y_pred)
    
    cm_norm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    
    fig, ax = plt.subplots(figsize=(8, 8))
    im = ax.imshow(cm_norm, interpolation='nearest', cmap=plt.cm.Blues)
    ax.figure.colorbar(im, ax=ax)
    
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=label_names.values(), yticklabels=label_names.values(),
           xlabel='Predicted label', ylabel='True label')
    
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    thresh = cm_norm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, "{:.2f}\n({})".format(cm_norm[i, j], cm[i, j]),
                    ha="center", va="center", color="white" if cm_norm[i, j] > thresh else "black")
    
    ax.set_title("Normalized Confusion Matrix")
    
    plt.show()

def plot_images(images, labels, n_cols=4, figsize=(10,10)):
    n_rows = int(np.ceil(len(images)/n_cols))

    fig, axs = plt.subplots(n_rows, n_cols, figsize=figsize)
    fig.subplots_adjust(hspace=0.2, wspace=0.1, top=0.95, bottom=0.05)

    for i, (image, label) in enumerate(zip(images, labels)):
        row_idx = i // n_cols
        col_idx = i % n_cols

        ax = axs[row_idx, col_idx]
        ax.imshow(image)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f"{label}", fontsize=8)

    for i in range(len(images), n_rows * n_cols):
        row_idx = i // n_cols
        col_idx = i % n_cols

        ax = axs[row_idx, col_idx]
        ax.axis('off')
    
    fig.tight_layout()

    plt.show()

def degree_distribution(graph, maxK):
    Pk = []
    Deg_seq = np.array(list(dict(graph.degree()).values()))
    Pk.append(np.histogram(Deg_seq, bins=np.arange(1, maxK+2), density=True)[0])
    return Pk