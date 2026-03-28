<p align="center">
  <img src="img/logo.png" alt="Inworld AI Logo">
</p>

# Inworld AI TTS for Home Assistant

A Home Assistant integration for [Inworld AI Text-to-Speech (TTS)](https://platform.inworld.ai/).


[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=notf0und&repository=hass-inworld-tts&category=Integration)


[![GitHub Release](https://img.shields.io/github/release/notf0und/hass-inworld-tts.svg?style=flat-square)](https://github.com/notf0und/hass-inworld-tts/releases)
[![GitHub Activity](https://img.shields.io/github/commit-activity/y/notf0und/hass-inworld-tts.svg?style=flat-square)](https://github.com/notf0und/hass-inworld-tts/commits/main)
[![License](https://img.shields.io/github/license/notf0und/hass-inworld-tts.svg?style=flat-square)](LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.1+-blue?style=flat-square)](https://www.home-assistant.io)
[![HACS](https://img.shields.io/badge/HACS-Custom-orange?style=flat-square)](https://hacs.xyz/)

[![GitHub Sponsors][sponsorsbadge]][sponsors]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]


## Features

- 🔊 High-quality text-to-speech powered by Inworld AI
- 🎯 Easy configuration through Home Assistant UI
- 🔐 Secure API key management
- ☁️ Cloud-based processing
- 🌍 Support for 15 languages
- 🚀 Choose between TTS 1.5 Max (best quality) and TTS 1.5 Mini (ultra-fast)

## Installation

### Via HACS (Recommended)

Click the button above or follow these steps:

1. Open Home Assistant
2. Go to **Settings** → **Devices & Services** → **Home Assistant Community Store (HACS)**
3. Click **Explore & Download Repositories**
4. Search for **Inworld AI TTS**
5. Click **Download**
6. Restart Home Assistant

### Manual Installation

1. Copy the `inworld_tts` folder from `custom_components` to your Home Assistant `custom_components` directory:
   ```bash
   cp -r inworld_tts config/custom_components/
   ```

2. Restart Home Assistant

## Configuration

1. Go to **Settings** → **Devices & Services** → **+ Add Integration**
2. Search for **Inworld AI TTS**
3. Enter your [Inworld AI API key](https://platform.inworld.ai/api-keys)
4. Select the TTS model (`TTS 1.5 Max` or `TTS 1.5 Mini`)
5. Optionally set a default voice ID (e.g. `Dennis`)
6. Click **Submit**

## Usage

Once configured, you can use the TTS service:

```yaml
action: tts.speak
target:
   entity_id: tts.inworld_ai
data:
   message: Hello, this is a test message
   media_player_entity_id: media_player.living_room
```

Or in automations:

```yaml
automation:
  - alias: "Announce motion detection"
    trigger:
      platform: state
      entity_id: binary_sensor.motion_sensor
      to: "on"
    action: tts.speak
    target:
      entity_id: tts.inworld_ai
    data:
      message: Motion detected in the living room
      media_player_entity_id: media_player.living_room
```

Or add it to your voice assistant pipeline:

1. Go to **Settings** → **Voice Assistants** → **+ Add Assistant**
2. On field **Text-to-speech** → **Inworld AI**
3. Click **Create**
4. Done! Your voice assistant will now use Inworld AI for TTS responses.

## Getting an API Key

1. Visit [Inworld AI Portal](https://platform.inworld.ai/api-keys)
2. Sign up or log in
3. Click **API Keys** in the bottom left sidebar
4. Click **Generate new key**
5. Copy the **Basic (Base64)** authorization signature — this is your API key

> **Note:** Use the **Basic (Base64)** value, not the raw key or secret.

## Available Models

| Model | ID | Description |
|-------|----|-------------|
| TTS 1.5 Max | `inworld-tts-1.5-max` | Flagship model, best balance of quality and speed |
| TTS 1.5 Mini | `inworld-tts-1.5-mini` | Ultra-fast, most cost-efficient |

## Supported Languages

English, Chinese, Japanese, Korean, Russian, Italian, Spanish, Portuguese, French, German, Polish, Dutch, Hindi, Hebrew, Arabic.

## Support

For issues or feature requests, please visit the [GitHub Issues](https://github.com/notf0und/hass-inworld-tts/issues) page.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This integration is not officially affiliated with Inworld AI. It is a community-maintained integration.

[sponsorsbadge]: https://img.shields.io/badge/sponsor-GitHub-blue?style=flat-square
[sponsors]: https://github.com/sponsors/notf0und
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow?style=flat-square
[buymecoffee]: https://buymeacoffee.com/gonzarturm
