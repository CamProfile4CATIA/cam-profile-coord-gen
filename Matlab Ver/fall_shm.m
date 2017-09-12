function fall_shm(startangle, stopangle, displacement, rotationsense,icorr)


global x;
global y;
global R;

for i=startangle+1:1:stopangle
    deltatheta=i-startangle;
    theta=startangle+deltatheta;
    kdash=-(displacement/2)*(1-(cosd((180/(stopangle-startangle))*deltatheta)));
    k=R+kdash;
    if strcmp(rotationsense,'CW')
        x(i+icorr)=-k*sind(i);
    elseif strcmp(rotationsense,'CCW')
        x(i+icorr)=k*sind(i);
    end
    y(i+icorr)=k*cosd(i);
end
R=k;
end
