from tkinter import *
from tkinter.constants import *
import ArticlePage
import ListPage
import WorkEntry
import AdminPage
import ReportsPage
import AllotWorkPage
import WorkEntrySection
import TodaysWorkPage
import NewParty
import NewGroup
import WorkDiaryPage
import RegistrationPage


# def switchFrame(emptyframe,root):
#     emptyframe.tkraise()
#     root.tkraise()
#     return

# def switchAdminFrame(root):
#     root.tkraise()
#     return

def recreateArticlePage(currentframe,root):
    currentframe.destroy()
    ArticlePage.article(root)
    return

def recreateAdminPage(currentframe,root):
    currentframe.destroy()
    AdminPage.admin(root)
    return


def recreateListPage(currentframe,root,buttonframe):
    currentframe.destroy()
    buttonframe.destroy()
    ListPage.workList(root)
    return


def recreateWorkEntry(currentframe,root,buttonframe):
    currentframe.destroy()
    buttonframe.destroy()
    WorkEntry.enterWork(root)
    return

    
def recreateReportsPage(currentframe,root,buttonframe):
    currentframe.destroy()
    buttonframe.destroy()
    ReportsPage.reportList(root)
    
    return


def recreateAllotWorkPage(currentframe,root,buttonframe):
    currentframe.destroy()
    buttonframe.destroy()
    AllotWorkPage.allotWorkList(root)
    
    return

def recreateWorkEntrySection(currentframe,root,buttonframe):
    currentframe.destroy()
    buttonframe.destroy()
    WorkEntrySection.enterWorkIn(root)
    
    return

def recreateTodaysWorkPage(currentframe,root,buttonframe):
    currentframe.destroy()
    buttonframe.destroy()
    TodaysWorkPage.todaysWorkList(root)
    
    return

def recreateNewGroup(currentframe,root,buttonframe):
    currentframe.destroy()
    buttonframe.destroy()
    NewGroup.newGroup(root)
    
    return

def recreateNewParty(currentframe,root,buttonframe):
    currentframe.destroy()
    buttonframe.destroy()
    NewParty.newParty(root)
    
    return


def recreateWorkDiaryPage(currentframe,root,buttonframe):
    currentframe.destroy()
    buttonframe.destroy()
    WorkDiaryPage.workDiaryList(root)
    
    return


def recreateRegistrationPage(currentframe,root,buttonframe):
    currentframe.destroy()
    buttonframe.destroy()
    RegistrationPage.registeruser(root)
    
    return