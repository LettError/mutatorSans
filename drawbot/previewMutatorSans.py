import os

folder = os.path.dirname(os.getcwd())
fontPath = os.path.join(folder, 'MutatorSans.ttf')

variations = listFontVariations(fontPath)

wghtMin = variations['wght']['minValue']
wghtMax = variations['wght']['maxValue']
wdthMin = variations['wdth']['minValue']
wdthMax = variations['wdth']['maxValue']

txt = "Amazingly few discotheques provide jukeboxes."

Variable([
    dict(name="wght", ui="Slider", args=dict(value=400, minValue=wghtMin, maxValue=wghtMax)),
    dict(name="wdth", ui="Slider", args=dict(value=400, minValue=wdthMin, maxValue=wdthMax)),
    dict(name="txt", ui="EditText", args=dict(text=txt)),
    dict(name="pt", ui="Slider", args=dict(value=64, minValue=12, maxValue=640)),
], globals())

newPage(800, 600)

margin = 20
x = y = margin
w = width() - margin*2
h = height() - margin*2

font(fontPath)
fontSize(pt)
fontVariations(wght=wght, wdth=wdth)
textBox(txt.upper(), (x, y, w, h), align='center')

font("Menlo-Regular")
fontVariations(resetVariations=True)
fontSize(9)
textBox('MutatorSans weight=%3.3f width=%3.3f / %3.3fpt' % (wght, wdth, pt), (20, 10, w, 12), align='center')
