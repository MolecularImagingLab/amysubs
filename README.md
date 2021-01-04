# Amygdala segmentation pipeline for the [HCP Early Psychosis 1.0 Release Dataset](https://www.humanconnectome.org/study/human-connectome-project-for-early-psychosis/document/hcp-early-psychosis-release-reference-manual-and-access-instructions)
# Using [FreeSurfer 7.0 Segmentation Algorithm:](https://surfer.nmr.mgh.harvard.edu/fswiki/HippocampalSubfieldsAndNucleiOfAmygdala)
## General Steps
### 1. Clone repository
### 2. Run FreeSurfer scripts - After downloading the data, open terminal and execute: ./reg_seg.sh
### 3. Conduct quality control - Ensuring qc_fetch.py is in the same folder, execute: .\qc_reg_seg.sh. In this step it is best practice to document the results of the visual quality check.
### 4. Get amygdala volumes - execute: ./summarystats.sh, generating a text file contaning all amygdala volumes for all subjects by hemisphere
### 5. Check size order of sublnuclei volumes - execute: ./subsize_checker.py, this also checks for outliers using standard boxplot interquartile range
### 6. Generate table for stats including demographic information - execute: ./clean_data.py
### 7. Conduct stats on data using linear mixed effects model - In R, execute: lme_amygdala.R
