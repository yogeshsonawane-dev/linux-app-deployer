from pathlib import Path

BASE_REPO_DIR = Path("/opt/repos")
BASE_DEPLOY_DIR = Path("/opt/app")

APPLICATIONS = {
    "famvest": {
        "git_url": "git@github.com/yogeshsonawane-dev/famvest.git",
        "branch": "main",
        "build_type": "maven",
        "artifact_path": "target/famvest-*.jar",
        "service_name": "famvest-app",
        "deploy_path": BASE_DEPLOY_DIR / "famvest",
        "symlink": "famvest.jar",
        "application_url": "https://famvest.upvaly.com"
    },
    "netly": {
        "git_url": "git@github.com/yogeshsonawane-dev/netly.git",
        "branch": "main",
        "build_type": "maven",
        "artifact_path": "target/netly-*.jar",
        "service_name": "netly-app",
        "deploy_path": BASE_DEPLOY_DIR / "netly",
        "symlink": "netly.jar",
        "application_url": "https://netly.upvaly.com"
    },
    "duebook": {
        "git_url": "git@github.com/yogeshsonawane-dev/duebook.git",
        "branch": "main",
        "build_type": "maven",
        "artifact_path": "target/duebook-*.jar",
        "service_name": "duebook-app",
        "deploy_path": BASE_DEPLOY_DIR / "duebook",
        "symlink": "duebook.jar",
        "application_url": "https://duebook.famvest.online"
    },
    "finapi": {
        "git_url": "git@github.com/yogeshsonawane-dev/finapi.git",
        "branch": "main",
        "build_type": "maven",
        "artifact_path": "target/finapi-*.jar",
        "service_name": "finapi-app",
        "deploy_path": BASE_DEPLOY_DIR / "finapi",
        "symlink": "finapi.jar",
        "application_url": "https://finapi.upvaly.com"
    }
}

ALLOWED_SERVICES = {"famvest-app", "netly-app", "duebook-app", "finapi-app"}

BUILD_COMMANDS = {
    "maven": ["mvn", "clean", "package", "-DskipTests"]
}
