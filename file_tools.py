def file_organizer():
    import os
    import shutil
    from pathlib import Path
    count = 0

    starting_path = input("Enter the Folder:")
    destination_folder = input("Enter destination folder:")
    file_ext = input("Enter file extension:").lower()


    home_path = Path.home()

    main_st_path = home_path / starting_path

    if not main_st_path.exists():
       print("Starting folder does not exist.")
       return
    
    main_des_path = home_path / destination_folder

    if not main_des_path.exists():
     print("Destination Folder does not Exist.")
     return
    
    found = False

    for root, dirs, files in os.walk(main_st_path):
        

        for  file in files:

            if file.lower().endswith(file_ext):
                found = True

                source_path = os.path.join(root, file)
                destination_path = main_des_path / file

                while True:

                    if destination_path.exists():
                      
                      print(f"{file} already exist in destination, change the name or skip this file.")

                      new_main_name = input("Enter new name or Type Cancel to skip this file :").lower().strip()

                      if new_main_name == "cancel":  #Skip current file
                       break

                      
                      elif new_main_name == "":
                       print("New name cant be empty!")
                       continue
                      
                      else:
                      
                       new_file = new_main_name + file_ext
                       destination_path = main_des_path / new_file
                       continue

                    
                    else:

                       print("Moving file:")
                       print(source_path)
      

                       shutil.move(source_path, destination_path)
                       print("file moved!")
                       count += 1
                       break

    if found:

     print(f"{count} files moved successfully!")

    if not found :
       print("No matching files found.")
    
        
            
file_organizer()
          




   
    





   
    
  
  
