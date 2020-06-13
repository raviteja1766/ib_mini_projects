#!/usr/bin/env python
import os
import boto3
import argparse
import base64


def get_stage_vars(function_name, aws_region='eu-west-1', profile_name=None):
    import boto3
    if profile_name:
        session = boto3.Session(profile_name=profile_name)
    else:
        session = boto3.Session()

    lambda_client = session.client('lambda', region_name=aws_region)
    response = lambda_client.get_function_configuration(FunctionName=function_name)
    return response["Environment"]["Variables"]


args = argparse.ArgumentParser(add_help=False)
args.add_argument('project_name')
args.add_argument('branch')
args.add_argument('aws_region', default="ap-south-1")
args.add_argument('profile_name', default=None)


def main():
    flags = args.parse_args()
    old_project_name = flags.project_name
    branch = flags.branch
    aws_region = flags.aws_region
    profile_name = flags.profile_name
    function_name = old_project_name +"-"+ branch

    stage_vars = get_stage_vars(function_name, aws_region, profile_name)
    if isinstance(stage_vars, dict):
        exp = "export DJANGO_SETTINGS_MODULE=\"%s.settings.%s\"" % (
            old_project_name, branch
        )
        os.system(exp)
        print(exp)
        for key, val in stage_vars.items():
            exp = "export %s=\"%s\"" % (key, val)
            os.system(exp)
            print(exp)

    print("\n\n\n# Now Execute python manage.py <your_management_command>")


if __name__ == "__main__":
    """
    * Download & place get_stage_vars.py your project directory

    ```sh

    $python get_stage_vars.py project_name branch aws_region
        usage: get_stage_vars.py project_name branch aws_region

    $python get_stage_vars.py ib_service alpha eu-west-1
    ```

    * above script will be usefull to execute the management commands in zappa based deployments
    """
    main()
