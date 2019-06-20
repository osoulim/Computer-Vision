% Intrinsic and Extrinsic Camera Parameters
%
% This script file can be directly executed under Matlab to recover the camera intrinsic and extrinsic parameters.
% IMPORTANT: This file contains neither the structure of the calibration objects nor the image coordinates of the calibration points.
%            All those complementary variables are saved in the complete matlab data file Calib_Results.mat.
% For more information regarding the calibration model visit http://www.vision.caltech.edu/bouguetj/calib_doc/


%-- Focal length:
fc = [ 1141.850086752728203 ; 1140.135827197829940 ];

%-- Principal point:
cc = [ 648.189239928494089 ; 373.668939760862600 ];

%-- Skew coefficient:
alpha_c = 0.000000000000000;

%-- Distortion coefficients:
kc = [ 0.117026151275975 ; -0.607880360275291 ; 0.002068454947039 ; 0.001471818267151 ; 0.000000000000000 ];

%-- Focal length uncertainty:
fc_error = [ 6.960423426673430 ; 6.647872850669967 ];

%-- Principal point uncertainty:
cc_error = [ 7.202706655720584 ; 5.639022457404376 ];

%-- Skew coefficient uncertainty:
alpha_c_error = 0.000000000000000;

%-- Distortion coefficients uncertainty:
kc_error = [ 0.021459094442918 ; 0.100989192008552 ; 0.001682634867988 ; 0.002926411786715 ; 0.000000000000000 ];

%-- Image size:
nx = 1280;
ny = 720;


%-- Various other variables (may be ignored if you do not use the Matlab Calibration Toolbox):
%-- Those variables are used to control which intrinsic parameters should be optimized

n_ima = 12;						% Number of calibration images
est_fc = [ 1 ; 1 ];					% Estimation indicator of the two focal variables
est_aspect_ratio = 1;				% Estimation indicator of the aspect ratio fc(2)/fc(1)
center_optim = 1;					% Estimation indicator of the principal point
est_alpha = 0;						% Estimation indicator of the skew coefficient
est_dist = [ 1 ; 1 ; 1 ; 1 ; 0 ];	% Estimation indicator of the distortion coefficients


%-- Extrinsic parameters:
%-- The rotation (omc_kk) and the translation (Tc_kk) vectors for every calibration image and their uncertainties

%-- Image #1:
omc_1 = [ 2.018283e+00 ; 1.944527e+00 ; 1.531629e-01 ];
Tc_1  = [ -9.564866e+01 ; -8.388644e+01 ; 4.436716e+02 ];
omc_error_1 = [ 5.212786e-03 ; 5.317989e-03 ; 9.924894e-03 ];
Tc_error_1  = [ 2.801828e+00 ; 2.194499e+00 ; 2.855485e+00 ];

%-- Image #2:
omc_2 = [ 2.131525e+00 ; 2.116266e+00 ; -1.440263e-01 ];
Tc_2  = [ -1.776236e+02 ; -8.205219e+01 ; 4.568552e+02 ];
omc_error_2 = [ 4.694959e-03 ; 6.176171e-03 ; 1.132269e-02 ];
Tc_error_2  = [ 2.898871e+00 ; 2.314103e+00 ; 2.969584e+00 ];

%-- Image #3:
omc_3 = [ -2.102770e+00 ; -2.149939e+00 ; 4.878091e-01 ];
Tc_3  = [ -1.855826e+02 ; -8.183808e+01 ; 4.771684e+02 ];
omc_error_3 = [ 5.891507e-03 ; 4.191302e-03 ; 9.757117e-03 ];
Tc_error_3  = [ 3.030828e+00 ; 2.435835e+00 ; 2.903764e+00 ];

%-- Image #4:
omc_4 = [ 1.914224e+00 ; 1.898707e+00 ; 2.675655e-01 ];
Tc_4  = [ -9.269714e+01 ; -8.393818e+01 ; 3.782293e+02 ];
omc_error_4 = [ 5.150522e-03 ; 5.042694e-03 ; 8.344369e-03 ];
Tc_error_4  = [ 2.391116e+00 ; 1.874923e+00 ; 2.456119e+00 ];

%-- Image #5:
omc_5 = [ 1.782039e+00 ; 1.705928e+00 ; 4.754145e-01 ];
Tc_5  = [ -7.469550e+01 ; -7.531603e+01 ; 4.346770e+02 ];
omc_error_5 = [ 5.554179e-03 ; 4.876609e-03 ; 7.330390e-03 ];
Tc_error_5  = [ 2.736750e+00 ; 2.146903e+00 ; 2.895238e+00 ];

%-- Image #6:
omc_6 = [ 1.766780e+00 ; 1.765593e+00 ; 1.534559e-01 ];
Tc_6  = [ -1.239582e+02 ; -4.576631e+01 ; 6.483347e+02 ];
omc_error_6 = [ 5.174332e-03 ; 5.573094e-03 ; 8.819109e-03 ];
Tc_error_6  = [ 4.074034e+00 ; 3.221086e+00 ; 4.201068e+00 ];

%-- Image #7:
omc_7 = [ 1.876336e+00 ; 1.672651e+00 ; -5.170863e-01 ];
Tc_7  = [ -1.580216e+02 ; -8.149915e+01 ; 4.387236e+02 ];
omc_error_7 = [ 3.439446e-03 ; 5.478390e-03 ; 7.792767e-03 ];
Tc_error_7  = [ 2.786803e+00 ; 2.211004e+00 ; 2.679286e+00 ];

%-- Image #8:
omc_8 = [ 1.843557e+00 ; 1.970723e+00 ; -1.014171e+00 ];
Tc_8  = [ -1.477039e+02 ; -8.161124e+01 ; 5.186839e+02 ];
omc_error_8 = [ 2.823302e-03 ; 6.031831e-03 ; 8.487582e-03 ];
Tc_error_8  = [ 3.293035e+00 ; 2.607500e+00 ; 2.842960e+00 ];

%-- Image #9:
omc_9 = [ 1.870680e+00 ; 1.509334e+00 ; -3.265335e-01 ];
Tc_9  = [ -1.468471e+02 ; -7.599675e+01 ; 4.958010e+02 ];
omc_error_9 = [ 4.056123e-03 ; 5.290516e-03 ; 7.571010e-03 ];
Tc_error_9  = [ 3.138931e+00 ; 2.467289e+00 ; 3.086078e+00 ];

%-- Image #10:
omc_10 = [ 1.882057e+00 ; 1.776970e+00 ; -6.700239e-01 ];
Tc_10  = [ -1.515325e+02 ; -8.449066e+01 ; 4.432286e+02 ];
omc_error_10 = [ 3.158258e-03 ; 5.615791e-03 ; 8.094132e-03 ];
Tc_error_10  = [ 2.820113e+00 ; 2.235041e+00 ; 2.603415e+00 ];

%-- Image #11:
omc_11 = [ -2.064941e+00 ; -2.051249e+00 ; 2.099481e-01 ];
Tc_11  = [ -1.651204e+02 ; -7.322129e+01 ; 4.017831e+02 ];
omc_error_11 = [ 5.049936e-03 ; 4.374982e-03 ; 9.424089e-03 ];
Tc_error_11  = [ 2.541551e+00 ; 2.038180e+00 ; 2.543735e+00 ];

%-- Image #12:
omc_12 = [ 2.017122e+00 ; 2.061487e+00 ; 4.292196e-01 ];
Tc_12  = [ -1.391564e+02 ; -7.570827e+01 ; 3.733256e+02 ];
omc_error_12 = [ 5.569123e-03 ; 5.112563e-03 ; 8.812025e-03 ];
Tc_error_12  = [ 2.401815e+00 ; 1.907351e+00 ; 2.487006e+00 ];

