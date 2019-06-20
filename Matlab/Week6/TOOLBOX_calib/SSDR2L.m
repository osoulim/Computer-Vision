% *************************************************************************
% Title: Function-Compute Correlation between two images using the 
% similarity measure of Sum of Squared Differences (SSD) with Right Image 
% as reference.
% Author: Siddhant Ahuja
% Created: May 2008
% Copyright Siddhant Ahuja, 2008
% Inputs: Left Image (var: leftImage), Right Image (var: rightImage),
% Window Size (var: windowSize), Minimum Disparity (dispMin), Maximum
% Disparity (dispMax)
% Outputs: Disparity Map (var: dispMap), Time taken (var: timeTaken)
% Example Usage of Function: [dispMap, timeTaken]=funcSSDR2L('StereogramLeft.jpg', 'StereogramRight.jpg', 9, 0, 16);
% *************************************************************************
function [dispMap, timeTaken]=SSDR2L(leftImage, rightImage, windowSize, dispMin, dispMax)

    
        leftImage=rgb2gray(leftImage);
        leftImage=im2double(leftImage);

     
        rightImage=rgb2gray(rightImage);
        rightImage=im2double(rightImage);
 

% Find the size (columns and rows) of the left image and assign the rows to
% variable nrLeft, and columns to variable ncLeft
[nrLeft,ncLeft] = size(leftImage);
% Find the size (columns and rows) of the right image and assign the rows to
% variable nrRight, and columns to variable ncRight
[nrRight,ncRight] = size(rightImage);
% Check to see if both the left and right images have same number of rows
% and columns
if(nrLeft==nrRight && ncLeft==ncRight)
else
    error('Both left and right images should have the same number of rows and columns');
end
% Check the size of window to see if it is an odd number.
if (mod(windowSize,2)==0)
    error('The window size must be an odd number.');
end
% Check whether minimum disparity is less than the maximum disparity.
if (dispMin>dispMax)
    error('Minimum Disparity must be less than the Maximum disparity.');
end
% Create an image of size nrLeft and ncLeft, fill it with zeros and assign
% it to variable dispMap
dispMap=zeros(nrLeft, ncLeft);
% Find out how many rows and columns are to the left/right/up/down of the
% central pixel based on the window size
win=(windowSize-1)/2;
tic; % Initialize the timer to calculate the time consumed.
for i=1+win:1:nrLeft-win
    for j=1+win:1:ncLeft-win-dispMax
        prevSSD = 65532;
        bestMatchSoFar = dispMin;
        for dispRange=dispMin:1:dispMax
            ssd=0.0;
            for a=-win:1:win
                for b=-win:1:win
                    if  j+b+dispRange <= ncLeft
                        temp=rightImage(i+a,j+b)-leftImage(i+a,j+b+dispRange);
                        temp=temp*temp;
                        ssd=ssd+temp;
                    end
                end
            end
            if  prevSSD > ssd
                prevSSD = ssd;
                bestMatchSoFar = dispRange;
            end
        end
        dispMap(i,j) = bestMatchSoFar;
    end
end
% Stop the timer to calculate the time consumed.
timeTaken=toc;