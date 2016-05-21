import sys as Sys
import time

def printProgress (iteration, total, decimals = 2, barLength = 100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : number of decimals in percent complete (Int) 
        barLength   - Optional  : character length of bar (Int) 
    """
    prefix = '  Progress:'
    suffix = 'Complete'
    
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '#' * filledLength + '-' * (barLength - filledLength)
    
    Sys.stdout.write('{0} [{1}] {2}{3} {4}\r'.format(prefix, bar, percents, '%', suffix)),
    Sys.stdout.flush()
    if iteration == total:
        print("\n")
        
items = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i     = 0
total     = len(items)


printProgress(i, total, barLength = 50)
for item in items:
    time.sleep(0.5)
    i += 1
    printProgress(i, total, barLength = 50)