#!/usr/bin/env python3
import os

import aws_cdk as cdk

from common.c01_s3log_stack import S3LogStack
from common.c02_vpc_stack import VpcStack
from common.c03_sg_stack import SGStack

app = cdk.App()
S3LogStack(app, "S3LogStack",)
VpcStack(app, "VpcStack",)
SGStack(app, "SGStack",)
app.synth()
