function rise_uarm(startangle, stopangle, displacement, rotationsense,icorr)


global x;
global y;
global R;

for i=startangle+1:1:stopangle
    deltatheta=i-startangle;
    theta=startangle+deltatheta;
    if deltatheta <= (stopangle-startangle)/2;
        kdash=2*displacement*(deltatheta/(stopangle-startangle))^2;
    elseif deltatheta > (stopangle-startangle)/2;
        kdash=displacement-2*displacement*(1-(deltatheta/(stopangle-startangle)))^2;
    end
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
