#! /bin/bash
while read sub; do
	
	./qc_fetch.py $sub

	cd /home/rami/Documents/qc/$sub

	google-chrome T1_to_T2.v21.QC.gif
	freeview -v nu.mgz -v T2.FSspace.mgz:sample=cubic -v lh.seg.mgz:colormap=lut rh.seg.mgz:colormap=lut

done < subjectlist.txt

