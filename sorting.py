import os, shutil

original_dataset_dir_in  = 'D:\Maze_Machine\input_pixel'
original_dataset_dir_out  = 'D:\Maze_Machine\output_pixel'

base_dir = 'D:\Maze_Machine\mazes'
os.mkdir(base_dir)

in_train_dir = os.path.join(base_dir, 'in_train')
os.mkdir(in_train_dir)
in_validation_dir = os.path.join(base_dir, 'in_validation')
os.mkdir(in_validation_dir)
in_test_dir = os.path.join(base_dir, 'in_test')
os.mkdir(in_test_dir)
out_train_dir = os.path.join(base_dir, 'out_train')
os.mkdir(out_train_dir)
out_validation_dir = os.path.join(base_dir, 'out_validation')
os.mkdir(out_validation_dir)
out_test_dir = os.path.join(base_dir, 'out_test')
os.mkdir(out_test_dir)

fnames = ['input{}.png'.format(i) for i in range(700)]  
for fname in fnames:                                                       
    src = os.path.join(original_dataset_dir_in, fname)                        
    dst = os.path.join(in_train_dir, fname)                              
    shutil.copyfile(src, dst)

fnames = ['input{}.png'.format(i) for i in range(700, 900)]  
for fname in fnames:                                                       
    src = os.path.join(original_dataset_dir_in, fname)                        
    dst = os.path.join(in_validation_dir, fname)                              
    shutil.copyfile(src, dst)

fnames = ['input{}.png'.format(i) for i in range(900, 1000)]  
for fname in fnames:                                                       
    src = os.path.join(original_dataset_dir_in, fname)                        
    dst = os.path.join(in_test_dir, fname)                              
    shutil.copyfile(src, dst)
    
fnames = ['output{}.png'.format(i) for i in range(700)]  
for fname in fnames:                                                       
    src = os.path.join(original_dataset_dir_out, fname)                        
    dst = os.path.join(out_train_dir, fname)                              
    shutil.copyfile(src, dst)

fnames = ['output{}.png'.format(i) for i in range(700, 900)]  
for fname in fnames:                                                       
    src = os.path.join(original_dataset_dir_out, fname)                        
    dst = os.path.join(out_validation_dir, fname)                              
    shutil.copyfile(src, dst)

fnames = ['output{}.png'.format(i) for i in range(900, 1000)]  
for fname in fnames:                                                       
    src = os.path.join(original_dataset_dir_out, fname)                        
    dst = os.path.join(out_test_dir, fname)                              
    shutil.copyfile(src, dst)
    
print('total training input images:', len(os.listdir(in_train_dir)))
print('total training output images:', len(os.listdir(out_train_dir)))
print('total test input images:', len(os.listdir(in_test_dir)))
print('total test output images:', len(os.listdir(out_test_dir)))
print('total validation input images:', len(os.listdir(in_validation_dir)))
print('total validation output images:', len(os.listdir(out_validation_dir)))