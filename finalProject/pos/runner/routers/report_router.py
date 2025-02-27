from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.requests import Request
from pydantic import BaseModel

from pos.core.models.report import Report
from pos.core.models.sales import Sales
from pos.core.services.report_service import ReportService
from pos.core.services.sales_service import SalesService
from pos.runner.routers.infra import _Infra

sales_router = APIRouter()
report_router = APIRouter()

def create_sales_service(request: Request) -> SalesService:
    infra: _Infra = request.app.state.infra
    return SalesService(
        infra.sales_repo()
    )

def create_report_service(request: Request) -> ReportService:
    infra: _Infra = request.app.state.infra
    return ReportService(
        infra.report_repo()
    )



class SalesResponse(BaseModel):
    sales: Sales

class ReportResponse(BaseModel):
    report: Report

@sales_router.get("", status_code=200, response_model=SalesResponse)
def get_sales(service: SalesService = Depends(create_sales_service)) -> SalesResponse:
    sales: SalesResponse = SalesResponse(sales=service.get_sales())
    return sales

@report_router.get("", status_code=200, response_model=ReportResponse)
def get_report(shift_id: str = Query(..., description="The ID of the shift"), service: ReportService = Depends(create_report_service)) -> ReportResponse:
    try:
        report: ReportResponse = ReportResponse(report=service.get_report(shift_id))
        return report
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))