from sqlmodel import Session, select
from backend.app.models import User, Report, Job, ExtractedValue


def test_database_table_creation_and_insertion(session: Session):
    # Test User insertion
    user = User(name="Test User", age=30, gender="male", pregnant=False, preferred_language="en")
    session.add(user)
    session.commit()
    session.refresh(user)

    assert user.id is not None
    assert user.name == "Test User"

    # Test Report insertion
    report = Report(user_id=user.id, doc_type="lab_report", source_filename="sample_cbc.pdf", status="queued")
    session.add(report)
    session.commit()
    session.refresh(report)

    assert report.id is not None
    assert report.user_id == user.id

    # Verify query retrieves record
    db_report = session.exec(select(Report).where(Report.id == report.id)).first()
    assert db_report is not None
    assert db_report.source_filename == "sample_cbc.pdf"
