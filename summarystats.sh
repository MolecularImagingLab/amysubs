#! /bin/bash

subjects=$( cat subjectlist.txt )
sides='lh rh'
for side in ${sides[@]}; do

	asegstats2table --subjects $subjects --statsfile=amygdalar-nuclei.$side.T2.v21.T2.stats --tablefile=$side.amy_allsubjects.txt --skip

done
