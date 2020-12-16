import dpdata


my_system = dpdata.LabeledSystem('test.out',fmt = 'siesta/aimd_output')



my_out = my_system.to('deepmd/raw', 'dpmd_raw')


