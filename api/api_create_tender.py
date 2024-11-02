# from dao.dao_create_tender import TenderDAO
# #from dto.model_tender import TenderDTO

# class TenderAPI:
#     @staticmethod
#     def create_tender(data):
#         return TenderDAO.create_tender(data)

#     @staticmethod
#     def get_tender(tender_id):
#         tender = TenderDAO.get_tender(tender_id)
#         if not tender:
#             raise ValueError("Tender not found")
#         return tender

#     @staticmethod
#     def get_all_tenders():
#         return TenderDAO.get_all_tenders()

#     @staticmethod
#     def update_tender(tender_id, data):
#         if TenderDAO.update_tender(tender_id, data) == 0:
#             raise ValueError("Tender not found or no changes applied")
#         return "Tender updated successfully"

#     @staticmethod
#     def delete_tender(tender_id):
#         if TenderDAO.delete_tender(tender_id) == 0:
#             raise ValueError("Tender not found")
#         return "Tender deleted successfully"
