try: 
    from setuptools import setup
except ImportError:
    from distutils.core import setup 
    
config = { 
    'description': 'Dynamic Array Exercise',
    'author': 'Feyisayo Adediwura',
    'url': 'URL link',
    'download_url': 'Where to download link',
    'author_email': 'fish@temple.edu',
    'version': '1.0',
    'install_requirements': ['nose'],
    'packages': ['d_array'],
    'scripts': [],
    'name' : 'd_array'
    }
    
setup(**config)