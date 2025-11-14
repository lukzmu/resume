from datetime import datetime

import pydantic


class PersonSchema(pydantic.BaseModel):
    person_name: str
    title: str
    contact: list[str] | None = None


class JobSchema(pydantic.BaseModel):
    job_name: str
    description: list[str]
    start_date: datetime
    end_date: datetime | None = None


class CompanySchema(pydantic.BaseModel):
    company_name: str
    jobs: list[JobSchema]


class EducationSchema(pydantic.BaseModel):
    institution_name: str
    field_of_study: str
    degree: str
    start_date: datetime
    end_date: datetime | None = None


class CertificateSchema(pydantic.BaseModel):
    certificate_name: str
    provider: str
    issue_date: datetime


class ProjectSchema(pydantic.BaseModel):
    project_name: str
    start_date: datetime
    end_date: datetime | None = None


class ResumeSchema(pydantic.BaseModel):
    person: PersonSchema
    experience: list[CompanySchema] | None = None
    education: list[EducationSchema] | None = None
    certification: list[CertificateSchema] | None = None
    projects: list[ProjectSchema] | None = None
