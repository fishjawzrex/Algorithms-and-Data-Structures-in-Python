try: 
    from setuptools import setup
except ImportError:
    from distutils.core import setup 
    
config = { 
    'description': 'My Project',
    'author': 'Feyisayo Adediwura',
    'url': 'https:\\www.google.com',
    'download_url': 'Where to download link',
    'author_email': 'fish@temple.edu',
    'version': '1.0',
    'install_requirements': ['nose'],
    'packages': ['my_first_rename'],
    'scripts': [print "hello world!"],
    'name' : 'project_trial_1'
    }
    
setup(**config)