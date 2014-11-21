Release notes
=============

Version 1.0RC6
--------------
unsupported interim release

+ added  HBV type lower zone to wflow\_sbm. Use MaxPercolation > 0 to use this zone. MaxLeakege > 0 will send
  water outside of the model
+ Test version of the wflow_W3RA model
+ Made two lateral flow options for sbm
+ Stopped support for pcraster version 3 and python 2.6
+ removed all the try/except from importing wflow. Now you
  NEED to install wflow as a package
+ Added seperate wflow\_routing module that includes the kinematic wave routing. This part will be removed from the
  wflow\_sbm and wflow\_hbv models
+ Added check in gash interception not to have more interception than available potential evap
+ Fixed capillary rise calculation to include timestep. This means that sub-daily models may need to be recalibrated

Version 1.0 RC5
---------------
unsupported interim release

+ netcdf reading and writing added (filename should be configured in ini file, framework section: netcdfoutput, netcdfwritebuffer, netcdfinput)
+ summary sections (summary, summary_max, symmary_avg, ect) added to ini file to save maps at end of run
+ added option to save flow per subcatchment by setting pits at the end of each subcatchment in the ldd
+ added new tbl file for wflow_sbm (et_reftopot.tbl). Used to covert reference ET to potential ET. Set to 1 by default
+ better representation of open water ET in wflow_sbm
+ wflow_adapt can now convert log files to XML for Delft-FEWS

Version 1.0 RC4
---------------

unsupported interim release

+ tss (and csv) output refactored. The ini file can now hold multiple outputtss sections each with a diffrent maps for extracting/averaging