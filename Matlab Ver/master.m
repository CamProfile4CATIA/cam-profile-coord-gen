function master(fullpathname)
[~,~,sheetdata]=xlsread('Template.xlsx');
[rows,columns]=size(sheetdata);

if exist(fullpathname, 'file')==0
    h = msgbox('Specified file does not exist!','Error','error');
    return
  
        
elseif sum([sheetdata{7:rows,4}])~= 360
    h = msgbox('Incomplete data :Total angle is not 360!','Error','error');
    return;
end
    

global x ;
global y ;
global R ;

dropcount=0;
for i=7:1:rows
    if strmatch(sheetdata(i,1),'FALL')
        if sheetdata{i,4}==0
        dropcount=dropcount+1;
        end
    end
end


x=zeros(1,361+dropcount);
y=zeros(1,361+dropcount);
icorr=0;

startangle=0;
radius=sheetdata{4,3};
R=radius;

for i=7:1:rows
    if strmatch(sheetdata(i,1),'RISE')
        if strmatch(sheetdata(i,2),'UV')
            stopangle=startangle+sheetdata{i,4};
            displacement=sheetdata{i,3};
            rise_uv(startangle, stopangle, displacement,sheetdata{3,3},icorr)
            startangle=stopangle;
        elseif strmatch(sheetdata(i,2),'SHM')
            stopangle=startangle+sheetdata{i,4};
            displacement=sheetdata{i,3};
            rise_shm(startangle, stopangle, displacement,sheetdata{3,3},icorr)
            startangle=stopangle;    
        elseif strmatch(sheetdata(i,2),'CYCLOIDAL')
            stopangle=startangle+sheetdata{i,4};
            displacement=sheetdata{i,3};
            rise_cycloidal(startangle, stopangle, displacement,sheetdata{3,3},icorr)
            startangle=stopangle;
        elseif strmatch(sheetdata(i,2),'UARM')
            stopangle=startangle+sheetdata{i,4};
            displacement=sheetdata{i,3};
            rise_uarm(startangle, stopangle, displacement,sheetdata{3,3},icorr)
            startangle=stopangle;
         
       
            
        end
            
    elseif strmatch(sheetdata(i,1),'FALL')
        
        if sheetdata{i,4}==0
            icorr=icorr+1;
            abrupt_fall(startangle, sheetdata{i,3}, sheetdata{3,3},icorr)
            
        elseif strmatch(sheetdata(i,2),'UV')
            stopangle=startangle+sheetdata{i,4};
            displacement=sheetdata{i,3};
            fall_uv(startangle, stopangle, displacement,sheetdata{3,3},icorr)
            startangle=stopangle;
        elseif strmatch(sheetdata(i,2),'SHM')
            stopangle=startangle+sheetdata{i,4};
            displacement=sheetdata{i,3};
            fall_shm(startangle, stopangle, displacement,sheetdata{3,3},icorr)
            startangle=stopangle;
        elseif strmatch(sheetdata(i,2),'CYCLOIDAL')
            stopangle=startangle+sheetdata{i,4};
            displacement=sheetdata{i,3};
            fall_cycloidal(startangle, stopangle, displacement,sheetdata{3,3},icorr)
            startangle=stopangle;
        elseif strmatch(sheetdata(i,2),'UARM')
            stopangle=startangle+sheetdata{i,4};
            displacement=sheetdata{i,3};
            fall_uarm(startangle, stopangle, displacement,sheetdata{3,3},icorr)
            startangle=stopangle;
        
            
        end
    elseif strmatch(sheetdata(i,1),'DWELL')
        stopangle=startangle+sheetdata{i,4};
        dwell(startangle, stopangle,sheetdata{3,3},icorr)
        startangle=stopangle;
    end
end
x(360+dropcount)=0;
y(360+dropcount)=radius;

x(361+dropcount)=x(1);
y(361+dropcount)=y(1);

xlswrite('Coordinates.xlsx',[x' y']) 
h = msgbox('Coordinates sucessfully Generated!','Success');
end
    
        