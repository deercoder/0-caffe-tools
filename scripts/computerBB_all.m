
% compute the bounding box of images rendered from 3ds max

function computerBB_all()
inputDir='C:\Users\305\Desktop\workspace\photorealistic\results_12_16_posesplit_four';
%inputDir='C:\Users\305\Desktop\test';
filelist = dir(inputDir);

% create flipped images
%for i=1:length(filelist)
 %   if(~strcmp(filelist(i).name, '.') && ~strcmp(filelist(i).name, '..'))
  %      fprintf('Creating Flipped images for %s \n', filelist(i).name);
   %     flipImage([inputDir '/' filelist(i).name '/renderresultwithbackground_white']);
    %    flipImage([inputDir '/' filelist(i).name '/renderresultwithbackground']);
    %end    
%end

% calculate bbox
% for i=1:length(filelist)
%     if(~strcmp(filelist(i).name, '.') && ~strcmp(filelist(i).name, '..'))
%         fprintf('Calculating BBox for %s \n', filelist(i).name);
%         computerBB([inputDir '/' filelist(i).name '/renderresultwithbackground_white'], [inputDir  '/Annotation'], filelist(i).name);
%     end
% end
% end

for i=1:length(filelist)
    if(~strcmp(filelist(i).name, '.') && ~strcmp(filelist(i).name, '..'))
        fprintf('Calculating BBox for %s \n', filelist(i).name);
    
        computerBB([inputDir '/' filelist(i).name '/renderresultwithbackground_white'], ...
        'C:\Users\305\Desktop\workspace\exp_posesplit\voc_2014_four\Annotations', filelist(i).name);
    end
end
end