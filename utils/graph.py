import matplotlib.pyplot as plt


# Training and validation learning curve
def draw_learning_curve(history):
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    plt.figure(figsize=(10, 10))

    plt.subplot(2, 1, 1)
    plt.plot(loss, color='teal', label='loss')
    plt.plot(val_loss, color='orange', label='val_loss')
    plt.xticks(range(history.epoch[-1]+1))
    plt.legend(loc='upper left')
    plt.title('Training and Validation Loss')

    plt.subplot(2, 1, 2)
    plt.plot(acc, color='teal', label='accuracy')
    plt.plot(val_acc, color='orange', label='val_accuracy')
    plt.xticks(range(history.epoch[-1]+1))
    plt.legend(loc='upper left')
    plt.title('Training and Validation Accuracy')

    plt.show()


# Confusion matrix
def draw_confusion_matrix(cm, labels):
    class_num = len(labels)
    tick_marks = range(class_num)
    thresh = cm.min() + (cm.max()-cm.min()) / 2

    fig, ax = plt.subplots()
    im = ax.matshow(cm, cmap=plt.cm.gray_r)
    fig.colorbar(im)

    for i in range(class_num):
        for j in range(class_num):
            fg = None
            if cm[i, j] < thresh:
                fg = 'black'
            else:
                fg = 'white'
            ax.text(x=j,
                    y=i,
                    s=cm[i, j],
                    ha='center',
                    va='center',
                    ma='center',
                    color=fg,
                    size='x-large',
                    )

    ax.set_xticks(tick_marks)
    ax.set_yticks(tick_marks)

    plt.setp(ax.set_xticklabels(labels),
             ha='center',
             va='bottom',
             ma='center',
             rotation='horizontal',
             rotation_mode='default',
             )
    plt.setp(ax.set_yticklabels(labels),
             ha='right',
             va='center',
             ma='center',
             rotation='horizontal',
             rotation_mode='default',
             )
