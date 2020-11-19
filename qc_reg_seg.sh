#! /bin/bash
while read sub; do
	
	./qc_fetch.py $sub

	google-chrome /home/rami/Documents/qc/$sub/T1_to_T2.v21.QC.gif

	freeview -v /home/rami/Documents/qc/$sub/nu.mgz -v /home/rami/Documents/qc/$sub/T2.FSspace.mgz:sample=cubic -v /home/rami/Documents/qc/$sub/lh.seg.mgz:colormap=lut /home/rami/Documents/qc/$sub/rh.seg.mgz:colormap=lut

done < subjectlist.txt

