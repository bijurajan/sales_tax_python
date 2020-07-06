#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin('pypi:pybuilder_pytest')
use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")


name = "sales_tax_python"
default_task = "publish"


@init
def set_properties(project):
    project.get_property("pytest_extra_args").append("-x")
    project.build_depends_on("mockito")
