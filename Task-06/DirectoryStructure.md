## HOME ASSISTANT DIRECTORY LAYOUT

.
├── .HA_VERSION

├── .cloud

├── .storage

│   ├── auth

│   ├── auth_provider.homeassistant

│   ├── cloud

│   ├── core.area_registry

│   ├── core.config

│   ├── core.config_entries

│   ├── core.device_registry

│   ├── core.entity_registry

│   ├── core.restore_state

│   ├── frontend.user_data_7a04118ad289497dbaf068d2b098b016

│   ├── onboarding

│   └── person

├── automations.yaml

├── configuration.yaml

├── customize.yaml

├── groups.yaml

├── home-assistant.log

├── home-assistant_v2.db

├── home-assistant_v2.db-shm

├── home-assistant_v2.db-wal

├── scripts.yaml

├── secrets.yaml

└── tts

3 directories, 23 files



**.storage** directory contains a lot of user-related information, including user login information (username/password, encrypted in auth_provider.homeassistant file).

**configuration.yaml:** User-edited configuration files.

**home-assistant.log:** Run log (cleared with each reboot).

**home-assistant_v2.db:** Database..


