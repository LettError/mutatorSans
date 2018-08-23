import math
d = listFontVariations("MutatorMathTest")
print(list(d.keys()))

for fontName in installedFonts():
    variations = listFontVariations(fontName)
    if variations: 
        print(fontName)
        for axis_name, dimensions in variations.items():
            print (axis_name, dimensions)
        print ()


weightMin = listFontVariations('MutatorMathTest')['wght']['minValue']
weightMax = listFontVariations('MutatorMathTest')['wght']['maxValue']

widthMin = listFontVariations('MutatorMathTest')['wdth']['minValue']
widthMax = listFontVariations('MutatorMathTest')['wdth']['maxValue']


steps = 50
txt = 'FISH'

def ip(a, b, f):
    return a + f*(b-a)
    
for i in range(steps):
    angle = 2 * pi * (i / steps)
    a1 = .5+cos(angle)*.5
    a2 = .5+sin(angle)*.5
    newPage(1100, 300)
    font("MutatorMathTest")
    fontSize(120)
    weightValue = ip(weightMin, weightMax, a1)
    widthValue = ip(widthMin, widthMax, a2)
    fontVariations(wght=weightValue, wdth=widthValue)
    
    
    text(txt, (70, 70))

    font("Menlo-Regular")
    fontSize(10)

    text('MutatorSans weight: %3.3f, width: %3.3f' % (weightValue, widthValue), (10, 10))

saveImage('mutatorSasns.gif')