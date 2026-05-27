# Changelog

All notable changes to `scitex-sh` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.4]

- fix(workflows): resync integrated release pipeline from scitex-dev v0.11.20 (#4)
- fix(workflows): standardize to scitex-dev canonical set (#3)

## [0.1.3]

- fix(tests): clear PA-306 + PA-307 test-quality violations (#1)
- quality: subprocess-coverage wiring, codecov.yml, merged install-check, tracked `.scitex/dev/config.yaml`
- docs: add full README (Demo, Architecture, badges), skills, CONTRIBUTING.md, CHANGELOG.md
- docs: adopt inline [WHAT]/[WHEN]/[HOW] marker standard for skills
- ci: sync release pipeline, add newb doc-quality workflow, linguist-generated for _sphinx_html/
- chore(deps): bump scitex-dev pin floor to 0.11.7

## [0.1.2]

- audit: clear PS203 + PS204 + PS303 + PS107/110/112/113
- fix(release-safety): opt-in publish-pypi.yml (workflow_dispatch only)
- fix(skills): strip trailing `<!-- EOF -->` (SK211)
- fix(api): PA501/PA201/PA203 hygiene — `from __future__ import annotations`, `__version__` in `__all__`, fallback `0.0.0+local`
- chore(version): switch `__version__` to importlib.metadata to prevent drift

## [0.1.1]

- feat(skills): add SKILL.md (audit §E1); ship `_skills` via package-data
- feat(examples): add quickstart example + test_examples smoke test
- fix(test): use scitex_sh directly; importorskip umbrella scitex when checked
- ci: add CLA gate, install-test workflow, trusted-publisher PyPI workflow, standardized test matrix
- chore(extras): canonicalize `[project.optional-dependencies]`

## [0.1.0]

- Initial CHANGELOG entry — see git log for prior history.
