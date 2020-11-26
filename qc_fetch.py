#!/usr/bin/env python

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
    out_name = 'T1_to_T2.v21.QC.gif'
    local_copy = tmp + out_name
    print("Retrieving:",regqc_path)
    # Execute 
    ftp_client.get(regqc_path,local_copy)
    print("Placed in:",local_copy)
    ## fetch files for segmentation QC
    files = {'nu.mgz':'/mri/nu.mgz', 'T2.FSspace.mgz':'/mri/T2.FSspace.mgz',
             'lh.seg.mgz':'/mri/lh.hippoAmygLabels-T1-T2.v21.FSvoxelSpace.mgz',
             'rh.seg.mgz':'/mri/rh.hippoAmygLabels-T1-T2.v21.FSvoxelSpace.mgz'
            'aseg.mgz':'/mri/aseg.mgz'}
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

