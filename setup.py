from setuptools import setup


setup(
    name="nb-convnet_mnist",
    packages= ['convnet_mnist'],
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'jupyter-server-proxy',
        'notebook'
    ],
    url="https://github.com/ouseful-PR/Hand-Written-Digit-Recognition",
    author="",
    description="tony.hirst@gmail.com",
    entry_points={
        'jupyter_serverproxy_servers': [
            'convnet_mnist = convnet_mnist:setup_convnet_mnist',
        ]
    })