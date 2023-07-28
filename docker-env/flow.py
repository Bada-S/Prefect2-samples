from prefect import flow
from prefect_shell import ShellOperation

@flow
def myFlow():
    ShellOperation(
        commands=[
            "echo $DOCKER_BUILDKIT"
        ],
    ).run()

if __name__ == "__main__":
    myFlow()