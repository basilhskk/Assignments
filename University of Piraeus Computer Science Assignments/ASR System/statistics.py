from __future__ import print_function
from sklearn.metrics import confusion_matrix


def statistics(samples, predictions):
    pairs = [(samples[i], predictions[i]) for i in range(len(samples))]

    #=============================#
    # Statistics - Initialization #
    #=============================#
    statistics = {
        'digits': {},
        'samples': {},
        'total_correct_predictions': 0.0,
        'total_false_predictions': 0.0,
        'total_accuracy': None
    }

    # Fill the digits
    for i in range(0, 10):
        statistics['digits'][str(i)] = {
            'predictions': {},
            'total_predictions': 0.0,
            'accuracy': None
        }

        # Fill the prediction digits
        for j in range(0, 10): statistics['digits'][str(i)]['predictions'][str(j)] = 0.0


    # Fill the samples
    for sample in samples:
        statistics['samples'][str(sample)] = {
            'prediction': None,
            'confusion_matrix': None,
            'correct_predictions': 0.0,
            'false_predictions': 0.0,
            'accuracy': None
        }


    #==========================#
    # Statistics - Calculation #
    #==========================#
    for sample, prediction in pairs:
        statistics['samples'][str(sample)]['prediction'] = str(prediction)

        # Calculate statistics per digit
        for i in range(len(sample)):
            statistics['digits'][str(sample[i])]['predictions'][str(prediction[i])] += 1
            statistics['digits'][str(sample[i])]['total_predictions'] += 1

            # Correct prediction
            if sample[i] == prediction[i]:
                statistics['samples'][str(sample)]['correct_predictions'] += 1
                statistics['total_correct_predictions'] += 1

            # False prediction
            else:
                statistics['samples'][str(sample)]['false_predictions'] += 1
                statistics['total_false_predictions'] += 1
        
        # Calculate sample confusion matrix
        statistics['samples'][str(sample)]['confusion_matrix'] = confusion_matrix(sample, prediction)

        # Calculate sample accuracy
        if statistics['samples'][str(sample)]['false_predictions'] == 0:
            statistics['samples'][str(sample)]['accuracy'] = 1.0
        else:
            statistics['samples'][str(sample)]['accuracy'] = statistics['samples'][str(sample)]['correct_predictions'] / (statistics['samples'][str(sample)]['correct_predictions'] + statistics['samples'][str(sample)]['false_predictions'])

    # Calculate per digit accuracy
    for i in range(0, 10):
        statistics['digits'][str(i)]['accuracy'] = statistics['digits'][str(i)]['predictions'][str(i)] / statistics['digits'][str(i)]['total_predictions']

    # Calculate total sample accuracy
    statistics['total_accuracy'] = statistics['total_correct_predictions'] / (statistics['total_correct_predictions'] + statistics['total_false_predictions'])

    return statistics


def printDigitConfusionMatrix(stats):
    max_width = 0
    counters = []

    # Get the digit counters
    for i in range(0, 10):
        counters.append([])
        for j in range(0, 10):
            counter = str(int(stats['digits'][str(i)]['predictions'][str(j)]))
            counters[-1].append(counter)

            if len(counter) > max_width: max_width = len(counter)

    width = max_width + 1
    print('    +{}+'.format('-' * ((width) * 10 + 1 + len(' SUCCESS | FAIL    |'))))

    print('    |', end='')
    for i in range(0, 10): print('{}{}'.format(' ' * (width - 1), i), end='')
    print(' | SUCCESS | FAIL    |')

    print('+---+{}+'.format('-' * ((width) * 10 + 1 + len(' SUCCESS | FAIL    |'))))

    for i in range(0, 10):
        print('| {} |'.format(i), end='')

        for counter in counters[i]:
            space = max_width + 1 - len(str(counter))
            print('{}{}'.format(' ' * space, counter), end='')

        accuracy_percent = round(stats['digits'][str(i)]['accuracy'] * 100, 1)
        loss_percent = round(100.0 - accuracy_percent, 1)
        print(' | {:5.1f} % | {:5.1f} % |'.format(accuracy_percent, loss_percent))

    print('+---+{}+'.format('-' * ((width) * 10 + 1 + len(' SUCCESS | FAIL    |'))))

    total_accuracy_percent = round(stats['total_accuracy'] * 100, 1)
    total_loss_percent = round(100.0 - total_accuracy_percent, 1)
    print('     {} | {:5.1f} % | {:5.1f} % |'.format(' ' * ((width) * 10), total_accuracy_percent, total_loss_percent))
    print('     {} +-------------------+'.format(' ' * ((width) * 10)))
