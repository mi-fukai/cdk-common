#!/usr/bin/env python3
import os

import aws_cdk as cdk

from common.c01_s3log_stack import S3LogStack
from common.c02_vpc_stack import VpcStack
from common.c03_securitygroup_stack import SecurityGroupStack
from common.c04_sns_stack import SnsStack

app = cdk.App()
S3LogStack(app, "01-S3LogStack",)
VpcStack(app, "C02-VpcStack",)
SecurityGroupStack(app, "C03-SecurityGroupStack",)
SnsStack(app, "C04-SnsStack",)
app.synth()
