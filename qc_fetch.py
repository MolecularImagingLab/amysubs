#!/usr/bin/env python
"""This script is used to grab files from a remote computer for visually quality control. 
The .gif file is used to check the registration of the T1 scan to T2 scan, and ideally 
the borders of the images should align exactly. The .mgz files are used to visually check 
the segmentation of the amygdala and/or hippocampus. The aseg.mgz file is useful for checking 
the position of the amygdala and/or hippocampus relative to other brain areas. Finally, this 
script may be used alone (i.e. ./qc_fetch.py SUBJECT-ID) or in conjunction with qc_reg_seg.sh."""
def main():
    # Import libraries
    import paramiko
    import os
    import sys
    # Set up ssh connection
    host = 'enter i.p. address'
    user = 'enter username'
    psswrd = 'enter password'
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname = host, username = user, password = psswrd)
    ftp_client=ssh_client.open_sftp()
    print("ssh Active:",ssh_client.get_transport().is_active())
    # Fetch files for registration QC
    # Grab from:
    root = '/group/tuominen/AMY-HCP/SUBJECTS_DIR/'
    file = '/mri/transforms/T1_to_T2.v21.QC.gif'
    subject_id = sys.argv[1]
    regqc_path = root+subject_id+file
    # Place in:
    tmp = '/home/rami/Documents/qc/'
    os.mkdir(tmp+subject_id)
    tmp = tmp+subject_id+'/'
    out_name = 'T1_to_T2.v21.QC.gif' # string here will be the name of the saved .gif files
    local_copy = tmp + out_name
    print("Retrieving:",regqc_path)
    # Execute 
    ftp_client.get(regqc_path,local_copy)
    print("Placed in:",local_copy)
    # Fetch files for segmentation QC
    files = {'nu.mgz':'/mri/nu.mgz', 'T2.FSspace.mgz':'/mri/T2.FSspace.mgz',
             'lh.seg.mgz':'/mri/lh.hippoAmygLabels-T1-T2.v21.FSvoxelSpace.mgz',
             'rh.seg.mgz':'/mri/rh.hippoAmygLabels-T1-T2.v21.FSvoxelSpace.mgz',
             'aseg.mgz':'/mri/aseg.mgz'} # .keys() here will be the names of the saved .mgz files
    for file in files.keys():
        segqc_path = root+subject_id+files[file]
        out_name = file
        local_copy = tmp + out_name
        print("Retrieving:",segqc_path)
    # Execute 
        ftp_client.get(segqc_path,local_copy)
        print("Placed in:",local_copy)
if __name__ == "__main__":
    # execute only if run as a script
    main()
