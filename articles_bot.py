from langchain.document_loaders import GoogleDriveLoader
from langchain.indexes import VectorstoreIndexCreator

ARTICLES_ID = "1mowUkXKPlyi2-7_zECsySL1D92-uYc1IVPYAtbafchA"

loader = GoogleDriveLoader(
    credentials_path="credentials.json", document_ids=[ARTICLES_ID], recursive=True
)
# https://python.langchain.com/docs/modules/data_connection/document_loaders/

index = VectorstoreIndexCreator().from_loaders([loader])


resp = index.query_with_sources("How long can a trustee hold their position?")
print(resp)
