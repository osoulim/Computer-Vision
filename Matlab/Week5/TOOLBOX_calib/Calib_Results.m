% Intrinsic and Extrinsic Camera Parameters
%
% This script file can be directly executed under Matlab to recover the camera intrinsic and extrinsic parameters.
% IMPORTANT: This file contains neither the structure of the calibration objects nor the image coordinates of the calibration points.
%            All those complementary variables are saved in the complete matlab data file Calib_Results.mat.
% For more information regarding the calibration model visit http://www.vision.caltech.edu/bouguetj/calib_doc/


%-- Focal length:
fc = [ 1204.519106593358174 ; 1199.377888516199164 ];

%-- Principal point:
cc = [ 497.747058105464248 ; 604.842741951255107 ];

%-- Skew coefficient:
alpha_c = 0.000000000000000;

%-- Distortion coefficients:
kc = [ 0.158863642517012 ; -0.878477226749010 ; -0.004362641012330 ; 0.002153021800054 ; 0.000000000000000 ];

%-- Focal length uncertainty:
fc_error = [ 49.150351105198958 ; 48.292854027570911 ];

%-- Principal point uncertainty:
cc_error = [ 6.185701667315620 ; 14.606938415880688 ];

%-- Skew coefficient uncertainty:
alpha_c_error = 0.000000000000000;

%-- Distortion coefficients uncertainty:
kc_error = [ 0.033049322681790 ; 0.320028964996359 ; 0.001723873675878 ; 0.001845518720682 ; 0.000000000000000 ];

%-- Image size:
nx = 960;
ny = 1280;


%-- Various other variables (may be ignored if you do not use the Matlab Calibration Toolbox):
%-- Those variables are used to control which intrinsic parameters should be optimized

n_ima = 7;						% Number of calibration images
est_fc = [ 1 ; 1 ];					% Estimation indicator of the two focal variables
est_aspect_ratio = 1;				% Estimation indicator of the aspect ratio fc(2)/fc(1)
center_optim = 1;					% Estimation indicator of the principal point
est_alpha = 0;						% Estimation indicator of the skew coefficient
est_dist = [ 1 ; 1 ; 1 ; 1 ; 0 ];	% Estimation indicator of the distortion coefficients


%-- Extrinsic parameters:
%-- The rotation (omc_kk) and the translation (Tc_kk) vectors for every calibration image and their uncertainties

%-- Image #1:
omc_1 = [ 2.915358e+00 ; 7.484980e-01 ; -1.273985e-01 ];
Tc_1  = [ -1.101716e+02 ; 4.311119e+01 ; 4.432397e+02 ];
omc_error_1 = [ 6.666930e-03 ; 2.454341e-03 ; 8.907810e-03 ];
Tc_error_1  = [ 2.274396e+00 ; 5.428663e+00 ; 1.805313e+01 ];

%-- Image #2:
omc_2 = [ 2.374992e+00 ; 1.862590e+00 ; 2.576998e-02 ];
Tc_2  = [ -1.167234e+02 ; -4.723738e+01 ; 4.268233e+02 ];
omc_error_2 = [ 5.922182e-03 ; 4.119836e-03 ; 7.634554e-03 ];
Tc_error_2  = [ 2.203611e+00 ; 5.173672e+00 ; 1.735589e+01 ];

%-- Image #3:
omc_3 = [ 2.213139e+00 ; 1.884386e+00 ; -1.573090e-01 ];
Tc_3  = [ -1.172016e+02 ; -9.993618e+01 ; 4.485114e+02 ];
omc_error_3 = [ 7.393324e-03 ; 6.489066e-03 ; 8.634491e-03 ];
Tc_error_3  = [ 2.315734e+00 ; 5.365812e+00 ; 1.820400e+01 ];

%-- Image #4:
omc_4 = [ 2.440231e+00 ; 1.578201e+00 ; -8.647504e-02 ];
Tc_4  = [ -1.163015e+02 ; -6.028143e+01 ; 4.175991e+02 ];
omc_error_4 = [ 8.420663e-03 ; 5.447199e-03 ; 7.589315e-03 ];
Tc_error_4  = [ 2.154640e+00 ; 5.020789e+00 ; 1.699951e+01 ];

%-- Image #5:
omc_5 = [ 2.494517e+00 ; 1.545467e+00 ; -1.455026e-01 ];
Tc_5  = [ -1.203426e+02 ; -8.672738e+00 ; 6.417579e+02 ];
omc_error_5 = [ 7.679018e-03 ; 5.142735e-03 ; 9.904109e-03 ];
Tc_error_5  = [ 3.294330e+00 ; 7.803680e+00 ; 2.617577e+01 ];

%-- Image #6:
omc_6 = [ 2.034454e+00 ; 2.263137e+00 ; -1.418732e-01 ];
Tc_6  = [ -1.132856e+02 ; -9.181149e+01 ; 4.690432e+02 ];
omc_error_6 = [ 4.140119e-03 ; 5.154624e-03 ; 9.009529e-03 ];
Tc_error_6  = [ 2.405466e+00 ; 5.618025e+00 ; 1.907896e+01 ];

%-- Image #7:
omc_7 = [ 2.189534e+00 ; 2.000460e+00 ; -7.614386e-02 ];
Tc_7  = [ -1.125464e+02 ; -6.238263e+01 ; 4.496635e+02 ];
omc_error_7 = [ 6.398305e-03 ; 5.568116e-03 ; 7.728505e-03 ];
Tc_error_7  = [ 2.316443e+00 ; 5.410956e+00 ; 1.831115e+01 ];

