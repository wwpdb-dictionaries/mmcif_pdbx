#!/bin/csh -f
#
# File:  Build.csh
# Date:  12-April-2004
#
# Usage: Build.csh <dict_name>
#
# -- 
if ( "$1" == "" ) then 
    echo "Usage:  $0 <dict_name>" 
    exit 1
endif

set d = "$1"

if ( ! -e $d'.PARTS' ) then 
    echo "Missing configuration file $d.PARTS"
    exit 1
endif 

set list = `cat $d.PARTS`
set dict = "$d.dic"

rm -f $dict

echo "###########################################################################" >> $dict
echo "#" >> $dict
echo "# File:  $dict" >> $dict
echo "# Date:  `date`" >> $dict
echo "#" >> $dict
echo "# Created from files in CVS module dict-$dict unless noted:" >> $dict
foreach f ($list)
    echo  "#        $f   " >> $dict
end
echo "#" >> $dict
echo "###########################################################################" >> $dict
echo " " >> $dict
echo " " >> $dict


foreach f ($list)
    cat $f >> $dict
end

set n = `wc -l $dict` 
echo "$dict created - text lines  =  $n"
echo ""

cp $dict ../dist
#
