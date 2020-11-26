#! /bin/bash
# load subjects list
subjects=$( cat subjectlist.txt )
# Group subnuclei results by hemisphere (produced by freesurfer segmentation script)
sides='lh rh'
for side in ${sides[@]}; do

	asegstats2table --subjects $subjects --statsfile=amygdalar-nuclei.$side.T2.v21.T2.stats --tablefile=$side.amy_allsubjects.txt --skip

done
# Group whole amygdala result (produed by freesurfer reconall script)
asegstats2table --subjects $subjects --statsfile=aseg.stats --tablefile=whole.amy_allsubjects.txt --skip
