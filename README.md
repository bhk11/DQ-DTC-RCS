# Deep Q Direct Torque Control with a Reduced Control Set (DQ-DTC-RCS) - Code Examples

[Read the Paper](https://ieeexplore.ieee.org/document/9416143)

The jupyter notebooks in this folder were created to present the training and usage of a DQ-DTC-RCS reinforcement learning drive control system. A deep Q direct torque controller can be trained via the DQ_DTC_training.ipynb notebook. The trained controller can then be tested with the DQ_DTC_validation_profile.ipynb notebook.

The needed python packages are listed in the requirements.txt and can e.g. be installed via
```
	pip install -r requirements.txt
```
	

The python code files CustomKerasRL2Callbacks_torqueCtrl.py, mapping.py and Plot_TimeDomain_torqueCtrl.py implement extensions to the code
that were outsourced from the notebooks, they do not need to be executed manually. 

# Citation

Please use the following BibTeX entry to cite this code:

```
@INPROCEEDINGS{DQ-DTC-RCS,
  author={Haucke-Korber, Barnabas and Schenke, Maximilian and Wallscheid, Oliver},  
  booktitle={2023 IEEE International Electric Machines & Drives Conference (IEMDC)}, 
  title={Deep Q Direct Torque Control with a Reduced Control Set Towards Six-Step Operation of Permanent Magnet Synchronous Motors}, 
  year={2023},
  volume={},
  number={},
  pages={1-7}}
```
