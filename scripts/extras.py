detailedListM = ['assets',
                 'autosave',
                 'cache',
                 'clips',
                 'data',
                 'Houdini',
                 'images',
                 'movies',
                 'renderData',
                 'sceneAssembly',
                 'scene',
                 'scripts',
                 'sound',
                 'sourceimages',
                 'TimeEditor']
Mprocess = str(detailedListM).replace("[", "")
Mprocess2 = str(Mprocess).replace("]", "")
Mprocess3 = str(Mprocess2).replace("'", "")
Mprocess4 = str(Mprocess3).replace(",", "")
Mprocess5 = str(Mprocess4).replace(" ", "\n")

detailedListH = ['abc',
                 'audio',
                 'comp',
                 'desk',
                 'flip',
                 'geo',
                 'hda',
                 'render',
                 'scripts',
                 'sim',
                 'tex',
                 'video']
Hprocess = str(detailedListH).replace("[", "")
Hprocess2 = str(Hprocess).replace("]", "")
Hprocess3 = str(Hprocess2).replace("'", "")
Hprocess4 = str(Hprocess3).replace(",", "")
Hprocess5 = str(Hprocess4).replace(" ", "\n")
