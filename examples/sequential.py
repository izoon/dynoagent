from typing import Dict
from dynoagent import DynoAgent

# Define DynoAgent instances for different workflow steps
ingest_agent = DynoAgent(name="IngestAgent", role="Extractor", skills=["OCR", "Text Extraction"], goal="Extract text from receipts")
indexing_agent = DynoAgent(name="IndexingAgent", role="Indexer", skills=["Data Storage", "Vector DB"], goal="Index extracted text into a vector database")
analysis_agent = DynoAgent(name="AnalysisAgent", role="Analyzer", skills=["Summarization", "Pattern Recognition"], goal="Analyze and categorize receipt data")
review_agent = DynoAgent(name="ReviewAgent", role="Validator", skills=["Data Validation", "Accuracy Checking"], goal="Review extracted receipt data for correctness")
verification_agent = DynoAgent(name="VerificationAgent", role="Verifier", skills=["Identity Matching", "Fraud Detection"], goal="Cross-check user identity in the database")
approval_agent = DynoAgent(name="ApprovalAgent", role="Approver", skills=["Expense Approval", "Financial Decision Making"], goal="Approve or reject expense claims")

# 📝 Define the workflow execution sequentially
def process_receipt_sequential(receipt_text: str, user_id: str) -> Dict:
    """
    Executes the full receipt processing pipeline using DynoAgent instances sequentially.
    """
    extracted_text = ingest_agent.perform_task("Extract receipt text", receipt_text)
    indexed_text = indexing_agent.perform_task("Index extracted text", extracted_text)
    summary = analysis_agent.perform_task("Analyze receipt data", indexed_text)
    review_status = review_agent.perform_task("Review analyzed receipt", summary)
    review_agent.dynamic_role_update(review_status)
    verification_status = verification_agent.perform_task("Verify user identity", user_id)
    approval_status = approval_agent.perform_task("Approve expense", verification_status)

    return {
        "ExtractedText": extracted_text,
        "IndexedText": indexed_text,
        "Summary": summary,
        "ReviewStatus": review_status,
        "VerificationStatus": verification_status,
        "ApprovalStatus": approval_status
    }