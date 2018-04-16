#xml as input, returns an xml with gct harmonic analysis and comments (for any double gcts for the same chord)
from music21 import *
import os
import glob
import numpy as np
import operator
from copy import deepcopy
from collections import Counter
from sympy.stats import correlation
from matplotlib import pyplot as plt
from matplotlib.mlab import PCA
from matplotlib.pyplot import bar
from scipy import stats
from scipy.stats import entropy
from sklearn.manifold import TSNE
from HARM_consonanceChordRecognizer_func import HARM_consonanceChordRecognizer

fileNames = 'TestFileBachChorales'
def computeGCTsFromFile(fileName):
    #currFolder = 'TestFileBachChorales'
    consWeights = [1,0,0,1,1,1,0,1,1,1,0,0] #weights of consonant (1) and dissonant (0) intervals

    # get all the files in folder with .xml extension
    #allDocs = glob.glob(currFolder + os.sep + "*.xml")
    allDocs = glob.glob(fileName)

    # parse all pieces
    pieceIDX = 0
    # for all pieces in the set
    #for pieceName in allDocs:
    #    print("-----Parsing piece: " + pieceName + "... ")

        # parse piece
        #p = converter.parse(pieceName)
    p = converter.parse(fileName)

    # make names
#    splitName = pieceName.split(".")
#    noExtName = splitName[0]
#    finalName = noExtName + ".txt"

    # reduction
    r1 = p.parts[-1]
    r2 = p.parts[-2]
    rc = stream.Score()
    rc.insert(0, r1)
    rc.insert(0, r2)
    rcChordified = rc.chordify()
    rcFlat = rcChordified.flat
    reduction = rcFlat.getElementsByClass('Chord')
    chordsAll = []
    offsetsAll = []
    for ch in reduction:
        #ch.editorial.footnotes.append(c)
        #ch.editorial.footnotes[0]
        print("---GCT----")
        chOffset = ch.offset
        #offsetsAll.append(offsetsAll)
        chord = [c.midi for c in ch]
        #call main function that recognizes the chord
        chordForm = HARM_consonanceChordRecognizer(chord,consWeights)
        print(chordForm)
        chordsAll.append(chordForm)
        #ch.lyric = str(chordForm)
        for i in chordForm:
            ch.addLyric(str(i))
        #ch.addLyric("lala")
        #p.parts[-1].append(ch)
    #p.append(reduction)()
    #rClef = clef.bestClef(reduction)
    reduction = reduction.transpose(24)
    reduction.write("xml", "GCTs_"+fileName)
    #return reduction