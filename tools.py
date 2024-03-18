import sys, traceback

def safe(func,*args):
    try:
        func(*args)
    except:
        print('Catched: ',sys.exc_info()[0:2])
        traceback.print_exc()