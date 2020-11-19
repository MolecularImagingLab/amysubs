#! /bin/bash
export SUBJECTS_DIR=/group/tuominen/AMY-HCP/SUBJECTS_DIR
function process {
	recon-all -s $1 -i $2 -T2 $3 -all
	segmentHA_T2.sh $1 $3 T2 1 
}
subjects=$( cat subjectlist.txt )
np=0
for i in ${subjects[@]}; do
T1w=$( find /group/tuominen/AMY-HCP/subjects/$i/unprocessed/T1w_MPR -name "*T1w_MPR.nii.gz" )
T2w=$( find /group/tuominen/AMY-HCP/subjects/$i/unprocessed/T2w_SPC -name "*T2w_SPC.nii.gz" )
process $i $T1w $T2w &
(( np++ ))
echo $T1w
if [ $np == 40 ]; then 
	echo $np	
	echo "waiting and setting np back to 0"	
	wait
	np=0
fi 
done
