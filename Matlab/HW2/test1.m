I1 = imread("Ball_1.JPG");
hsv = rgb2hsv(I1);
h = hsv(:,:,1);
s = hsv(:,:,2);
v = hsv(:,:,3);

mask = h > 0.05 & h < 0.2 & s < 0.9  & v > 0.9;

se = strel('disk', 12);
mask = imopen(mask, se);

imshow(I1);
