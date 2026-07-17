"""Constants for the Inworld AI TTS integration."""

DOMAIN = "inworld_tts"

CONF_MODEL = "model"
CONF_DELIVERY_MODE = "delivery_mode"

MODEL_TTS_2 = "inworld-tts-2"
MODEL_TTS_1_5_MAX = "inworld-tts-1.5-max"
MODEL_TTS_1_5_MINI = "inworld-tts-1.5-mini"

MODELS = {
    MODEL_TTS_2: "TTS 2 (Flagship, natural-language steering)",
    MODEL_TTS_1_5_MAX: "TTS 1.5 Max (Best quality)",
    MODEL_TTS_1_5_MINI: "TTS 1.5 Mini (Ultra-fast)",
}

# Delivery mode only affects inworld-tts-2 (it replaces temperature there and is
# ignored by the 1.5 models).
DELIVERY_MODE_STABLE = "STABLE"
DELIVERY_MODE_BALANCED = "BALANCED"
DELIVERY_MODE_CREATIVE = "CREATIVE"

DELIVERY_MODES = {
    DELIVERY_MODE_STABLE: "Stable (most consistent)",
    DELIVERY_MODE_BALANCED: "Balanced (default)",
    DELIVERY_MODE_CREATIVE: "Creative (most expressive)",
}

DEFAULT_MODEL = MODEL_TTS_1_5_MAX
DEFAULT_VOICE = "Dennis"
DEFAULT_DELIVERY_MODE = DELIVERY_MODE_BALANCED

INWORLD_TTS_API_URL = "https://api.inworld.ai/tts/v1/voice"
INWORLD_VOICES_API_URL = "https://api.inworld.ai/tts/v1/voices"
