import dpdata


my_system = dpdata.LabeledSystem('PAH3boundedfattyacid.out',fmt = 'siesta/aimd_output')



my_out = my_system.to('deepmd/npy', 'dpmd_npy')


