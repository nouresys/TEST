"""
Configuration centralisée pour le chatbot HR
Optimisé pour CPU uniquement - Chargement unique des modèles
"""
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# ================================================
# CHEMINS BASE - NE PAS MODIFIER SANS NÉCESSITÉ
# ================================================
BASE_PATH = os.getenv(
    "BASE_PATH",
    r"D:\PARTAGE\Projet_Chatbot\chatbot_copy_V2 (2)\chatbot_copy_V2"
)

DRH_PATH = os.getenv(
    "DRH_PATH",
    r"Z:\Boutaina\Ressources Humaines & Communication"
)

LLM_PATH = os.getenv(
    "LLM_PATH",
    r"C:\Users\chalaouaneb\.cache\huggingface\hub\models--TheBloke--Mistral-7B-Instruct-v0.2-GGUF\snapshots\3a6fbf4a41a1d52e415a4958cde6856d34b2db93\mistral-7b-instruct-v0.2.Q4_K_M.gguf"
)

EMBEDDING_MODEL_NAME = os.getenv(
    "EMBEDDING_MODEL_NAME",
    r"C:\Users\chalaouaneb\.cache\huggingface\hub\models--BAAI--bge-m3"
)


# ================================================
# DOSSIERS DE SORTIE
# ================================================
OUTPUT_DIRS = {
    "pdf": os.path.join(BASE_PATH, "pdf_files"),
    "word": os.path.join(BASE_PATH, "word_files"),
    "ppt": os.path.join(BASE_PATH, "ppt_files"),
    "excel": os.path.join(BASE_PATH, "excel_files"),
    "images": os.path.join(BASE_PATH, "image_embeddings"),
    "outlook": os.path.join(BASE_PATH, "outlook_files")
}

# ================================================
# CHEMINS FAISS & MÉTADONNÉES
# ================================================
FAISS_INDEX_PATH = os.path.join(BASE_PATH, "faiss_index.idx")
VECTOR_META_PATH = os.path.join(BASE_PATH, "vector_metadata.json")
GLOBAL_META_PATH = os.path.join(BASE_PATH, "all_metadata.json")
LOG_FILE = os.path.join(BASE_PATH, "chatbot_sessions.txt")

# ================================================
# PARAMÈTRES RAG (Optimisés CPU)
# ================================================
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))
TOP_K = int(os.getenv("TOP_K", 7))
SIM_THRESHOLD = float(os.getenv("SIM_THRESHOLD", 0.15))
EMBEDDING_BATCH_SIZE = int(os.getenv("EMBEDDING_BATCH_SIZE", 64))

# ================================================
# PARAMÈTRES LLM (Optimisés CPU)
# ================================================
MAX_NEW_TOKENS = int(os.getenv("MAX_NEW_TOKENS", 400))
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.4))
TOP_P = float(os.getenv("TOP_P", 0.9))
REPETITION_PENALTY = float(os.getenv("REPETITION_PENALTY", 1.15))

# ================================================
# CONFIGURATION SERVEUR
# ================================================
FLASK_PORT = int(os.getenv("FLASK_PORT", 5010))
SOCKETIO_CORS = os.getenv("SOCKETIO_CORS", "http://localhost:3000")

# ================================================
# VÉRIFICATION AU DÉMARRAGE
# ================================================
def check_paths():
    """Vérifie que tous les chemins nécessaires existent"""
    checks = {
        "BASE_PATH": BASE_PATH,
        "LLM_PATH": LLM_PATH,
        "EMBEDDING_MODEL_NAME": EMBEDDING_MODEL_NAME,
        "FAISS_INDEX_PATH": FAISS_INDEX_PATH,
        "VECTOR_META_PATH": VECTOR_META_PATH
    }
    
    for name, path in checks.items():
        if os.path.exists(path):
            logger.info(f"[OK] {name}: {path}")
        else:
            logger.warning(f"[MISSING] {name}: {path}")

    if os.path.exists(FAISS_INDEX_PATH):
        logger.info("[INFO] FAISS index found - will be loaded directly (no regeneration)")
    else:
        logger.warning("[INFO] FAISS index not found - will be generated on first use")

check_paths()
