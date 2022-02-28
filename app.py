#!/usr/bin/env python3
import os

import aws_cdk as cdk

from common.common_01_s3log_stack import Common-01-S3LogStack
from common.common_02_vpc_stack import Common_02_VpcStack
from common.common_03_sg_stack import Common_03_SGStack

app = cdk.App()
Common-01-S3LogStack(app, "Common-01-S3LogStack",)
Common_02_VpcStack(app, "Common_02_VpcStack",)
Common_03_SGStack(app, "Common_03_SGStack",)
app.synth()
