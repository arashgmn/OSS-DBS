# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 08:34:11 2018

@author: trieu,butenko
"""
import numpy as np

d = {
    'voxel_arr_MRI': 1,
    'voxel_arr_DTI': 0,
    'Init_neuron_model_ready': 0,
    'Init_mesh_ready': 0,
    'Adjusted_neuron_model_ready': 0,
    'CSF_mesh_ready': 0,
    'Adapted_mesh_ready': 0,
    'signal_generation_ready': 0,
    'Parallel_comp_ready': 0,
    'Parallel_comp_interrupted':0,
    'IFFT_ready': 0,
    'MRI_data_name': 'icbm_avg_152_segmented.nii.gz',
    'MRI_in_m': 0,
    'DTI_data_name': '',
    'DTI_in_m': 0,
    'CSF_index': 3.0,
    'WM_index': 2.0,
    'GM_index': 1.0,
    'default_material': 1,
    'Electrode_type': 'Medtronic3389',
    'Brain_shape_name': '0',
    'Aprox_geometry_center': [11.7631, -13.9674 , -8.8594],
    'Approximating_Dimensions': [80.0, 80.0, 80.0],
    'Implantation_coordinate_X': 11.7631, 
    'Implantation_coordinate_Y': -13.9674 , 
    'Implantation_coordinate_Z': -8.8594,
    'Second_coordinate_X': 13.7358,
    'Second_coordinate_Y': -10.0639,
    'Second_coordinate_Z': -3.7747,
    'Rotation_Z': 0.0,
    'encap_thickness': 0.1,
    'encap_tissue_type': 2,
    'encap_scaling_cond': 0.9,
    'encap_scaling_perm': 1.0,
    'pattern_model_name': '0',
    'Axon_Model_Type': 'McIntyre2002',
    'diam_fib': [5.7],
    'n_Ranvier': [3],
    'v_init': -80.0,
    'Neuron_model_array_prepared': 0,
    'Name_prepared_neuron_array': 'Allocated_axons.h5',
    'EQS_core': 'QS',
    'Skip_mesh_refinement': 1,
    'el_order': 2,
    'number_of_processors': 2,
    'FEniCS_MPI': 0,
    'current_control': 0,
    'Phi_vector': [None, 5, None, 0],
    'Solver_Type': 'GMRES',
    'freq': 130.0,
    'T': 60.0,
    't_step': 1.0,
    'phi': 0.0,
    'Signal_type': 'Rectangle',
    'Ampl_scale': 1.0,
    'CPE_activ': 0,
    'Full_Field_IFFT': 0,
    'spectrum_trunc_method': 'Octave Band Method',
    'trunc_param': 1000.0,
    'Truncate_the_obtained_full_solution': 0,
    'external_grounding': 0,
    'Stim_side': 0,
    'stretch': 1.0126193765016878,
'beta': 0.0,
    'K_A': 0.0,
    'beta_ground': 0.0,
    'K_A_ground': 0.0,
    'Global_rot': 1,
    'x_seed': 11.7631, #7.9418, # 2.5 mm away from the implantation site
    'y_seed': -13.9674,#24.0083, # 2.5 mm away from the implantation site
    'z_seed': -8.8594,#10.7399, # 2.5 mm away from the implantation site
    'x_steps': 20,
    'y_steps': 10,
    'z_steps': 20,
    'x_step': 1,
    'y_step': 1,
    'z_step': 0.5,
    'alpha_array_glob': [0, 20, 50, 0, 50, 20],
    'beta_array_glob':  [0, 0, 0, 0, 0, 20],
    'gamma_array_glob': [0, 45, 50, 50, 0, 0],
    'X_coord_old': 0,
    'Y_coord_old': 0,
    'Z_coord_old': 0,
    'YZ_angles': [0],
    'ZX_angles': [0],
    'XY_angles': [0],
    't_step_end': 1200,
    'VTA_from_divE': 0,
    'VTA_from_NEURON': 0,
    'VTA_from_E': 1,
    'Activation_threshold_VTA': 0.2,
    'refinement_frequency': [0],
    'num_ref_freqs': 1,
    'rel_div_CSF': -1,
    'Adaptive_frac_div': 1.0,
    'Min_Scaling': 1.0,
    'CSF_ref_reg': 0.0,
    'rel_div': 5.0,
    'rel_div_current': 1.0,
    'VTA_type':'grid', # cylinder or grid
    'Nx': 40,     # number of radial seeds 
    'Nz_p': 100,   # number of seeds above the implantation site
    'Nz_n':0,   # number of seeds below the implantation site
    'dx':.1,     # radial distance between seeds
    'dz':.1,     # vertical distance between seeds
    'xmin':0.2,   # minimum radial distance from the lead
    'z0': 1.5,     # seeding starting level from the tip of the lead upward in S coordinates (mm)
    'n_dirs':5,  # number of additional surfaces around the lead axis
}
