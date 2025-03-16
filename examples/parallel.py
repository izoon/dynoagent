import asyncio
from typing import Dict
from dynoagent import DynoAgent

# Define DynoAgent instances for different workflow steps
ingest_agent = DynoAgent(name="IngestAgent", role="Extractor", skills=["OCR", "Text Extraction"], goal="Extract text from receipts")
indexing_agent = DynoAgent(name="IndexingAgent", role="Indexer", skills=["Data Storage", "Vector DB"], goal="Index extracted text into a vector database")
analysis_agent = DynoAgent(name="AnalysisAgent", role="Analyzer", skills=["Summarization", "Pattern Recognition"], goal="Analyze and categorize receipt data")
review_agent = DynoAgent(name="ReviewAgent", role="Validator", skills=["Data Validation", "Accuracy Checking"], goal="Review extracted receipt data for correctness")
verification_agent = DynoAgent(name="VerificationAgent", role="Verifier", skills=["Identity Matching", "Fraud Detection"], goal="Cross-check user identity in the database")
approval_agent = DynoAgent(name="ApprovalAgent", role="Approver", skills=["Expense Approval", "Financial Decision Making"], goal="Approve or reject expense claims")

# 📝 Define the workflow execution in parallel
async def process_receipt_parallel(receipt_text: str, user_id: str) -> Dict:
    """
    Executes the full receipt processing pipeline using DynoAgent instances in parallel where possible.
    """
    extracted_text = await asyncio.to_thread(ingest_agent.perform_task, "Extract receipt text", receipt_text)
    indexing_task = asyncio.to_thread(indexing_agent.perform_task, "Index extracted text", extracted_text)
    analysis_task = asyncio.to_thread(analysis_agent.perform_task, "Analyze receipt data", extracted_text)
    indexed_text, summary = await asyncio.gather(indexing_task, analysis_task)
    review_task = asyncio.to_thread(review_agent.perform_task, "Review analyzed receipt", summary)
    verification_task = asyncio.to_thread(verification_agent.perform_task, "Verify user identity", user_id)
    review_status, verification_status = await asyncio.gather(review_task, verification_task)
    review_agent.dynamic_role_update(review_status)
    approval_status = await asyncio.to_thread(approval_agent.perform_task, "Approve expense", verification_status)

    return {
        "ExtractedText": extracted_text,
        "IndexedText": indexed_text,
        "Summary": summary,
        "ReviewStatus": review_status,
        "VerificationStatus": verification_status,
        "ApprovalStatus": approval_status
    }