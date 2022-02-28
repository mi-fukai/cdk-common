import aws_cdk as cdk
from aws_cdk import (
    Stack,
    cloudformation_include as cfn_inc,
)
from constructs import Construct
import common.constants

class SecurityGroupStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        template = cfn_inc.CfnInclude(self, "Template",
            template_file="01-Common-03-SecurityGroup.yml",
            parameters=dict(ServiceName=common.constants.SERVICE_NAME),
            preserve_logical_ids=False)
