import os

from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor, RuleDescriptor

root = os.getcwd()
doc = DesignSpaceDocument()

familyName = "MutatorSansTest"

#------
# axes
#------

a1 = AxisDescriptor()
a1.maximum = 1000
a1.minimum = 0
a1.default = 0
a1.name = "width"
a1.tag = "wdth"
doc.addAxis(a1)

a2 = AxisDescriptor()
a2.maximum = 1000
a2.minimum = 0
a2.default = 0
a2.name = "weight"
a2.tag = "wght"
doc.addAxis(a2)

#---------
# masters
#---------

s0 = SourceDescriptor()
s0.path = "MutatorSansLightCondensed.ufo"
s0.name = "master.MutatorSansTest.LightCondensed.0"
s0.familyName = familyName
s0.styleName = "LightCondensed"
s0.location = dict(weight=0, width=0)
s0.copyLib = True
s0.copyInfo = True
s0.copyGroups = True
s0.copyFeatures = True
doc.addSource(s0)

s1 = SourceDescriptor()
s1.path = "MutatorSansBoldCondensed.ufo"
s1.name = "master.MutatorSansTest.BoldCondensed.1"
s1.familyName = familyName
s1.styleName = "BoldCondensed"
s1.location = dict(weight=1000, width=0)
doc.addSource(s1)

s2 = SourceDescriptor()
s2.path = "MutatorSansLightWide.ufo"
s2.name = "master.MutatorSansTest.LightWide.2"
s2.familyName = familyName
s2.styleName = "LightWide"
s2.location = dict(weight=0, width=1000)
doc.addSource(s2)

s3 = SourceDescriptor()
s3.path = "MutatorSansBoldWide.ufo"
s3.name = "master.MutatorSansTest.BoldWide.3"
s3.familyName = familyName
s3.styleName = "BoldWide"
s3.location = dict(weight=1000, width=1000)
doc.addSource(s3)

#-----------
# instances
#-----------

i0 = InstanceDescriptor()
i0.name = 'instance_LightCondensed'
i0.familyName = familyName
i0.styleName = "Medium"
i0.path = os.path.join(root, "instances", "MutatorSansTest-Medium.ufo")
i0.location = dict(weight=500, width=327)
i0.kerning = True
i0.info = True
doc.addInstance(i0)

#-------
# rules
#-------

rd = RuleDescriptor()
rd.name = 'fold_I_serifs'
rd.conditionSets = [[{'minimum': 0.0, 'maximum': 328.0, 'name': 'width'}]]
rd.subs = [('I', 'I.narrow')]
doc.addRule(rd)

rd = RuleDescriptor()
rd.name = 'fold_S_terminals'
rd.conditionSets = [[{'minimum': 0.0, 'maximum': 1000.0, 'name': 'width'}, {'minimum': 0.0, 'maximum': 500.0, 'name': 'weight'}]]
rd.subs = [('S', 'S.closed')]
doc.addRule(rd)

#--------
# saving
#--------

path = os.path.join(root, "MutatorSans__Test__.designspace")
doc.write(path)
