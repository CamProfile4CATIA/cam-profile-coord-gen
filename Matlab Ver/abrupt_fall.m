function abrupt_fall(startangle,displacement, rotationsense,icorr )


global x;
global y;
global R;

R=R-displacement;
i=startangle;
    if strcmp(rotationsense,'CW')
        x(i+icorr)=-R*sind(i);
    elseif strcmp(rotationsense,'CCW')
        x(i+icorr)=R*sind(i);
    end
    y(i+icorr)=R*cosd(i);

end
