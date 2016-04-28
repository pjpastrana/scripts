#!/bin/bash

script_to_deploy=$1
deploy_path=~/usr/bin
echo "Deploying script $script_to_deploy to $deploy_path"
rm *~
cp $script_to_deploy.* $deploy_path/$script_to_deploy