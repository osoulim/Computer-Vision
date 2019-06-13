% Intrinsic and Extrinsic Camera Parameters
%
% This script file can be directly executed under Matlab to recover the camera intrinsic and extrinsic parameters.
% IMPORTANT: This file contains neither the structure of the calibration objects nor the image coordinates of the calibration points.
%            All those complementary variables are saved in the complete matlab data file Calib_Results.mat.
% For more information regarding the calibration model visit http://www.vision.caltech.edu/bouguetj/calib_doc/


%-- Focal length:
fc = [ 1129.849819404540767 ; 1124.774902795486923 ];

%-- Principal point:
cc = [ 639.553279376802152 ; 376.105541174868449 ];

%-- Skew coefficient:
alpha_c = 0.000000000000000;

%-- Distortion coefficients:
kc = [ 0.049883762291914 ; -0.341400697073864 ; 0.003739200469173 ; -0.000347999717983 ; 0.000000000000000 ];

%-- Focal length uncertainty:
fc_error = [ 7.479315956897595 ; 6.765079539948021 ];

%-- Principal point uncertainty:
cc_error = [ 6.273649281193644 ; 4.716043548044380 ];

%-- Skew coefficient uncertainty:
alpha_c_error = 0.000000000000000;

%-- Distortion coefficients uncertainty:
kc_error = [ 0.013721186312428 ; 0.045897683385519 ; 0.001189844087905 ; 0.002103571836708 ; 0.000000000000000 ];

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
omc_1 = [ 2.194219e+00 ; 2.014117e+00 ; 5.669569e-01 ];
Tc_1  = [ -1.746006e+02 ; -9.459499e+01 ; 5.184193e+02 ];
omc_error_1 = [ 4.847747e-03 ; 4.299338e-03 ; 8.943552e-03 ];
Tc_error_1  = [ 2.929174e+00 ; 2.237389e+00 ; 3.537428e+00 ];

%-- Image #2:
omc_2 = [ 2.144342e+00 ; 1.944273e+00 ; 6.443161e-01 ];
Tc_2  = [ -2.286213e+02 ; -8.909935e+01 ; 5.030301e+02 ];
omc_error_2 = [ 4.545858e-03 ; 4.058718e-03 ; 8.671940e-03 ];
Tc_error_2  = [ 2.895069e+00 ; 2.225295e+00 ; 3.575682e+00 ];

%-- Image #3:
omc_3 = [ -1.997880e+00 ; -1.962803e+00 ; 1.061036e-01 ];
Tc_3  = [ -1.851997e+02 ; -8.356500e+01 ; 4.686443e+02 ];
omc_error_3 = [ 3.802705e-03 ; 3.456928e-03 ; 7.259103e-03 ];
Tc_error_3  = [ 2.586033e+00 ; 2.022048e+00 ; 3.090994e+00 ];

%-- Image #4:
omc_4 = [ -1.909247e+00 ; -1.933556e+00 ; 5.619690e-01 ];
Tc_4  = [ -6.096630e+01 ; -8.406240e+01 ; 6.245829e+02 ];
omc_error_4 = [ 4.048549e-03 ; 3.394408e-03 ; 7.193617e-03 ];
Tc_error_4  = [ 3.452333e+00 ; 2.604417e+00 ; 3.553074e+00 ];

%-- Image #5:
omc_5 = [ -1.855814e+00 ; -1.674206e+00 ; 6.496287e-01 ];
Tc_5  = [ -7.472180e+01 ; -5.754602e+01 ; 6.507927e+02 ];
omc_error_5 = [ 4.154787e-03 ; 3.529305e-03 ; 6.477384e-03 ];
Tc_error_5  = [ 3.581806e+00 ; 2.724197e+00 ; 3.497907e+00 ];

%-- Image #6:
omc_6 = [ 2.248705e+00 ; 1.826075e+00 ; 6.393032e-01 ];
Tc_6  = [ -2.043890e+02 ; -7.353952e+01 ; 4.799228e+02 ];
omc_error_6 = [ 4.668926e-03 ; 3.662720e-03 ; 8.556112e-03 ];
Tc_error_6  = [ 2.729685e+00 ; 2.098314e+00 ; 3.360489e+00 ];

%-- Image #7:
omc_7 = [ 2.214119e+00 ; 1.785246e+00 ; 6.927795e-01 ];
Tc_7  = [ -2.159438e+02 ; -7.280095e+01 ; 4.711887e+02 ];
omc_error_7 = [ 4.553332e-03 ; 3.519696e-03 ; 8.201865e-03 ];
Tc_error_7  = [ 2.698138e+00 ; 2.075792e+00 ; 3.356327e+00 ];

%-- Image #8:
omc_8 = [ 2.052181e+00 ; 2.043099e+00 ; 4.995833e-01 ];
Tc_8  = [ -2.054335e+02 ; -1.143181e+02 ; 4.825439e+02 ];
omc_error_8 = [ 4.152002e-03 ; 4.625251e-03 ; 8.664590e-03 ];
Tc_error_8  = [ 2.777713e+00 ; 2.120345e+00 ; 3.362096e+00 ];

%-- Image #9:
omc_9 = [ -2.021359e+00 ; -2.162549e+00 ; 4.090463e-03 ];
Tc_9  = [ -2.333917e+02 ; -1.357763e+02 ; 5.965515e+02 ];
omc_error_9 = [ 4.319334e-03 ; 3.750239e-03 ; 9.113327e-03 ];
Tc_error_9  = [ 3.335126e+00 ; 2.586464e+00 ; 4.125670e+00 ];

%-- Image #10:
omc_10 = [ -2.154493e+00 ; -2.241479e+00 ; -2.120036e-01 ];
Tc_10  = [ -1.620098e+02 ; -9.553074e+01 ; 3.807550e+02 ];
omc_error_10 = [ 3.478484e-03 ; 3.417531e-03 ; 7.578680e-03 ];
Tc_error_10  = [ 2.157205e+00 ; 1.667632e+00 ; 2.773924e+00 ];

