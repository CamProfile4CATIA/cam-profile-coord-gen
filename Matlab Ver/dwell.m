function dwell(startangle, stopangle, rotationsense,icorr)

global R;
global x;
global y;

for i=startangle+1:1:stopangle
    deltatheta=i-startangle;
    theta=startangle+deltatheta;  
    if strcmp(rotationsense,'CW')
        x(i+icorr)=-R*sind(i);
    elseif strcmp(rotationsense,'CCW')
        x(i+icorr)=R*sind(i);
    end
    y(i+icorr)=R*cosd(i);
end