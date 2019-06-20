% Intrinsic and Extrinsic Camera Parameters
%
% This script file can be directly executed under Matlab to recover the camera intrinsic and extrinsic parameters.
% IMPORTANT: This file contains neither the structure of the calibration objects nor the image coordinates of the calibration points.
%            All those complementary variables are saved in the complete matlab data file Calib_Results.mat.
% For more information regarding the calibration model visit http://www.vision.caltech.edu/bouguetj/calib_doc/


%-- Focal length:
fc = [ 1135.114827796511690 ; 1133.695354766027322 ];

%-- Principal point:
cc = [ 643.211814297354977 ; 362.151080933594073 ];

%-- Skew coefficient:
alpha_c = 0.000000000000000;

%-- Distortion coefficients:
kc = [ 0.134971386554822 ; -0.727156880896984 ; 0.000451629888921 ; -0.000712326305931 ; 0.000000000000000 ];

%-- Focal length uncertainty:
fc_error = [ 7.140881097749554 ; 6.738706983535214 ];

%-- Principal point uncertainty:
cc_error = [ 7.061348607954145 ; 6.082480424543037 ];

%-- Skew coefficient uncertainty:
alpha_c_error = 0.000000000000000;

%-- Distortion coefficients uncertainty:
kc_error = [ 0.026224037432175 ; 0.178667897039441 ; 0.002032086783770 ; 0.002628850337407 ; 0.000000000000000 ];

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
omc_1 = [ 2.054346e+00 ; 1.951502e+00 ; 1.159247e-01 ];
Tc_1  = [ -3.559088e+01 ; -8.552753e+01 ; 4.459054e+02 ];
omc_error_1 = [ 5.627162e-03 ; 5.005358e-03 ; 9.977728e-03 ];
Tc_error_1  = [ 2.788960e+00 ; 2.370441e+00 ; 2.847382e+00 ];

%-- Image #2:
omc_2 = [ 2.167457e+00 ; 2.123129e+00 ; -1.809699e-01 ];
Tc_2  = [ -1.169521e+02 ; -8.245603e+01 ; 4.621879e+02 ];
omc_error_2 = [ 5.157527e-03 ; 5.911429e-03 ; 1.131389e-02 ];
Tc_error_2  = [ 2.889690e+00 ; 2.477215e+00 ; 2.922652e+00 ];

%-- Image #3:
omc_3 = [ -2.088559e+00 ; -2.108945e+00 ; 5.152705e-01 ];
Tc_3  = [ -1.241919e+02 ; -8.222724e+01 ; 4.829947e+02 ];
omc_error_3 = [ 5.827311e-03 ; 4.472457e-03 ; 9.948703e-03 ];
Tc_error_3  = [ 3.028938e+00 ; 2.602074e+00 ; 2.869525e+00 ];

%-- Image #4:
omc_4 = [ 1.950736e+00 ; 1.906929e+00 ; 2.317911e-01 ];
Tc_4  = [ -3.517558e+01 ; -8.518440e+01 ; 3.803550e+02 ];
omc_error_4 = [ 5.553998e-03 ; 4.771116e-03 ; 8.814583e-03 ];
Tc_error_4  = [ 2.380618e+00 ; 2.019183e+00 ; 2.453349e+00 ];

%-- Image #5:
omc_5 = [ 1.818222e+00 ; 1.715877e+00 ; 4.433818e-01 ];
Tc_5  = [ -1.475633e+01 ; -7.731194e+01 ; 4.357827e+02 ];
omc_error_5 = [ 5.721930e-03 ; 4.623769e-03 ; 7.661115e-03 ];
Tc_error_5  = [ 2.718947e+00 ; 2.319611e+00 ; 2.913480e+00 ];

%-- Image #6:
omc_6 = [ 1.798075e+00 ; 1.778009e+00 ; 1.204261e-01 ];
Tc_6  = [ -5.520856e+01 ; -4.844145e+01 ; 6.503104e+02 ];
omc_error_6 = [ 5.244960e-03 ; 5.160277e-03 ; 8.602764e-03 ];
Tc_error_6  = [ 4.043797e+00 ; 3.481605e+00 ; 4.264680e+00 ];

%-- Image #7:
omc_7 = [ 1.897119e+00 ; 1.685683e+00 ; -5.567754e-01 ];
Tc_7  = [ -9.800746e+01 ; -8.213698e+01 ; 4.432543e+02 ];
omc_error_7 = [ 4.089158e-03 ; 5.367413e-03 ; 7.938510e-03 ];
Tc_error_7  = [ 2.778495e+00 ; 2.369908e+00 ; 2.637077e+00 ];

%-- Image #8:
omc_8 = [ 1.859611e+00 ; 1.985855e+00 ; -1.055461e+00 ];
Tc_8  = [ -8.470029e+01 ; -8.308034e+01 ; 5.227953e+02 ];
omc_error_8 = [ 3.387450e-03 ; 6.075545e-03 ; 8.739569e-03 ];
Tc_error_8  = [ 3.275551e+00 ; 2.807438e+00 ; 2.811676e+00 ];

%-- Image #9:
omc_9 = [ 1.891888e+00 ; 1.521894e+00 ; -3.671690e-01 ];
Tc_9  = [ -8.445767e+01 ; -7.722259e+01 ; 4.998146e+02 ];
omc_error_9 = [ 4.577126e-03 ; 5.119860e-03 ; 7.634342e-03 ];
Tc_error_9  = [ 3.122226e+00 ; 2.661963e+00 ; 3.094997e+00 ];

%-- Image #10:
omc_10 = [ 1.901296e+00 ; 1.790474e+00 ; -7.109014e-01 ];
Tc_10  = [ -9.138970e+01 ; -8.531830e+01 ; 4.475773e+02 ];
omc_error_10 = [ 3.853650e-03 ; 5.553552e-03 ; 8.220803e-03 ];
Tc_error_10  = [ 2.810914e+00 ; 2.395235e+00 ; 2.561373e+00 ];

%-- Image #11:
omc_11 = [ -2.057063e+00 ; -2.010563e+00 ; 2.390325e-01 ];
Tc_11  = [ -1.064021e+02 ; -7.358356e+01 ; 4.069258e+02 ];
omc_error_11 = [ 4.692849e-03 ; 4.479899e-03 ; 9.717341e-03 ];
Tc_error_11  = [ 2.546557e+00 ; 2.181404e+00 ; 2.506309e+00 ];

%-- Image #12:
omc_12 = [ 2.059684e+00 ; 2.066660e+00 ; 3.965625e-01 ];
Tc_12  = [ -8.158678e+01 ; -7.628573e+01 ; 3.772450e+02 ];
omc_error_12 = [ 5.634070e-03 ; 4.576356e-03 ; 9.090813e-03 ];
Tc_error_12  = [ 2.377668e+00 ; 2.035295e+00 ; 2.465682e+00 ];

