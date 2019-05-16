cam = webcam(1);
tic
for k=1:100   
    I = snapshot(cam);
    I = rgb2gray(I);
    I2 = snapshot(cam);
    I2 = rgb2gray(I2); 
    Q = (I2 - I) > 20;
    Q2(:,:,1) = Q; Q2(:,:,2) = Q; Q2(:,:,3) = Q; 
    image(Q2);
    text(k*2, k*2, ['rate=' num2str(k / toc)], "Color", [1 1 1])
end
clear cam;