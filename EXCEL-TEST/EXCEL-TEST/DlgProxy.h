
// DlgProxy.h: ͷ�ļ�
//

#pragma once

class CEXCELTESTDlg;


// CEXCELTESTDlgAutoProxy ����Ŀ��

class CEXCELTESTDlgAutoProxy : public CCmdTarget
{
	DECLARE_DYNCREATE(CEXCELTESTDlgAutoProxy)

	CEXCELTESTDlgAutoProxy();           // ��̬������ʹ�õ��ܱ����Ĺ��캯��

// ����
public:
	CEXCELTESTDlg* m_pDialog;

// ����
public:

// ��д
	public:
	virtual void OnFinalRelease();

// ʵ��
protected:
	virtual ~CEXCELTESTDlgAutoProxy();

	// ���ɵ���Ϣӳ�亯��

	DECLARE_MESSAGE_MAP()
	DECLARE_OLECREATE(CEXCELTESTDlgAutoProxy)

	// ���ɵ� OLE ����ӳ�亯��

	DECLARE_DISPATCH_MAP()
	DECLARE_INTERFACE_MAP()
};

