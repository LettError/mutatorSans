set -e  # make sure to abort on error
set -x  # echo commands

fontmake -m MutatorSans.designspace -o variable --verbose WARNING
fontmake -m MutatorSans-weight-only.designspace -o variable --verbose WARNING
fontmake -m MutatorSans-width-only.designspace -o variable --verbose WARNING
fontmake -m MutatorSans-with-openNodes.designspace -o variable --verbose WARNING
