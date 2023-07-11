import subprocess

def install_package(package):
    try:
        subprocess.check_call(['apt', 'install', '-y', package])
        print(f"Package '{package}' installed successfully using apt.")
    except subprocess.CalledProcessError:
        print(f"Failed to install package '{package}' using apt.")

def install_pip_package(package):
    try:
        subprocess.check_call(['pip', 'install', package])
        print(f"Package '{package}' installed successfully using pip.")
    except subprocess.CalledProcessError:
        print(f"Failed to install package '{package}' using pip.")

# Example usage
install_package('nano')
install_package('sl')
install_package('cowsay')
install_package('wget')
install_package('w3m')
install_package('git')
install_package('neofetch')
install_package('cpufetch')
install_package('tur-repo')
install_package('x11-repo')
install_package('fortune')
install_package('ttyper')
install_pip_package('requests')
install_pip_package('lolcat')
install_pip_package('art')
