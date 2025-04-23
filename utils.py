import re
from typing import List, Tuple, Dict

PII_PATTERNS = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "phone_number": r"\b(\+91[-\s]?|0)?[6-9]\d{9}\b",
    "dob": r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
    "aadhar_num": r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "cvv_no": r"\b\d{3,4}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])/?([0-9]{2})\b",
    "full_name": r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b",
}


def mask_pii(text: str) -> Tuple[str, List[Dict[str, str]]]:
    masked_text = text
    entities = []

    for entity_type, pattern in PII_PATTERNS.items():
        for match in re.finditer(pattern, masked_text):
            original_value = match.group()
            start, end = match.span()
            placeholder = f"[{entity_type}]"
            masked_text = masked_text[:start] + placeholder + masked_text[end:]
            updated_end = start + len(placeholder)
            entities.append({
                "position": [start, updated_end],
                "classification": entity_type,
                "entity": original_value,
            })

    return masked_text, entities
