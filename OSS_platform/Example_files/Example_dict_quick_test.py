# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 08:34:11 2018

@author: trieu,butenko
"""
import numpy as np

d = {
    'voxel_arr_MRI': 0,
    'voxel_arr_DTI': 0,
    'Init_neuron_model_ready': 0,
    'Init_mesh_ready': 0,
    'Adjusted_neuron_model_ready': 0,
    'CSF_mesh_ready': 0,
    'Adapted_mesh_ready': 0,
    'signal_generation_ready': 0,
    'Parallel_comp_ready': 0,
    'Parallel_comp_interrupted': 0,
    'IFFT_ready': 0,
    'MRI_data_name': 'icbm_avg_152_segmented.nii.gz',
    'MRI_in_m': 0,
    'DTI_data_name': '',
    'DTI_in_m': 0,
    'CSF_index': 1.0,
    'WM_index': 3.0,
    'GM_index': 2.0,
    'default_material': 3,
    'Electrode_type': 'Medtronic3389',
    'Brain_shape_name': '0',
    'x_length': 40.0,
    'y_length': 40.0,
    'z_length': 40.0,
    'Aprox_geometry_center': [10.92957028, -12.11697637, -7.69744601],
    'Implantation_coordinate_X': 10.929,
    'Implantation_coordinate_Y': -12.117,
    'Implantation_coordinate_Z': -7.697,
    'Second_coordinate_X': 10.929,
    'Second_coordinate_Y': -9.437,
    'Second_coordinate_Z': 3.697,
    'Rotation_Z': 0.0,
    'encap_thickness': 0.20000000000000004,
    'encap_tissue_type': 2,
    'encap_scaling_cond': 0.8,
    'encap_scaling_perm': 0.8,
    'pattern_model_name': '0',
    'diam_fib': [5.7],
    'n_Ranvier': [21],
    'v_init': -80.0,
    'Neuron_model_array_prepared': 0,
    'Name_prepared_neuron_array': '0',
    'Global_rot': 1,
    'x_seed': 10.929,
    'y_seed': -12.117,
    'z_seed': -7.697,
    'x_steps': 9,
    'y_steps': 0,
    'z_steps': 9,
    'x_step': 0.5,
    'y_step': 0.5,
    'z_step': 0.5,
    'alpha_array_glob': [0.0, 0.0, 0.0, 0.0, 45, 90, 135],
    'beta_array_glob': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    'gamma_array_glob': [0.0, 45.0, 90.0, 135.0, 0.0, 0.0, 0.0],
    'X_coord_old': 0,
    'Y_coord_old': 0,
    'Z_coord_old': 0,
    'YZ_angles': [0],
    'ZX_angles': [0],
    'XY_angles': [0],
    'EQS_core': 'QS',
    'Skip_mesh_refinement': 0,
    'refinement_frequency': [130.0],
    'num_ref_freqs': -1,
    'rel_div_CSF': 5.0,
    'CSF_frac_div': 5.0,
    'Min_Scaling': 1.0,
    'CSF_ref_reg': 10.0,
    'rel_div': 5.0,
    'Adaptive_frac_div': 5.0,
    'rel_div_current': 5.0,
    'el_order': 2,
    'number_of_processors': 4,
    'current_control': 1,
    'Phi_vector': [0.0015, None, 0.0, None],
    'freq': 130.0,
    'T': 60.0,
    't_step': 1.0,
    'phi': 0.0,
    'Signal_type': 'Rectangle',
    'Ampl_scale': 1.0,
    'CPE_activ': 0,
    'beta': 0.0,
    'K_A': 0.0,
    'beta_ground': 0.0,
    'K_A_ground': 0.0,
    'Full_Field_IFFT': 0,
    't_step_end': 1200,
    'VTA_from_divE': 0,
    'VTA_from_NEURON': 0,
    'VTA_from_E': 0,
    'Activation_threshold_VTA': 0,
    'spectrum_trunc_method': 'High Amplitude Method',
    'trunc_param': 50,
    'Truncate_the_obtained_full_solution': 0,
    'Show_paraview_screenshots': 0,

    'Solver_Type': 'GMRES',
    'FEniCS_MPI': 0,
    'Axon_Model_Type': 'McIntyre2002',
    'Approximating_Dimensions': [40.0, 40.0, 40.0],
    }
