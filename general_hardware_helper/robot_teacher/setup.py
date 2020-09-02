from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['robot_teacher'],
    package_dir={'': 'src'},
    scripts=[   "scripts/joint_state_saver_node.py",
                "scripts/move_teached_node.py"]
)

setup(**setup_args)
