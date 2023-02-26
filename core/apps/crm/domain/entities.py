from enum import Enum


class LeadStatus(str, Enum):
    NEW = "new"
    CONTACTED = "contacted"
    IN_PROGRESS = "inprogress"
    LOST = "lost"
    WON = "won"
