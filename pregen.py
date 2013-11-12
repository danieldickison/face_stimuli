import os
import re

def pregen(dir='.', mask='EyeMask.jpg'):
    os.chdir(dir)
    if not os.path.exists('out'):
        os.makedirs('out')
    files = [f for f in os.listdir('.') if f.endswith('.jpg') and not f.endswith('Mask.jpg') and not f.startswith('.')]
    for a in files:
        for b in files:
            if a != b:
                out = 'out/%s+%s+%s.jpg' % (a, b, mask)
                print 'compositing', out
                bash_command = "convert %s %s %s -composite %s" % (a, b, mask, out)
                os.system(bash_command)

if __name__=='__main__':
    pregen()
