from setuptools import setup, find_packages
#from distutils.core import setup
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'pocard',        
  packages = ['pocard'],   
  include_package_data=True,
  long_description=open(path.join(base_dir, "README.md"), encoding="utf-8").read(),
  long_description_content_type='text/markdown',
  version = '0.0.7',    
  license='MIT',     
  description = 'PokemonCard Generator', 
  author = 'Krypton Byte',                  
  author_email = 'galaxyvplus6434@gmail.com',     
  url = 'https://github.com/krypton-byte/pocard',   
  download_url = 'https://github.com/krypton-byte/pocard/archive/0.0.1.tar.gz',    
  keywords = ['POkemon', "pokemon", "yugioh", "card", "maker", "generator"], 
  install_requires=[           
          'pillow'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
