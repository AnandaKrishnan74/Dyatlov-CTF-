import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise RuntimeError("Set SECRET_KEY in your local .env file before starting the application.")

    SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE", "False").lower() == "true"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"

    # Keep real flag answers in the untracked .env file, never in public source code.
    FLAGS = {
        1: os.environ.get("FLAG_STAGE_1"),
        2: os.environ.get("FLAG_STAGE_2"),
        3: os.environ.get("FLAG_STAGE_3"),
        4: os.environ.get("FLAG_STAGE_4"),
        5: os.environ.get("FLAG_STAGE_5"),
        6: os.environ.get("FLAG_STAGE_6"),
        7: os.environ.get("FLAG_STAGE_7"),
    }

    missing_flags = [stage for stage, value in FLAGS.items() if not value]
    if missing_flags:
        raise RuntimeError(
            "Missing flag values in .env for stages: "
            + ", ".join(str(stage) for stage in missing_flags)
        )

    STAGE_TITLES = {
        1: "The Missing Expedition",
        2: "The Last Diary Entry",
        3: "The Forgotten Checkpoint",
        4: "The Photograph That Should Not Exist",
        5: "The Restricted Report",
        6: "The Unidentified Frequency",
        7: "The Final Truth",
    }

    STAGE_DESCRIPTIONS = {
        1: "Establish the facts surrounding the disappearance of the expedition.",
        2: "Recover the meaning of Dyatlov's suspicious diary entry.",
        3: "Reconstruct the expedition's route using checkpoint records.",
        4: "Investigate an unusual expedition photograph that should not exist.",
        5: "Investigate discrepancies between search-party evidence and official reports - Recovered Documents.",
        6: "Investigate the strange radio transmission intercepted during the search.",
        7: "Reconstruct the final sequence of events and recover the final case evidence.",
    }
