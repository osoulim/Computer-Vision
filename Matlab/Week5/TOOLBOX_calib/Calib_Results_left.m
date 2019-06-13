% Intrinsic and Extrinsic Camera Parameters
%
% This script file can be directly executed under Matlab to recover the camera intrinsic and extrinsic parameters.
% IMPORTANT: This file contains neither the structure of the calibration objects nor the image coordinates of the calibration points.
%            All those complementary variables are saved in the complete matlab data file Calib_Results.mat.
% For more information regarding the calibration model visit http://www.vision.caltech.edu/bouguetj/calib_doc/


%-- Focal length:
fc = [ 1128.079806197936705 ; 1122.968194027448817 ];

%-- Principal point:
cc = [ 652.647910030126354 ; 363.521361524456836 ];

%-- Skew coefficient:
alpha_c = 0.000000000000000;

%-- Distortion coefficients:
kc = [ 0.141754275862650 ; -0.939808519687525 ; 0.003528320469899 ; 0.003848216517568 ; 0.000000000000000 ];

%-- Focal length uncertainty:
fc_error = [ 12.873250616662590 ; 11.957147032309047 ];

%-- Principal point uncertainty:
cc_error = [ 7.791968028708610 ; 8.709046006053596 ];

%-- Skew coefficient uncertainty:
alpha_c_error = 0.000000000000000;

%-- Distortion coefficients uncertainty:
kc_error = [ 0.033495043745552 ; 0.205916936221438 ; 0.002730148944721 ; 0.002137953441006 ; 0.000000000000000 ];

%-- Image size:
nx = 1280;
ny = 720;


%-- Various other variables (may be ignored if you do not use the Matlab Calibration Toolbox):
%-- Those variables are used to control which intrinsic parameters should be optimized

n_ima = 10;						% Number of calibration images
est_fc = [ 1 ; 1 ];					% Estimation indicator of the two focal variables
est_aspect_ratio = 1;				% Estimation indicator of the aspect ratio fc(2)/fc(1)
center_optim = 1;					% Estimation indicator of the principal point
est_alpha = 0;						% Estimation indicator of the skew coefficient
est_dist = [ 1 ; 1 ; 1 ; 1 ; 0 ];	% Estimation indicator of the distortion coefficients


%-- Extrinsic parameters:
%-- The rotation (omc_kk) and the translation (Tc_kk) vectors for every calibration image and their uncertainties

%-- Image #1:
omc_1 = [ 2.233080e+00 ; 2.007557e+00 ; 5.448121e-01 ];
Tc_1  = [ -1.194333e+02 ; -9.397318e+01 ; 5.260655e+02 ];
omc_error_1 = [ 7.074717e-03 ; 5.637597e-03 ; 1.342385e-02 ];
Tc_error_1  = [ 3.693555e+00 ; 4.142529e+00 ; 6.142967e+00 ];

%-- Image #2:
omc_2 = [ 2.179137e+00 ; 1.936922e+00 ; 6.212672e-01 ];
Tc_2  = [ -1.734863e+02 ; -8.765739e+01 ; 5.123582e+02 ];
omc_error_2 = [ 7.041696e-03 ; 5.728499e-03 ; 1.325049e-02 ];
Tc_error_2  = [ 3.615205e+00 ; 4.109635e+00 ; 6.201097e+00 ];

%-- Image #3:
omc_3 = [ -2.000621e+00 ; -1.928188e+00 ; 1.234503e-01 ];
Tc_3  = [ -1.306510e+02 ; -8.267009e+01 ; 4.755411e+02 ];
omc_error_3 = [ 6.523013e-03 ; 5.182910e-03 ; 1.054161e-02 ];
Tc_error_3  = [ 3.249458e+00 ; 3.730133e+00 ; 5.250263e+00 ];

%-- Image #4:
omc_4 = [ -1.903801e+00 ; -1.899697e+00 ; 5.796415e-01 ];
Tc_4  = [ -2.490666e+00 ; -8.601365e+01 ; 6.281725e+02 ];
omc_error_4 = [ 6.818637e-03 ; 5.577146e-03 ; 1.185341e-02 ];
Tc_error_4  = [ 4.364050e+00 ; 4.826769e+00 ; 6.248213e+00 ];

%-- Image #5:
omc_5 = [ -1.848252e+00 ; -1.640790e+00 ; 6.619583e-01 ];
Tc_5  = [ -1.503883e+01 ; -5.942785e+01 ; 6.545083e+02 ];
omc_error_5 = [ 6.883721e-03 ; 5.003557e-03 ; 1.038423e-02 ];
Tc_error_5  = [ 4.535464e+00 ; 5.044202e+00 ; 6.148776e+00 ];

%-- Image #6:
omc_6 = [ 2.285029e+00 ; 1.816578e+00 ; 6.127952e-01 ];
Tc_6  = [ -1.496450e+02 ; -7.227358e+01 ; 4.882458e+02 ];
omc_error_6 = [ 7.075515e-03 ; 4.912864e-03 ; 1.278152e-02 ];
Tc_error_6  = [ 3.433958e+00 ; 3.874383e+00 ; 5.807723e+00 ];

%-- Image #7:
omc_7 = [ 2.250481e+00 ; 1.776950e+00 ; 6.667538e-01 ];
Tc_7  = [ -1.614142e+02 ; -7.127490e+01 ; 4.797158e+02 ];
omc_error_7 = [ 7.025566e-03 ; 4.789564e-03 ; 1.236730e-02 ];
Tc_error_7  = [ 3.380680e+00 ; 3.828455e+00 ; 5.805789e+00 ];

%-- Image #8:
omc_8 = [ 2.086707e+00 ; 2.036174e+00 ; 4.757507e-01 ];
Tc_8  = [ -1.512238e+02 ; -1.130655e+02 ; 4.902880e+02 ];
omc_error_8 = [ 6.345070e-03 ; 6.302285e-03 ; 1.341574e-02 ];
Tc_error_8  = [ 3.465799e+00 ; 3.907532e+00 ; 5.782021e+00 ];

%-- Image #9:
omc_9 = [ -2.027011e+00 ; -2.126772e+00 ; 1.271261e-02 ];
Tc_9  = [ -1.767841e+02 ; -1.344546e+02 ; 6.049640e+02 ];
omc_error_9 = [ 7.897123e-03 ; 6.647734e-03 ; 1.493714e-02 ];
Tc_error_9  = [ 4.205034e+00 ; 4.791928e+00 ; 7.105781e+00 ];

%-- Image #10:
omc_10 = [ -2.160760e+00 ; -2.204361e+00 ; -1.889340e-01 ];
Tc_10  = [ -1.100478e+02 ; -9.454009e+01 ; 3.867874e+02 ];
omc_error_10 = [ 5.600426e-03 ; 5.913715e-03 ; 1.110075e-02 ];
Tc_error_10  = [ 2.715241e+00 ; 3.077851e+00 ; 4.649516e+00 ];

