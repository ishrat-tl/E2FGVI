from setuptools import setup

setup(
    name='e2fgvi',
    version='0.1.0',
    description='Flow-Guided Video Inpainting',
    url='https://github.com/ishrat-tl/E2FGVI',
    author=['Zhen Li', 'Cheng-Ze Lu'],
    author_email=['zhenli1031gmail.com', 'czlu919@outlook.com'],
    license='Attribution-NonCommercial 4.0 International',
    packages=['e2fgvi',
              'e2fgvi/core',
              'e2fgvi/model',
              'e2fgvi/model/modules'],
    install_requires=['torch',
                      'torchvision',
                      'torchaudio',
                      'opencv-python',
                      'scipy',
                      'numpy',
                      'scikit-image',
                      'tqdm',
                      'matplotlib'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Attribution-NonCommercial 4.0 International',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    info='Official code for "Towards An End-to-End Framework for Flow-Guided Video Inpainting" (CVPR2022)'
)
