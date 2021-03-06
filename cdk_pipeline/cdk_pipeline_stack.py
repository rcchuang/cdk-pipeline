from aws_cdk import core
from os import path 
import aws_cdk.aws_lambda as lmb
import aws_cdk.aws_apigateway as apigw

class CdkPipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        this_dir = path.dirname(__file__)

        handler = lmb.Function(
            self, 'HelloHandler',
            runtime=lmb.Runtime.PYTHON_3_7,
            code=lmb.Code.from_asset(path.join(this_dir, 'lambda')),
            handler='hello.handler',
        )

        gw = apigw.LambdaRestApi(
            self, 'Gateway',
            handler=handler.current_version)
        
        self.url_output = core.CfnOutput(self, "Url",
            value=gw.url)
