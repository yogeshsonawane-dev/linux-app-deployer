from pathlib import Path

BASE_REPO_DIR = Path("/opt/repos")
BASE_DEPLOY_DIR = Path("/opt/app")

APPLICATIONS = {
    "famvest": {
        "git_url": "git@github.com:yogeshsonawane-dev/famvest.git",
        "branch": "main",
        "build_type": "maven",
        "artifact_path": "target/famvest-*.jar",
        "service_name": "famvest-app",
        "deploy_path": BASE_DEPLOY_DIR / "famvest",
        "symlink": "famvest.jar",
        "application_url": "https://famvest.upvaly.com",
        "api_health_end_point": "https://api.famvest.upvaly.com/api/public/health"
    },
    "netly": {
        "git_url": "git@github.com:yogeshsonawane-dev/netly.git",
        "branch": "main",
        "build_type": "maven",
        "artifact_path": "target/netly-*.jar",
        "service_name": "netly-app",
        "deploy_path": BASE_DEPLOY_DIR / "netly",
        "symlink": "netly.jar",
        "application_url": "https://netly.upvaly.com",
        "api_health_end_point": "https://api.netly.upvaly.com/api/public/health"
    },
    "duebook": {
        "git_url": "git@github.com:yogeshsonawane-dev/duebook.git",
        "branch": "main",
        "build_type": "maven",
        "artifact_path": "target/duebook-*.jar",
        "service_name": "duebook-app",
        "deploy_path": BASE_DEPLOY_DIR / "duebook",
        "symlink": "duebook.jar",
        "application_url": "https://duebook.upvaly.online",
        "api_health_end_point": "https://duebook.upvaly.com/api/public/health"
    },
    "finapi": {
        "git_url": "git@github.com:yogeshsonawane-dev/finapi.git",
        "branch": "main",
        "build_type": "maven",
        "artifact_path": "target/finapi-*.jar",
        "service_name": "finapi-app",
        "deploy_path": BASE_DEPLOY_DIR / "finapi",
        "symlink": "finapi.jar",
        "application_url": "https://finapi.upvaly.com",
        "api_health_end_point": "https://api.finapi.upvaly.com/api/public/health"
    },
    "adminhub": {
        "git_url": "git@github.com:yogeshsonawane-dev/admin-hub.git",
        "branch": "main",
        "build_type": "maven",
        "artifact_path": "target/admin-hub-*.jar",
        "service_name": "adminhub-app",
        "deploy_path": BASE_DEPLOY_DIR / "admin-hub",
        "symlink": "admin-hub.jar",
        "application_url": "https://adminhub.upvaly.com",
        "api_health_end_point": "https://adminhub.upvaly.com/api/public/health"
    }

}

ALLOWED_SERVICES = {"famvest-app", "netly-app", "duebook-app", "finapi-app", "adminhub-app"}

BUILD_COMMANDS = {
    "maven": ["mvn", "clean", "package", "-DskipTests"]
}
