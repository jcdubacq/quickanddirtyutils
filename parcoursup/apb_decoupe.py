#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Decoupe les dossiers "dématérialisés" de PostBac (APB) pour avoir
  un fichier pdf par candidat.

E. Viennet 2014-04-12
J.-C. Dubacq 2015--2018
"""

import os, sys, re, pdb

#INPUTPDF = '../dossiers_0931235M_RT.pdf'
INPUTPDF = sys.argv[1]

print 'Processing %s...' % INPUTPDF 
nb_pages = int(os.popen('pdftk %s dump_data | grep NumberOfPages' % INPUTPDF).read().split()[1])
print '%d pages' % nb_pages


pp = [] # indices de la premieres page de chaque dossier
for p in range(1,nb_pages+1):
    txt = os.popen('pdftotext -f %d -l %d %s -' % (p, p, INPUTPDF)).readlines()
    nameline = ''
    if (txt[0][:2] == 'N\xc2') and (txt[1]=='\n') and (txt[2][0] == '*') and (txt[4][0] == 'M'):
        nameline=txt[4].decode('utf8')
    elif (txt[0][:2] == 'N\xc2') and (txt[1]=='\n') and (txt[2][0] == '*') and (txt[5][0] == 'M'):
        nameline=txt[5].decode('utf8')
    if nameline != '':
        m = re.search(u'M[a-zA-Z]*\.?\s([\'A-ZÉÀÎÏÖÔÜÛÙÈÊË_\- ]*)', nameline)
        #mots=m.group(1).split()
        nom = '_'.join(m.group(1).split())
        nom = nom.replace("\'",u"\u2019").replace('_-','-').replace('-_','-')
        code = txt[0][3:].strip()
        if not nom or not code:
            print '%s page %s *** invalid data !' % (INPUTPDF, p)
        oufilename = code + '-' + nom + '.pdf'
        pp.append((p, '"'+oufilename+'"'))

print '%d candidats' % len(pp)

print 'eclatement du pdf...'
pp.append( ('end', None) )
if (not(os.path.isdir('output'))):
    os.mkdir('output')
for i in range(len(pp)-1):
    if i%100 == 0:
        print '%d/%s (%s)' % (i+1, len(pp)-1, pp[i][1])
    last_page = pp[i+1][0]
    if last_page != 'end':
        last_page -= 1
    x=os.system(('pdftk %s cat %s-%s output output/%s' % (INPUTPDF, pp[i][0],last_page, pp[i][1])).encode('utf-8'))
