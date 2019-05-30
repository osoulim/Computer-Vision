img = imread('text.png');
center = [100 100];
radius = 20;
tickness = 2;

for x = center(1) - radius: center(1) + radius
    for y = center(2) - radius: center(2) + radius
        dx = center(1) - x;
        dy = center(2) - y;
        dis = sqrt(dx * dx + dy * dy);
        if(dis < radius + tickness && dis > radius - tickness)
            img(y, x) = 1;
        end
    end
end

imshow(img)