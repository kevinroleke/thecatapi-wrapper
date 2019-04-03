from distutils.core import setup
setup(
  name = 'thecatapi',
  packages = ['thecatapi'],
  version = '1.0',
  license='MIT',
  description = 'Python3 wrapper for TheCatAPI',
  author = 'Your name',
  author_email = 'your.email@address.com',
  url = 'https://github.com/your_github_username/your_future_repo',
  download_url = 'https://github.com/your_github_username/your_future_repo/archive/v_10.tar.gz',
  keywords = ['thecatapi'],
  install_requires=[
          'requests', 'file-magic-bin'
      ],
  classifiers=[
    'Programming Language : Python3'
  ],
)
