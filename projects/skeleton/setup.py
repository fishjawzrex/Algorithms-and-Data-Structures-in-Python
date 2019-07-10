try: 
    from setuptools import setup
except ImportError:
    from distutils.core import setup 
    
config = { 
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL link',
    'download_url': 'Where to download link',
    'author_email': 'My Email',
    'version': '1.0',
    'install_requirements': ['nose'],
    'packages': ['proj_name'],
    'scripts': [],
    'name' : 'project_name'
    }
    
setup(**config)