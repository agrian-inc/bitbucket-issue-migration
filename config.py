# Mercurial user to be used for the commits of the migration
MIGRATION_COMMITS_USER = "Viper Admin <viper-admin@inf.ethz.ch>"

# Github only accepts assignees from valid users. We map those users from bitbucket.
USER_MAPPING = {
    "fpoli_eth": "fpoli",
    "{c2aa01d7-5a75-490b-9af8-c779a5a0d8e8}": "fpoli",
    "{557058:2a067556-b105-4ce3-b3ec-bf9ecac58455}": "fpoli",
    "mueller55": "mueller55",
    "{b724c0a3-39ff-41aa-b1fd-5f56de2abe11}": "mueller55",
    "{557058:bfefff28-2e68-4d1d-b0d5-69e5ce90efa7}": "mueller55",
    "meilers": "marcoeilers",
    "{7f85133f-0a10-4b92-8999-c63c441c5ccd}": "marcoeilers",
    "{557058:c6529106-a880-4ce3-af30-0f1e3c584455}": "marcoeilers",
    "arquintl": "arquintl",
    "{c1e08586-0797-4f40-94f9-6cce84e16840}": "arquintl",
    "{5c7fbff372cb04154791cfc1}": "arquintl",
    "gauravpartha": "gauravpartha",
    "{d31d5389-4b39-46ea-8214-9f3f9a87c500}": "gauravpartha",
    "{5c4ade80dcae4f5d16e79771}": "gauravpartha",
    "gaurav_p": "gauravpartha",
    "{deffc63b-6882-4dda-aa41-bf0851238cbc}": "gauravpartha",
    "{557058:a7f9ad30-ffe0-4a50-afeb-607147624427}": "gauravpartha",
    "Felale": "Felalolf",
    "{2d51ceff-d0c5-4656-b8a1-6147060ead9d}": "Felalolf",
    "{557058:e76ac194-2aec-4301-89de-bf67e80c92d0}": "Felalolf",
    "vakaras": "vakaras",
    "{6ad52865-3508-470f-b76f-d4b777004bd0}": "vakaras",
    "{557058:887dd121-6a5e-47e1-bb06-3d64b8fa29c9}": "vakaras",
    "mschwerhoff": "mschwerhoff",
    "{b28c5356-f751-4ded-a285-0889774978e0}": "mschwerhoff",
    "{557058:10d3684e-4a6c-47c2-84e0-bc1f2579e650}": "mschwerhoff",
    "fabiopakk": "fabiopakk",
    "{8c641d69-0c7a-47f1-aefb-296c96e018dc}": "fabiopakk",
    "{557058:50339889-65da-459d-811e-7532e71d77f6}": "fabiopakk",
    "arshavir": "aterga",
    "{d07d8b38-defa-4eea-91ba-ea6e15e195d3}": "aterga",
    "{557058:77dc96fb-1a0a-400d-b39a-ccabd91c98a0}": "aterga",
    "dohrau": "dohrau",
    "{2e15b3e2-8fde-4c2c-b460-c9e3f71e90ff}": "dohrau",
    "{557058:ea8a9b05-5424-439a-b424-c39ebb31013f}": "dohrau",
    "martin_clochard": "MartinClochard",
    "{bd18d17f-6685-43a9-ab7b-e5ad71669cb3}": "MartinClochard",
    "{5af1bdbc626b42214cd30659}": "MartinClochard",
    "alexander_summers": "alexanderjsummers",
    "{19f8d68f-a7da-4d75-a765-0393770be2de}": "alexanderjsummers",
    "{557058:978738dd-952f-4b9f-8e6f-7982e018475b}": "alexanderjsummers",
    "walkersilas": "walkersilas",
    "wytseoortwijn": "wytseoortwijn",
}

# We map bitbucket's issue "kind" to github "labels".
KIND_MAPPING = {
    "bug": "bug",
    "enhancement": "enhancement",
    "proposal": "proposal",
    "task": "task",
}

# We map bitbucket's issue "priority" to github "labels".
PRIORITY_MAPPING = {
    "trivial": "trivial",
    "minor": "minor",
    "major": "major",
    "critical": "critical",
    "blocker": "blocker",
}

# We map bitbucket's issue "component" to github "labels".
COMPONENT_MAPPING = {
    "Consistency": "consistency",
    "Parser": "parser",
    "silver-obligations": "silver-obligations",
    "Triggers": "triggers",
    "Examples": "examples",
    "Functions": "functions",
    "Logging, Reporting, IDE": "logging-reporting-ide",
    "Magic Wands": "magic-wands",
    "Permissions": "permissions",
    "Quantified Permissions": "quantified-permissions",
    "Silver": "silver",
    "Z3": "z3"
}

# The only github states are "open" and "closed".
# Therefore, we map some bitbucket states to github "labels".
STATE_MAPPING = {
    "on hold": "on hold",
    "invalid": "invalid",
    "duplicate": "duplicate",
    "wontfix": "wontfix",
    "resolved": None,
    "new": None,
    "open": None,
    "closed": None,
    "DECLINED": "declined",
    "MERGED": "merged",
    "SUPERSEDED": "superseeded",
    "OPEN": None,
}

# Bitbucket has several issue and pull request states.
# All states that are not listed in this set will be closed.
OPEN_ISSUE_OR_PULL_REQUEST_STATES = {
    "open",
    "new",
    "on hold",
    "OPEN",
}

# Mapping of known Bitbucket to their corresponding GitHub repo
# This information is used to convert links
KNOWN_REPO_MAPPING = {
    "viperproject/silver": "viperproject/silver",
    "viperproject/carbon": "viperproject/carbon",
    "viperproject/silicon": "viperproject/silicon",
    "viperproject/viperserver": "viperproject/viperserver",
    "viperproject/axiom-profiler": "viperproject/axiom-profiler",
    "viperproject/viper-runner": "viperproject/viper-runner",
    "viperproject/arp-plugin": "viperproject/arp-plugin",
    "viperproject/arp-plugin-test": "viperproject/arp-plugin-test",
    "viperproject/termination-plugin": "viperproject/termination-plugin",
    "viperproject/viper-linux-dev": "viperproject/viper-linux-dev",
    "viperproject/viper-linux-dev-docker": "viperproject/viper-linux-dev-docker",
    "viperproject/chalice2silver": "viperproject/chalice2silver",
    "viperproject/sample": "viperproject/sample",
    "viperproject/viper_client": "viperproject/viper_client",
    "viperproject/viper-ide": "viperproject/viper-ide",
    "viperproject/ouroboros": "viperproject/ouroboros",
    "viperproject/tutorial": "viperproject/tutorial",
    "viperproject/viper-ide-deps": "viperproject/viper-ide-deps",
    "viperproject/scala2silver": "viperproject/scala2silver",
    "viperproject/commutativity-plugin": "viperproject/commutativity-plugin",
    "viperproject/commutativity-plugin-test": "viperproject/commutativity-plugin-test",
    "viperproject/silver-sif-extension": "viperproject/silver-sif-extension",
    "viperproject/silicon_qp_statistics": "viperproject/silicon_qp_statistics",
    "viperproject/silver_qp_statistics": "viperproject/silver_qp_statistics",
    "viperproject/rslfrontend-deps": "viperproject/rslfrontend-deps",
    "viperproject/verifythis2018": "viperproject/verifythis2018",
    "viperproject/internal": "viperproject/internal",
    "viperproject/silver-multisets": "viperproject/silver-multisets",
    "viperproject/viper-setcomps": "viperproject/viper-setcomps",
    "viperproject/viperproject.bitbucket.org": "viperproject/viperproject.bitbucket.org",
    "viperproject/viper-ide-docker": "viperproject/viper-ide-docker",
    "viperproject/verifast2chalice": "viperproject/verifast2chalice",
    "viperproject/viper-sublime-ide": "viperproject/Viper-Sublime-IDE",
    "viperproject/viper-sublime-ide-win": "viperproject/viper-sublime-ide-win",
    "viperproject/ychalice":"viperproject/ychalice",
    "viperproject/ychaliceobligations": "viperproject/ychaliceobligations",
    "viperproject/obligations-chalice2silver": "viperproject/obligations-chalice2silver",
    "viperproject/obligations-silicon": "viperproject/obligations-silicon",
    "viperproject/obligations-silver": "viperproject/obligations-silver",
    "viperproject/cc4s-contracts": "viperproject/cc4s-contracts",
    "viperproject/cc4s-rewriter": "viperproject/cc4s-rewriter",
    "viperproject/dafny-ide": "viperproject/dafny-ide",
    "viperproject/carbon_for_ide": "viperproject/carbon_for_ide",
    "viperproject/silicon_for_ide": "viperproject/silicon_for_ide",
    "viperproject/silicon-finegrained": "viperproject/silicon-finegrained",
    "viperproject/silver-finegrained": "viperproject/silver-finegrained",
    "viperproject/silver_for_ide": "viperproject/silver_for_ide",
    "viperproject/rust2viper": "viperproject/rust2viper",
    "viperproject/viperonline-server": "viperproject/viperonline-server",
    "viperproject/viperonline-tool-hoster": "viperproject/viperonline-tool-hoster",
    "viperproject/viperonline-tutorial-generator": "viperproject/viperonline-tutorial-generator",
    "viperproject/voila": "viperproject/voila",
    "viperproject/silicon-assertable": "viperproject/silicon-assertable",
    "viperproject/silver-assertable": "viperproject/silver-assertable",
    "viperproject/silver-coarse": "viperproject/silver-coarse",
    "viperproject/silicon-coarse": "viperproject/silicon-coarse",
    "viperproject/silicon-verifiedif": "viperproject/silicon-verifiedif",
    "viperproject/silver-attributes": "viperproject/silver-attributes",
    "viperproject/silver-verifiedif": "viperproject/silver-verifiedif",
    "viperproject/obligations-silver": "viperproject/obligations-silver",
    "Felale/gobra-one": "viperproject/gobra",
    "agrian/twilight": "agrian-inc/twilight",
    "agrian/kraken": "agrian-inc/kraken",
}

# Mapping of known Bitbucket repos to their number of issues.
# This information is used to correctly account for the offset
# of PRs' IDs
KNOWN_ISSUES_COUNT_MAPPING = {
    "viperproject/silver": 301,
    "viperproject/carbon": 296,
    "viperproject/silicon": 410,
    "viperproject/viperserver": 0,
    "viperproject/axiom-profiler": 18,
    "viperproject/viper-runner": 0,
    "viperproject/arp-plugin": 3,
    "viperproject/arp-plugin-test": 0,
    "viperproject/termination-plugin": 2,
    "viperproject/viper-linux-dev": 12,
    "viperproject/viper-linux-dev-docker": 2,
    "viperproject/chalice2silver": 87,
    "viperproject/sample": 91,
    "viperproject/viper_client": 0,
    "viperproject/viper-ide": 108,
    "viperproject/ouroboros": 0,
    "viperproject/tutorial": 3,
    "viperproject/viper-ide-deps": 0,
    "viperproject/scala2silver": 9,
    "viperproject/commutativity-plugin": 0,
    "viperproject/commutativity-plugin-test": 0,
    "viperproject/silver-sif-extension": 0,
    "viperproject/silicon_qp_statistics": 0,
    "viperproject/silver_qp_statistics": 0,
    "viperproject/rslfrontend-deps": 0,
    "viperproject/verifythis2018": 0,
    "viperproject/internal": 0,
    "viperproject/silver-multisets": 0,
    "viperproject/viper-setcomps": 0,
    "viperproject/viperproject.bitbucket.org": 0,
    "viperproject/viper-ide-docker": 0,
    "viperproject/verifast2chalice": 0,
    "viperproject/viper-sublime-ide": 0,
    "viperproject/viper-sublime-ide-win": 0,
    "viperproject/ychalice": 0,
    "viperproject/ychaliceobligations": 0,
    "viperproject/obligations-chalice2silver": 0,
    "viperproject/obligations-silicon": 0,
    "viperproject/obligations-silver": 0,
    "viperproject/cc4s-contracts": 0,
    "viperproject/cc4s-rewriter": 0,
    "viperproject/dafny-ide": 4,
    "viperproject/carbon_for_ide": 0,
    "viperproject/silicon_for_ide": 0,
    "viperproject/silicon-finegrained": 0,
    "viperproject/silver-finegrained": 0,
    "viperproject/silver_for_ide": 0,
    "viperproject/rust2viper": 0,
    "viperproject/viperonline-server": 0,
    "viperproject/viperonline-tool-hoster": 0,
    "viperproject/viperonline-tutorial-generator": 0,
    "viperproject/voila": 107,
    "viperproject/silicon-assertable": 0,
    "viperproject/silver-assertable": 0,
    "viperproject/silver-coarse": 0,
    "viperproject/silicon-coarse": 0,
    "viperproject/silicon-verifiedif": 0,
    "viperproject/silver-attributes": 0,
    "viperproject/silver-verifiedif": 0,
    "viperproject/obligations-silver": 0,
    "Felale/gobra-one": 46,
    "agrian/twilight": 0,
    "agrian/kraken": 0,
}

KNOWN_CMAP_PATHS = {
    "viperproject/silver": "migration_data/silver_cmap.txt",
    "viperproject/carbon": "migration_data/carbon_cmap.txt",
    "viperproject/silicon": "migration_data/silicon_cmap.txt",
    "viperproject/viperserver": "migration_data/viperserver_cmap.txt",
    "viperproject/axiom-profiler": "migration_data/axiom-profiler_cmap.txt",
    "viperproject/viper-runner": "migration_data/viper-runner_cmap.txt",
    "viperproject/arp-plugin": "migration_data/arp-plugin_cmap.txt",
    "viperproject/arp-plugin-test": "migration_data/arp-plugin-test_cmap.txt",
    "viperproject/termination-plugin": "migration_data/termination-plugin_cmap.txt",
    "viperproject/viper-linux-dev": "migration_data/viper-linux-dev_cmap.txt",
    "viperproject/viper-linux-dev-docker": "migration_data/viper-linux-dev-docker_cmap.txt",
    "viperproject/chalice2silver": "migration_data/chalice2silver_cmap.txt",
    "viperproject/sample": "migration_data/sample_cmap.txt",
    "viperproject/viper_client": "migration_data/viper_client_cmap.txt",
    "viperproject/viper-ide": "migration_data/viper-ide_cmap.txt",
    "viperproject/ouroboros": "migration_data/ouroboros_cmap.txt",
    "viperproject/tutorial": "migration_data/tutorial_cmap.txt",
    "viperproject/viper-ide-deps": "migration_data/viper-ide-deps_cmap.txt",
    "viperproject/scala2silver": "migration_data/scala2silver_cmap.txt",
    "viperproject/commutativity-plugin": "migration_data/commutativity-plugin_cmap.txt",
    "viperproject/commutativity-plugin-test": "migration_data/commutativity-plugin-test_cmap.txt",
    "viperproject/silver-sif-extension": "migration_data/silver-sif-extension_cmap.txt",
    "viperproject/silicon_qp_statistics": "migration_data/silicon_qp_statistics_cmap.txt",
    "viperproject/silver_qp_statistics": "migration_data/silver_qp_statistics_cmap.txt",
    "viperproject/rslfrontend-deps": "migration_data/rslfrontend-deps_cmap.txt",
    "viperproject/verifythis2018": "migration_data/verifythis2018_cmap.txt",
    "viperproject/internal": "migration_data/internal_cmap.txt",
    "viperproject/silver-multisets": "migration_data/silver-multisets_cmap.txt",
    "viperproject/viper-setcomps": "migration_data/viper-setcomps_cmap.txt",
    "viperproject/viperproject.bitbucket.org": "migration_data/viperproject.bitbucket.org_cmap.txt",
    "viperproject/viper-ide-docker": "migration_data/viper-ide-docker_cmap.txt",
    "viperproject/verifast2chalice": "migration_data/verifast2chalice_cmap.txt",
    "viperproject/viper-sublime-ide": "migration_data/Viper-Sublime-IDE_cmap.txt",
    "viperproject/viper-sublime-ide-win": "migration_data/viper-sublime-ide-win_cmap.txt",
    "viperproject/ychalice": "migration_data/ychalice_cmap.txt",
    "viperproject/ychaliceobligations": "migration_data/ychaliceobligations_cmap.txt",
    "viperproject/obligations-chalice2silver": "migration_data/obligations-chalice2silver_cmap.txt",
    "viperproject/obligations-silicon": "migration_data/obligations-silicon_cmap.txt",
    "viperproject/obligations-silver": "migration_data/obligations-silver_cmap.txt",
    "viperproject/cc4s-contracts": "migration_data/cc4s-contracts_cmap.txt",
    "viperproject/cc4s-rewriter": "migration_data/cc4s-rewriter_cmap.txt",
    "viperproject/dafny-ide": "migration_data/dafny-ide_cmap.txt",
    "viperproject/carbon_for_ide": "migration_data/carbon_for_ide_cmap.txt",
    "viperproject/silicon_for_ide": "migration_data/silicon_for_ide_cmap.txt",
    "viperproject/silicon-finegrained": "migration_data/silicon-finegrained_cmap.txt",
    "viperproject/silver-finegrained": "migration_data/silver-finegrained_cmap.txt",
    "viperproject/silver_for_ide": "migration_data/silver_for_ide_cmap.txt",
    "viperproject/rust2viper": "migration_data/rust2viper_cmap.txt",
    "viperproject/viperonline-server": "migration_data/viperonline-server_cmap.txt",
    "viperproject/viperonline-tool-hoster": "migration_data/viperonline-tool-hoster_cmap.txt",
    "viperproject/viperonline-tutorial-generator": "migration_data/viperonline-tutorial-generator_cmap.txt",
    "viperproject/voila": "migration_data/voila_cmap.txt",
    "viperproject/silicon-assertable": "migration_data/silicon-assertable_cmap.txt",
    "viperproject/silver-assertable": "migration_data/silver-assertable_cmap.txt",
    "viperproject/silver-coarse": "migration_data/silver-coarse_cmap.txt",
    "viperproject/silicon-coarse": "migration_data/silicon-coarse_cmap.txt",
    "viperproject/silicon-verifiedif": "migration_data/silicon-verifiedif_cmap.txt",
    "viperproject/silver-attributes": "migration_data/silver-attributes_cmap.txt",
    "viperproject/silver-verifiedif": "migration_data/silver-verifiedif_cmap.txt",
    "Felale/gobra-one": "migration_data/gobra_cmap.txt",
    "agrian/twilight": "../migrate/twilight.git/cmap.txt",
    "agrian/kraken": "../migrate/kraken.git/cmap.txt",
}
