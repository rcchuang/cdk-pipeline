#!/usr/bin/env python3

from aws_cdk import core

from cdk_pipeline.cdk_pipeline_stack import CdkPipelineStack
from cdk_pipeline.pipeline_stack import PipelineStack 

app = core.App()
CdkPipelineStack(app, "cdk-pipeline")
PipelineStack(app, 'PipelineStack', env={
    'account': '344457656106',
    'region': 'us-east-1'
})

app.synth()
