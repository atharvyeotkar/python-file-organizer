
def search():
    import os
    import shutil
    from pathlib import Path
    
    starting_path = input("Enter the path:")
    home_path = Path.home()
    main_st_path = home_path / starting_path
    print("the  final starting path is:",main_st_path)

    
    destination_path = input("Enter the destination:")

    main_des_path = home_path / destination_path
    
    files = os.listdir(main_st_path)
    print(files)
    
    for root, dirs, files in os.walk(main_st_path):
        print("current Folder:", root)
        print("Folders:", dirs)
        print("Files:",files)

        if ".jpg" in items:
           source_path = os.path.join(main_st_path,items)
           destination_file_path = os.path.join(main_des_path,items)
           shutil.move(source_path,destination_file_path)
           print("Files Moved")
           
search()
          




   
    
  