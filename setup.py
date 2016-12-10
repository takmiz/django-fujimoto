import tarfile
tar=tarfile.open('django-fujimoto.tar', 'w')
tar.add('appspec.yml')
tar.add('requirements.txt')
tar.add('project')
tar.add('scripts')
tar.close()

from distutils.spawn import spawn
spawn(['gzip', '-f', 'django-fujimoto.tar'])
