from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='scrape-linkedin',
      version= "0.1",
      description='Linkedin scraper to get all details on public linkedin profiles.',
      long_description=readme(),
      author='Eric Fourrier',
      author_email='ericfourrier0@gmail.com',
      license = 'MIT',
      url='https://github.com/ericfourrier/scrape-linkedin',
      packages=['pylinkedin'],
      test_suite = 'test_linkedin',
      keywords=['linkedin','api', 'scraper'],
      zip_safe=False,
      install_requires=[
          'requests>=2.0.0',
          'lxml']
)
