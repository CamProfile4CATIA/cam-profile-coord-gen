function rise_cycloidal(startangle, stopangle, displacement,rotationsense,icorr )


global x;
global y;
global R;

for i=startangle+1:1:stopangle
    deltatheta=i-startangle;
    theta=startangle+deltatheta;
    kdash=(displacement/pi)*((pi*i/(startangle-stopangle))-(0.5*sind(360*deltatheta/(startangle-stopangle))));
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
