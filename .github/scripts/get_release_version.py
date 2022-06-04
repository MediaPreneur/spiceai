import os

with open(os.getenv("GITHUB_ENV"), "a") as githubEnv:
    with open("version.txt") as f:
        version = f.read()
    releaseVersion = version.strip()
    is_prerelease = True

    releaseNotePath = f"docs/release_notes/v{releaseVersion}.md"

    print(f"Checking if {releaseNotePath} exists")
    if os.path.exists(releaseNotePath):
        print(f"Found {releaseNotePath}")
        # Set LATEST_RELEASE to true
        githubEnv.write("LATEST_RELEASE=true\n")
        is_prerelease = False
    else:
        print(f"{releaseNotePath} is not found")
    print(f"Release build from v{releaseVersion}...")

    if is_prerelease:
        githubEnv.write("PRE_RELEASE=true\n")
    githubEnv.write("REL_VERSION={}\n".format(releaseVersion))
