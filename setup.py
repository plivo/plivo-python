from setuptools import find_packages, setup

long_description = '''\
The Plivo Python SDK makes it simpler to integrate communications into your
Python applications using the Plivo REST API. Using the SDK, you will be able
to make voice calls, send SMS and generate Plivo XML to control your call flows.

See https://github.com/plivo/plivo-python for more information.
'''

setup(
    name='plivo',
    version='4.18.0',
    description='A Python SDK to make voice calls & send SMS using Plivo and to generate Plivo XML',
    long_description=long_description,
    url='https://github.com/plivo/plivo-python',
    author='The Plivo SDKs Team',
    author_email='sdks@plivo.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Telephony',
    ],
    install_requires=[
        'requests >= 2, < 3',
        'six >= 1, < 2',
        'decorator >= 4, < 5',
        'lxml >= 3, < 5',
    ],
    keywords=['plivo', 'plivo xml', 'voice calls', 'sms'],
    include_package_data=True,
    packages=find_packages(exclude=['tests', 'tests.*']), )
