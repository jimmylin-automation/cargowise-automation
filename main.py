import time
import logging
from config import TEMPLATE_PATH, MATCH_THRESHOLD, DATE_TO_ENTER
from vision import find_eta_field
from automation import update_eta

# ==============================
# LOGGING SETUP
# ==============================

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

print("Starting CargoWise ETA automation...")

time.sleep(5)

confidence, position = find_eta_field(TEMPLATE_PATH)

print("Confidence:", confidence)

# ==============================
# SAFETY CHECK (BEFORE ACTION)
# ==============================

if confidence < 0.6:
    print("Low confidence — aborting to avoid wrong click")
    logging.warning(f"Aborted due to low confidence: {confidence}")
    exit()

# ==============================
# MAIN LOGIC
# ==============================

if confidence > MATCH_THRESHOLD:
    print("ETA field detected")

    update_eta(position, DATE_TO_ENTER)

    # ✅ LOG SUCCESS
    logging.info(f"ETA updated successfully | confidence={confidence}")

else:
    print("ETA field NOT found")

    # ✅ LOG FAILURE
    logging.info(f"ETA field NOT found | confidence={confidence}")