'''
generate variable font in RoboFont using the Batch extension

'''

import os
import variableFontGenerator

folder = os.getcwd()
desingSpacePath = os.path.join(folder, 'MutatorSans.designspace')
varFontPath = os.path.join(folder, 'MutatorSans.ttf')

p = variableFontGenerator.BatchDesignSpaceProcessor(desingSpacePath)
p.generateVariationFont(varFontPath)
