# Copyright (c) 2024 IHU Liryc, Université de Bordeaux, Inria.
# License: BSD-3-Clause


from distutils.core import setup


setup(name='mbox_vtk_viewer',
      version='0.0',
      packages=['mbox_vtk_viewer'],
      entry_points = {
          'musicbox.': [
              'vtk = mbox_vtk_viewer:Viewer'
          ]
      }
)
