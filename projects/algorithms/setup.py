try: 
    from setuptools import setup
except ImportError:
    from distutils.core import setup 
    
config = { 
    'description': 'algorithm study',
    'author': 'Feyisayo Adediwura',
    'url': 'URL link',
    'download_url': 'Where to download link',
    'author_email': 'fish@temple.edu',
    'version': '1.0',
    'install_requirements': ['nose'],
    'packages': ['bisearch_1'],
    'scripts': [],
    'name' : 'bisearch1'
    }
    
setup(**config)