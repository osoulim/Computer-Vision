% Intrinsic and Extrinsic Camera Parameters
%
% This script file can be directly executed under Matlab to recover the camera intrinsic and extrinsic parameters.
% IMPORTANT: This file contains neither the structure of the calibration objects nor the image coordinates of the calibration points.
%            All those complementary variables are saved in the complete matlab data file Calib_Results.mat.
% For more information regarding the calibration model visit http://www.vision.caltech.edu/bouguetj/calib_doc/


%-- Focal length:
fc = [ 1779.712889125601805 ; 1770.887601441253082 ];

%-- Principal point:
cc = [ 2003.204694607302372 ; 1460.287560942156233 ];

%-- Skew coefficient:
alpha_c = 0.000000000000000;

%-- Distortion coefficients:
kc = [ -0.278995233654039 ; 0.113733511057968 ; 0.000599272542737 ; -0.000560563309742 ; 0.000000000000000 ];

%-- Focal length uncertainty:
fc_error = [ 5.474046151691344 ; 5.153589119061234 ];

%-- Principal point uncertainty:
cc_error = [ 5.352598758930660 ; 4.511206983157281 ];

%-- Skew coefficient uncertainty:
alpha_c_error = 0.000000000000000;

%-- Distortion coefficients uncertainty:
kc_error = [ 0.006292580346892 ; 0.013714994798879 ; 0.000509766891663 ; 0.000478138433510 ; 0.000000000000000 ];

%-- Image size:
nx = 4000;
ny = 3000;


%-- Various other variables (may be ignored if you do not use the Matlab Calibration Toolbox):
%-- Those variables are used to control which intrinsic parameters should be optimized

n_ima = 18;						% Number of calibration images
est_fc = [ 1 ; 1 ];					% Estimation indicator of the two focal variables
est_aspect_ratio = 1;				% Estimation indicator of the aspect ratio fc(2)/fc(1)
center_optim = 1;					% Estimation indicator of the principal point
est_alpha = 0;						% Estimation indicator of the skew coefficient
est_dist = [ 1 ; 1 ; 1 ; 1 ; 0 ];	% Estimation indicator of the distortion coefficients


%-- Extrinsic parameters:
%-- The rotation (omc_kk) and the translation (Tc_kk) vectors for every calibration image and their uncertainties

%-- Image #1:
omc_1 = [ 1.277538e+00 ; 2.572495e+00 ; -8.644579e-01 ];
Tc_1  = [ -5.928200e+01 ; -1.716006e+02 ; 7.533820e+02 ];
omc_error_1 = [ 2.223880e-03 ; 4.290458e-03 ; 5.619278e-03 ];
Tc_error_1  = [ 2.301609e+00 ; 1.961176e+00 ; 2.275771e+00 ];

%-- Image #2:
omc_2 = [ 1.911616e+00 ; 2.032888e+00 ; -6.173905e-01 ];
Tc_2  = [ -1.117756e+02 ; -8.980696e+01 ; 6.762427e+02 ];
omc_error_2 = [ 2.849920e-03 ; 3.839086e-03 ; 6.041793e-03 ];
Tc_error_2  = [ 2.043937e+00 ; 1.744782e+00 ; 2.058679e+00 ];

%-- Image #3:
omc_3 = [ 2.345164e+00 ; 1.067072e+00 ; -1.389362e-01 ];
Tc_3  = [ -1.286530e+02 ; -5.241289e+01 ; 6.059597e+02 ];
omc_error_3 = [ 3.407934e-03 ; 2.626773e-03 ; 5.317066e-03 ];
Tc_error_3  = [ 1.831198e+00 ; 1.562548e+00 ; 2.181396e+00 ];

%-- Image #4:
omc_4 = [ 2.197754e+00 ; 2.246169e+00 ; -1.417623e-06 ];
Tc_4  = [ -8.537352e+01 ; -1.209797e+02 ; 6.312025e+02 ];
omc_error_4 = [ 6.991375e-03 ; 7.475915e-03 ; 1.572090e-02 ];
Tc_error_4  = [ 1.915184e+00 ; 1.620358e+00 ; 2.314662e+00 ];

%-- Image #5:
omc_5 = [ -1.674123e+00 ; -1.781666e+00 ; 9.368312e-01 ];
Tc_5  = [ -4.941273e+01 ; -2.447553e+01 ; 7.849887e+02 ];
omc_error_5 = [ 3.254813e-03 ; 3.008363e-03 ; 4.458505e-03 ];
Tc_error_5  = [ 2.368866e+00 ; 2.006596e+00 ; 2.206565e+00 ];

%-- Image #6:
omc_6 = [ 1.725457e+00 ; 1.781018e+00 ; 6.819236e-01 ];
Tc_6  = [ -4.634883e+00 ; 1.005432e+01 ; 6.851162e+02 ];
omc_error_6 = [ 3.407097e-03 ; 2.796140e-03 ; 4.804275e-03 ];
Tc_error_6  = [ 2.068854e+00 ; 1.760672e+00 ; 2.507851e+00 ];

%-- Image #7:
omc_7 = [ 2.357271e+00 ; 5.404185e-01 ; -1.170031e-01 ];
Tc_7  = [ -1.948420e+02 ; -2.950070e+01 ; 6.764521e+02 ];
omc_error_7 = [ 3.418167e-03 ; 2.508204e-03 ; 5.051027e-03 ];
Tc_error_7  = [ 2.046760e+00 ; 1.769232e+00 ; 2.618742e+00 ];

%-- Image #8:
omc_8 = [ -2.216873e+00 ; -2.168554e+00 ; 1.070255e-02 ];
Tc_8  = [ -1.082690e+02 ; -3.935666e+01 ; 3.176739e+02 ];
omc_error_8 = [ 2.604484e-03 ; 2.848682e-03 ; 5.827536e-03 ];
Tc_error_8  = [ 9.627386e-01 ; 8.269428e-01 ; 1.104704e+00 ];

%-- Image #9:
omc_9 = [ -1.685479e+00 ; -1.891816e+00 ; -7.693256e-01 ];
Tc_9  = [ -1.020945e+02 ; -1.427195e+02 ; 3.562409e+02 ];
omc_error_9 = [ 2.186922e-03 ; 2.834194e-03 ; 4.448630e-03 ];
Tc_error_9  = [ 1.125218e+00 ; 9.839692e-01 ; 1.400569e+00 ];

%-- Image #10:
omc_10 = [ 1.779433e+00 ; 2.340397e+00 ; -6.635210e-01 ];
Tc_10  = [ -9.966008e+01 ; -1.091452e+02 ; 5.368838e+02 ];
omc_error_10 = [ 2.206588e-03 ; 3.720472e-03 ; 5.582617e-03 ];
Tc_error_10  = [ 1.627993e+00 ; 1.390262e+00 ; 1.562448e+00 ];

%-- Image #11:
omc_11 = [ 2.160003e+00 ; 1.642019e+00 ; -8.008270e-02 ];
Tc_11  = [ -1.204432e+02 ; -9.997972e+01 ; 4.827518e+02 ];
omc_error_11 = [ 2.937573e-03 ; 3.006053e-03 ; 5.293164e-03 ];
Tc_error_11  = [ 1.471106e+00 ; 1.249473e+00 ; 1.645186e+00 ];

%-- Image #12:
omc_12 = [ 2.202221e+00 ; 1.236362e+00 ; 1.115628e+00 ];
Tc_12  = [ -1.593195e+02 ; -8.160737e+01 ; 4.568337e+02 ];
omc_error_12 = [ 3.428172e-03 ; 2.239625e-03 ; 4.603062e-03 ];
Tc_error_12  = [ 1.467874e+00 ; 1.207436e+00 ; 1.828566e+00 ];

%-- Image #13:
omc_13 = [ 2.340428e+00 ; 9.789729e-01 ; 8.471249e-01 ];
Tc_13  = [ -1.254227e+02 ; -5.422998e+01 ; 6.868232e+02 ];
omc_error_13 = [ 3.922967e-03 ; 2.374402e-03 ; 5.411517e-03 ];
Tc_error_13  = [ 2.110697e+00 ; 1.771112e+00 ; 2.720505e+00 ];

%-- Image #14:
omc_14 = [ 2.404933e+00 ; 1.125138e+00 ; -1.894642e-01 ];
Tc_14  = [ -9.541365e+01 ; -6.529791e+01 ; 4.749471e+02 ];
omc_error_14 = [ 3.188395e-03 ; 2.347311e-03 ; 4.959821e-03 ];
Tc_error_14  = [ 1.440680e+00 ; 1.220629e+00 ; 1.617174e+00 ];

%-- Image #15:
omc_15 = [ -1.892550e+00 ; -1.823625e+00 ; 6.636691e-01 ];
Tc_15  = [ -1.568941e+02 ; -5.132816e+01 ; 3.096410e+02 ];
omc_error_15 = [ 2.955729e-03 ; 2.284776e-03 ; 3.878813e-03 ];
Tc_error_15  = [ 9.623638e-01 ; 8.352224e-01 ; 8.727517e-01 ];

%-- Image #16:
omc_16 = [ NaN ; NaN ; NaN ];
Tc_16  = [ NaN ; NaN ; NaN ];
omc_error_16 = [ NaN ; NaN ; NaN ];
Tc_error_16  = [ NaN ; NaN ; NaN ];

%-- Image #17:
omc_17 = [ -2.200820e+00 ; -2.229813e+00 ; 3.140415e-02 ];
Tc_17  = [ -9.958675e+01 ; -5.956330e+01 ; 3.393114e+02 ];
omc_error_17 = [ 2.788384e-03 ; 2.988825e-03 ; 6.266800e-03 ];
Tc_error_17  = [ 1.029983e+00 ; 8.789134e-01 ; 1.163230e+00 ];

%-- Image #18:
omc_18 = [ 2.025033e+00 ; 2.042142e+00 ; 4.139138e-01 ];
Tc_18  = [ -5.933633e+01 ; -6.594062e+01 ; 1.576966e+02 ];
omc_error_18 = [ 2.540346e-03 ; 1.885258e-03 ; 4.089336e-03 ];
Tc_error_18  = [ 5.037488e-01 ; 4.150497e-01 ; 5.508202e-01 ];

