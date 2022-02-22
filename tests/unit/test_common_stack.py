import aws_cdk as core
import aws_cdk.assertions as assertions

from common.common_stack import CommonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in common/common_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CommonStack(app, "common")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
