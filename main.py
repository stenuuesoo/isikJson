import json
import logging
from typing import Any, Dict, List, Optional, Union

# Configure logging
logging.basicConfig(level=logging.INFO)

KeyType = Union[str, int]
NestedKeys = List[KeyType]

# Define constants for JSON keys
RESULT = "result"
RESPONSE = "response"
REPORT = "r:report"
RR437_RESPONSE = "prod:RR437Response"
ISIK = "Isik"
DOCUMENTS = "Dokumendid"
DOCUMENT = "Dokument"
DOCUMENT_VALIDITY = "KEHTIV"
DOCUMENT_TYPES = ["ELAMISLUBA", "ELAMISÕIGUS", "ELAMISLOAKAART", "PASS", "ISIKUTUNNISTUS"]


# Read and parse a JSON file
def read_file(file_path: str) -> Optional[Dict[str, Any]]:
    try:
        with open(file_path, "r") as file:
            raw_result = file.read().strip()
    except FileNotFoundError:
        logging.error(f"File {file_path} not found.")
        return None

    corrected_result = raw_result.replace(r'\"', '"')
    try:
        return json.loads(corrected_result)
    except json.JSONDecodeError as json_error:
        logging.error(f"An error occurred while parsing the JSON: {json_error}")
        return None


# Retrieve nested key values from a dictionary
def get_nested_key(data: Dict[str, Any], keys: List[str]) -> Optional[Any]:
    for key in keys:
        if key in data:
            data = data[key]
        else:
            return None
    return data


def extract_documents(parsed_result: Dict[str, Any]) -> Optional[List[Dict[str, Any]]]:
    """Extract document details from parsed JSON result. Retrieve nested key values from a dictionary."""
    return get_nested_key(
        parsed_result,
        [RESULT, RESPONSE, REPORT, RR437_RESPONSE, RESPONSE, ISIK, DOCUMENTS, DOCUMENT]
    )


def extract_multiple_keys(data: Dict[str, Any], key_paths: List[List[str]]) -> Dict[str, Optional[Any]]:
    """Extract multiple nested keys from a dictionary and return a dictionary of results"""
    results = {}
    for keys in key_paths:
        temp_data = data
        for key in keys:
            temp_data = temp_data.get(key, {})
        key_str = '.'.join(keys)
        results[key_str] = temp_data if temp_data else None
    return results


def fetch_data_from_keys(json_result: Dict[str, Any]) -> Dict[str, Optional[Any]]:
    """Fetch and return a dictionary of values corresponding to given nested keys."""
    key_paths: List[NestedKeys] = [
        [RESULT, RESPONSE, REPORT, RR437_RESPONSE, RESPONSE, ISIK, "Isik.Eesnimi"],
        [RESULT, RESPONSE, REPORT, RR437_RESPONSE, RESPONSE, ISIK, "Isik.Perenimi"],
        [RESULT, RESPONSE, REPORT, RR437_RESPONSE, RESPONSE, ISIK, DOCUMENTS, DOCUMENT]
    ]
    return extract_multiple_keys(json_result, key_paths)


def assemble_name_details(keys_result: Dict[str, Optional[Any]]) -> str:
    """Assemble and return the name details from the results."""
    first_name_key = '.'.join([RESULT, RESPONSE, REPORT, RR437_RESPONSE, RESPONSE, ISIK, "Isik.Eesnimi"])
    last_name_key = '.'.join([RESULT, RESPONSE, REPORT, RR437_RESPONSE, RESPONSE, ISIK, "Isik.Perenimi"])
    first_name = keys_result.get(first_name_key)
    last_name = keys_result.get(last_name_key)
    return f"{first_name or 'Unknown'} {last_name or 'Unknown'}"


def filter_documents(documents: List[Dict[str, Any]], doc_types: List[str], status: str) -> List[Dict[str, Any]]:
    """Filter documents based on types and status."""
    return [
        doc for doc in documents
        if doc.get("Dokument.Liik") in doc_types and doc.get("Dokument.Staatus") == status
    ]


def log_and_prepare_results(filtered_docs: List[Dict[str, Any]]) -> List[str]:
    """Prepare and log document details."""
    results = []
    for doc in filtered_docs:
        doc_type = doc["Dokument.Liik"]
        doc_number = doc["Dokument.Number"]
        doc_status = doc["Dokument.Staatus"]
        result_line = f"{doc_type} {doc_status} nr: {doc_number}"
        if "Dokument.KehtibKuni" in doc:
            result_line += f" kehtib kuni {doc['Dokument.KehtibKuni']}"
        logging.info(result_line)
        results.append(result_line)
    return results


def filter_and_log_documents(keys_result: Dict[str, Optional[Any]], search_criteria: Dict[str, str]) -> List[str]:
    """Filter, log, and prepare documents."""
    documents_entries_key = '.'.join([RESULT, RESPONSE, REPORT, RR437_RESPONSE, RESPONSE, ISIK, DOCUMENTS, DOCUMENT])
    documents_entries = keys_result.get(documents_entries_key)
    if documents_entries is None:
        logging.error("No documents found.")
        return []
    filtered_docs = filter_documents(documents_entries, search_criteria["types"], search_criteria["status"])
    return log_and_prepare_results(filtered_docs)


def save_to_file(name_details: str, results: List[str], file_name: str = "result.txt") -> None:
    """Save results to a file."""
    with open(file_name, "w") as file:
        file.write(f"{name_details}\n")
        for result in results:
            file.write(result + "\n")


def main() -> None:
    """Main function to orchestrate the operations."""
    json_result = read_file("data.txt")
    if json_result is None:
        return

    search_criteria: Dict[str, Union[str, List[str]]] = {
        "status": DOCUMENT_VALIDITY,
        "types": DOCUMENT_TYPES
    }

    keys_result = fetch_data_from_keys(json_result)
    name_details = assemble_name_details(keys_result)
    logging.info(name_details)

    results = filter_and_log_documents(keys_result, search_criteria)
    if results:
        save_to_file(name_details, results)


if __name__ == "__main__":
    main()