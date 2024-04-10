import os
import fnmatch
import sys


folder_path = "/home/venkateshar/Venky/Projects/Marcelo_task"
package_list = ['requests','numpy','pandas','scikit-learn','matplotlib','tensorflow','flask','beautifulsoup4', 'django']


def read_requirements(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def check_packages(package_list, requirements):
    packages = [lib.split('==')[0].lower() for lib in package_list]
    requirements_list = [lib.split('==')[0].lower() for lib in requirements]
    approved = []
    unapproved = []

    for requirement in requirements_list:
        if requirement in packages:
            approved.append(requirement)
        else:
            unapproved.append(requirement)

    return approved, unapproved


def find_requirements_file(folder, app_names):
    result = {}
    for app_name in app_names:
        app_folder = os.path.join(folder, app_name)
        for foldername, subfolders, filenames in os.walk(app_folder):
            for filename in filenames:
                if filename == 'requirements.txt':
                    result[app_name] = os.path.join(foldername, filename)
    return result


if __name__ == "__main__":

    arguments = sys.argv[1:]

    apps = [arg for arg in arguments]
 
    #To get the requirements.txt files from given apps
    requirements_paths = find_requirements_file(folder_path, apps)

    req_apps = []
    for app, req_file_path in requirements_paths.items():
        if os.path.exists(req_file_path):
            # Read and return the libraries from requirements.txt file
            requirements = read_requirements(req_file_path)
            #Return the matching and unmatching libraries records
            approved, unapproved = check_packages(package_list, requirements)

            req_apps.append(app)
            print(f"App: {app}")
            print("Approved Packages:")
            for package in approved:
                print(package)

            print("\nUnapproved Packages:")
            for package in unapproved:
                print(package)

            print("\n")
    
    # printing the app name wich don't have requirments.txt file

    apps_list = [s_app for s_app in apps if s_app not in req_apps ]
    if apps_list:
        print(f"No requirments.txt file Apps: {','.join(apps_list)}")

