"""Constants for the Inworld AI TTS integration."""

DOMAIN = "inworld_tts"

CONF_MODEL = "model"

MODEL_TTS_1_5_MAX = "inworld-tts-1.5-max"
MODEL_TTS_1_5_MINI = "inworld-tts-1.5-mini"

MODELS = {
    MODEL_TTS_1_5_MAX: "TTS 1.5 Max (Best quality)",
    MODEL_TTS_1_5_MINI: "TTS 1.5 Mini (Ultra-fast)",
}

DEFAULT_MODEL = MODEL_TTS_1_5_MAX
DEFAULT_VOICE = "Dennis"

INWORLD_TTS_API_URL = "https://api.inworld.ai/tts/v1/voice"
INWORLD_VOICES_API_URL = "https://api.inworld.ai/tts/v1/voices"
