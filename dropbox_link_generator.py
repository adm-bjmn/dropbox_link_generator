'''Dropbox link generator'''
import os
import dropbox

def create_direct_link(dbx):
    '''
    create_direct_link uses the dropbox api to upload a 
    user specified file to a user specified dropbox folder
    and create a sharable link to the file once uploaded.
    '''
    
    specific_filename = str(input(
        'Please type the name of the file you want to upload: '))
    destination_folder = input(
        'Please enter the name of the destination folder inside your Dropbox:')
    rootdir = '/Users/adm.bjmn/Desktop'  # Root directory on machine
    file_found = False  # Variable to track if the file is found
    
    # Traverse through the directory tree
    for dir, dirs, files in os.walk(rootdir):
        for file in files:
            if file == specific_filename:  # Check if requested file exists
                file_found = True
                
                try:
                    # Check if the destination folder exists in Dropbox
                    dbx.files_get_metadata(path=f'/{destination_folder}')  
                except dropbox.exceptions.ApiError as err:
                    print(f"Destination folder '{destination_folder}' does not exist.")
                    break 
                try:
                    file_path = os.path.join(dir, file) # file path on machine
                    dest_path = os.path.join(f'/{destination_folder}/', file)
                    print(f'Uploading {file_path} to {dest_path}')
                    
                    with open(file_path, 'rb') as f:
                        response = dbx.files_upload(
                            f.read(), dest_path, mute=True)
                        
                    # Get the shared link of the uploaded file
                    settings = dropbox.sharing.SharedLinkSettings(
                        requested_visibility=dropbox.sharing.RequestedVisibility.public)
                    shared_link_metadata = dbx.sharing_create_shared_link_with_settings(
                        response.path_display, settings)
                    shared_link_url = shared_link_metadata.url
                    print('Shared Link URL:', shared_link_url)
                # Catch any exception that occurs during the upload process
                except Exception as err:  
                    print(f"Failed to upload {file}: {err}")
    
    if not file_found:  # If the file is not found in the search
        print('File not found')
                
    return "Finished."


def main():
    token = str(input('Please enter your Dropbox Token:'))
    dbx = dropbox.Dropbox(token)  # Create a Dropbox instance using the token
    print(create_direct_link(dbx))


#===== Program Start ===== 
if __name__=='__main__':
    main()
