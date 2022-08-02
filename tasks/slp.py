from invoke import task
#from tasks.shared import is_local


@task
def deploy(ctx):
    """helm deploy of styra local-plane bundle server"""

    DEPLOY_SLP="""
helm template charts/styra-local-plane \
--set tenant=$TENANT \
--set system=$SYSTEM_NAME \
--set systemId=$SYSTEM_ID \
--set bearerToken=$STYRA_BEARER_TOKEN \
--set image.tag=$SLP_IMAGE_VERSION \
-f charts/styra-local-plane/values.yaml \
> test.yaml
    """
    print("Deploy SLP bundle server")
    ctx.run(DEPLOY_SLP)
