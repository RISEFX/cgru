#!/bin/bash

dest=$1

if [ -z "$dest" ]; then
   echo "Specify destination."
   exit 1
fi

function createDir(){
   [ -d $1 ] || mkdir -p $1
}

exclude="$exclude --exclude 'config.xml'"
exclude="$exclude --exclude 'pathmap_*.cmd'"
exclude="$exclude --exclude 'override.sh'"
exclude="$exclude --exclude '.svn'"
exclude="$exclude --exclude '*.cmd'"
exclude="$exclude --exclude '*.pyc'"
exclude="$exclude --exclude '__pycache__'"
exclude="$exclude --exclude 'doxygen/output'"

function  copy()
{
   eval "rsync -qL $exclude $1/* $2/;"
}
function rcopy()
{
   eval "rsync -rL $exclude $1 $2;"
}

createDir $dest
pushd $dest > /dev/null
dest=$PWD
cd ..
destUP=$PWD
popd > /dev/null

cd ../..
examples/clear.sh

copy . $dest

rcopy bin $dest
rcopy lib $dest
rcopy doc $dest
rcopy icons $dest
rcopy software_setup $dest
rcopy start $dest
rcopy examples $dest

copy afanasy $dest/afanasy
rcopy afanasy/bin $dest/afanasy
rcopy afanasy/lib $dest/afanasy
[ -d afanasy/bin_pyaf ] && rcopy afanasy/bin_pyaf $dest/afanasy
rcopy afanasy/doc $dest/afanasy
rcopy afanasy/icons $dest/afanasy
rcopy afanasy/init $dest/afanasy
rcopy afanasy/plugins $dest/afanasy
rcopy afanasy/python $dest/afanasy
rcopy afanasy/webvisor $dest/afanasy

copy utilities $dest/utilities
rcopy utilities/doc $dest/utilities

createDir $dest/utilities/release
rcopy utilities/release/doc $dest/utilities/release

createDir $dest/utilities/site
rcopy utilities/site/doc $dest/utilities/site

rcopy utilities/afstarter $dest/utilities
rcopy utilities/keeper $dest/utilities
rcopy utilities/moviemaker $dest/utilities
rcopy utilities/regexp $dest/utilities

createDir $dest/plugins
rcopy plugins/nuke $dest/plugins
rcopy plugins/houdini $dest/plugins
rcopy plugins/xsi $dest/plugins
rcopy plugins/blender $dest/plugins
rcopy plugins/max $dest/plugins
rcopy plugins/c4d $dest/plugins

copy plugins/maya $dest/plugins/maya
rcopy plugins/maya/doc $dest/plugins/maya
rcopy plugins/maya/icons $dest/plugins/maya
rcopy plugins/maya/mel $dest/plugins/maya
[ -d plugins/maya/mll ] && rcopy plugins/maya/mll $dest/plugins/maya

CGRU_VERSION=`cat version.txt`
cd utilities
source ./getrevision.sh ..
echo "${CGRU_VERSION} rev${CGRU_REVISION}" > $dest/version.txt