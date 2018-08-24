
// DlgProxy.cpp : 实现文件
//

#include "stdafx.h"
#include "EXCEL-TEST.h"
#include "DlgProxy.h"
#include "EXCEL-TESTDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CEXCELTESTDlgAutoProxy

IMPLEMENT_DYNCREATE(CEXCELTESTDlgAutoProxy, CCmdTarget)

CEXCELTESTDlgAutoProxy::CEXCELTESTDlgAutoProxy()
{
	EnableAutomation();
	
	// 为使应用程序在自动化对象处于活动状态时一直保持 
	//	运行，构造函数调用 AfxOleLockApp。
	AfxOleLockApp();

	// 通过应用程序的主窗口指针
	//  来访问对话框。  设置代理的内部指针
	//  指向对话框，并设置对话框的后向指针指向
	//  该代理。
	ASSERT_VALID(AfxGetApp()->m_pMainWnd);
	if (AfxGetApp()->m_pMainWnd)
	{
		ASSERT_KINDOF(CEXCELTESTDlg, AfxGetApp()->m_pMainWnd);
		if (AfxGetApp()->m_pMainWnd->IsKindOf(RUNTIME_CLASS(CEXCELTESTDlg)))
		{
			m_pDialog = reinterpret_cast<CEXCELTESTDlg*>(AfxGetApp()->m_pMainWnd);
			m_pDialog->m_pAutoProxy = this;
		}
	}
}

CEXCELTESTDlgAutoProxy::~CEXCELTESTDlgAutoProxy()
{
	// 为了在用 OLE 自动化创建所有对象后终止应用程序，
	//	析构函数调用 AfxOleUnlockApp。
	//  除了做其他事情外，这还将销毁主对话框
	if (m_pDialog != NULL)
		m_pDialog->m_pAutoProxy = NULL;
	AfxOleUnlockApp();
}

void CEXCELTESTDlgAutoProxy::OnFinalRelease()
{
	// 释放了对自动化对象的最后一个引用后，将调用
	// OnFinalRelease。  基类将自动
	// 删除该对象。  在调用该基类之前，请添加您的
	// 对象所需的附加清理代码。

	CCmdTarget::OnFinalRelease();
}

BEGIN_MESSAGE_MAP(CEXCELTESTDlgAutoProxy, CCmdTarget)
END_MESSAGE_MAP()

BEGIN_DISPATCH_MAP(CEXCELTESTDlgAutoProxy, CCmdTarget)
END_DISPATCH_MAP()

// 注意: 我们添加了对 IID_IEXCELTEST 的支持
//  以支持来自 VBA 的类型安全绑定。  此 IID 必须同附加到 .IDL 文件中的
//  调度接口的 GUID 匹配。

// {55F8E529-8DE2-41A1-8CE3-191E7C84C609}
static const IID IID_IEXCELTEST =
{ 0x55F8E529, 0x8DE2, 0x41A1, { 0x8C, 0xE3, 0x19, 0x1E, 0x7C, 0x84, 0xC6, 0x9 } };

BEGIN_INTERFACE_MAP(CEXCELTESTDlgAutoProxy, CCmdTarget)
	INTERFACE_PART(CEXCELTESTDlgAutoProxy, IID_IEXCELTEST, Dispatch)
END_INTERFACE_MAP()

// IMPLEMENT_OLECREATE2 宏在此项目的 StdAfx.h 中定义
// {A9E9DAED-42BA-4C05-89D5-08ED9407F763}
IMPLEMENT_OLECREATE2(CEXCELTESTDlgAutoProxy, "EXCELTEST.Application", 0xa9e9daed, 0x42ba, 0x4c05, 0x89, 0xd5, 0x8, 0xed, 0x94, 0x7, 0xf7, 0x63)


// CEXCELTESTDlgAutoProxy 消息处理程序
