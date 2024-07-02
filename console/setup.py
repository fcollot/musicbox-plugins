# Copyright (c) 2024 IHU Liryc, Université de Bordeaux, Inria.
# License: BSD-3-Clause


from distutils.core import setup


setup(name='mbox_console',
      version='0.0',
      packages=['mbox_console'],
      entry_points = {
          'musicbox.console': [
              'musicbox = mbox_console:Console'
          ]
      }
)
