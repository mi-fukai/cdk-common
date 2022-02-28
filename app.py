#!/usr/bin/env python3
import os

import aws_cdk as cdk

from common.c01_s3log_stack import C01-S3LogStack
from common.c02_vpc_stack import C02-VpcStack
from common.c03_sg_stack import C03-SGStack

app = cdk.App()
C01-S3LogStack(app, "C01-S3LogStack",)
C02-VpcStack(app, "C02-VpcStack",)
C03-SGStack(app, "C03-SGStack",)
app.synth()
