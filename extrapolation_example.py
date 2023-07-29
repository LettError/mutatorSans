"""
    This is an example of how to extrapolate from this:
        MutatorSans-weight-only-extrapolating.designspace
    This space has 2 sources and 1 instance, way outside.

    UFOOperator is part of https://github.com/LettError/ufoProcessor
    This package is aimed at generating designspace-based 
    interpolations for complete UFOs as well as single glyphs,
    kerning, fontinfo, etc.

    UFOOperator reads the designspace, and loads the fonts.
    Then there are 2 flags: doc.useVarlib, which indicates
    which math model is to be used for the calculation:
    mutatorMath or fontTools.varlib
    And doc.extrapolate which determines the expected
    behaviour outside of the area covered by the defined sources.

    Example added to MutatorSans, July 29, 2023 erik@letterror.com
"""

import ufoProcessor.ufoOperator

path = "MutatorSans-weight-only-extrapolating.designspace"
doc = ufoProcessor.ufoOperator.UFOOperator(path)
doc.loadFonts()
doc.useVarlib = False   # set to True to use the varlib model
doc.extrapolate = True  # set to False to clip the output to the defined masters, set to True to allow extrapolation
doc.generateUFOs()