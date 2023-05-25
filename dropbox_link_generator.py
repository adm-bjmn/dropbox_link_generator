'''Dropbox link generator'''
import dropbox, sys, os
token = ''
dbx = dropbox.Dropbox(token)
rootdir = '/Users/adm.bjmn/Desktop' # stores root directory variable


def create_direct_link(specific_filename, destination_folder):
    file_found = False
    for dir, dirs, files in os.walk(rootdir):
        for file in files:
            if file == specific_filename:
                file_found = True  
                try:
                    dbx.files_get_metadata(path=f'/{destination_folder}')  # Check if destination folder exists
                except dropbox.exceptions.ApiError as err:
                    print(f"Destination folder '{destination_folder}' does not exist.")
                    continue 
                try:
                    file_path = os.path.join(dir, file)
                    dest_path = os.path.join(
                        f'/{destination_folder}/', file)
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
                except Exception as err: # Would be nice to learn more about specific errors so i can tidy up the output.
                    print(f"Failed to upload {file}: {err}")
    if not file_found:
        print('File not found')
                
    return "Finished."

def main():
    specific_filename = str(input(
        'Please type the name of the file you want to upload: '))
    destination_folder = input(
        'Please enter the name of the destination folder inside your dropbox:')

    
    
    print(create_direct_link(specific_filename, destination_folder))

#===== Program Start ===== 
if __name__=='__main__':
    main()