#!/bin/bash -f

if [ "$1" == "" ]; then 
    echo "Usage:  $0 <dict_name>" 
    exit 1
fi
dict=$1

TOPDIR="$( builtin cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

dictname=$dict.dic
outdict=$TOPDIR/dist/$dictname
basedir=$TOPDIR/base

if [ ! -e $basedir/$dict'.PARTS' ]; then 
    echo "Missing configuration file $basedir/$dict.PARTS"
    exit 1
fi


rm -f $outdict
for part in `cat $basedir/$dict.PARTS`; do
    #echo "Appending $part"
    cat $TOPDIR/$part  >> $outdict
done

if [ -e $basedir/$dict'.SED' ]; then
    echo "Running sed"
    sed -f $basedir/$dict'.SED' < $outdict > $outdict.tmp
    mv $outdict.tmp $outdict
fi

echo "Completed generation of $dictname"
exit 0
