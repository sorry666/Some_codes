
// DlgProxy.cpp : ʵ���ļ�
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
	
	// ΪʹӦ�ó������Զ��������ڻ״̬ʱһֱ���� 
	//	���У����캯������ AfxOleLockApp��
	AfxOleLockApp();

	// ͨ��Ӧ�ó����������ָ��
	//  �����ʶԻ���  ���ô�����ڲ�ָ��
	//  ָ��Ի��򣬲����öԻ���ĺ���ָ��ָ��
	//  �ô���
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
	// Ϊ������ OLE �Զ����������ж������ֹӦ�ó���
	//	������������ AfxOleUnlockApp��
	//  ���������������⣬�⻹���������Ի���
	if (m_pDialog != NULL)
		m_pDialog->m_pAutoProxy = NULL;
	AfxOleUnlockApp();
}

void CEXCELTESTDlgAutoProxy::OnFinalRelease()
{
	// �ͷ��˶��Զ�����������һ�����ú󣬽�����
	// OnFinalRelease��  ���ཫ�Զ�
	// ɾ���ö���  �ڵ��øû���֮ǰ�����������
	// ��������ĸ���������롣

	CCmdTarget::OnFinalRelease();
}

BEGIN_MESSAGE_MAP(CEXCELTESTDlgAutoProxy, CCmdTarget)
END_MESSAGE_MAP()

BEGIN_DISPATCH_MAP(CEXCELTESTDlgAutoProxy, CCmdTarget)
END_DISPATCH_MAP()

// ע��: ��������˶� IID_IEXCELTEST ��֧��
//  ��֧������ VBA �����Ͱ�ȫ�󶨡�  �� IID ����ͬ���ӵ� .IDL �ļ��е�
//  ���Ƚӿڵ� GUID ƥ�䡣

// {55F8E529-8DE2-41A1-8CE3-191E7C84C609}
static const IID IID_IEXCELTEST =
{ 0x55F8E529, 0x8DE2, 0x41A1, { 0x8C, 0xE3, 0x19, 0x1E, 0x7C, 0x84, 0xC6, 0x9 } };

BEGIN_INTERFACE_MAP(CEXCELTESTDlgAutoProxy, CCmdTarget)
	INTERFACE_PART(CEXCELTESTDlgAutoProxy, IID_IEXCELTEST, Dispatch)
END_INTERFACE_MAP()

// IMPLEMENT_OLECREATE2 ���ڴ���Ŀ�� StdAfx.h �ж���
// {A9E9DAED-42BA-4C05-89D5-08ED9407F763}
IMPLEMENT_OLECREATE2(CEXCELTESTDlgAutoProxy, "EXCELTEST.Application", 0xa9e9daed, 0x42ba, 0x4c05, 0x89, 0xd5, 0x8, 0xed, 0x94, 0x7, 0xf7, 0x63)


// CEXCELTESTDlgAutoProxy ��Ϣ�������
