#!/usr/bin/env python3
import os

import aws_cdk as cdk

from common.s3log_stack import S3LogStack
from common.vpc_stack import VpcStack

app = cdk.App()
S3LogStack(app, "S3LogStack",)
VpcStack(app, "VpcStack",)
app.synth()
