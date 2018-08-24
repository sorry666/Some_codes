
// EXCEL-TESTDlg.h : ͷ�ļ�
//

#pragma once
#include "CApplication.h"
#include "CRange.h"
#include "CWorkbooks.h"
#include "CWorkbook.h"
#include "CWorksheets.h"
#include "CWorksheet.h"

class CEXCELTESTDlgAutoProxy;


// CEXCELTESTDlg �Ի���
class CEXCELTESTDlg : public CDialogEx
{
	DECLARE_DYNAMIC(CEXCELTESTDlg);
	friend class CEXCELTESTDlgAutoProxy;

// ����
public:
	CEXCELTESTDlg(CWnd* pParent = NULL);	// ��׼���캯��
	virtual ~CEXCELTESTDlg();

// �Ի�������
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_EXCELTEST_DIALOG };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV ֧��


// ʵ��
protected:
	CEXCELTESTDlgAutoProxy* m_pAutoProxy;
	HICON m_hIcon;

	BOOL CanExit();

	// ���ɵ���Ϣӳ�亯��
	virtual BOOL OnInitDialog();
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnClose();
	virtual void OnOK();
	virtual void OnCancel();
	DECLARE_MESSAGE_MAP()
public:
	CApplication m_app;
	long m_rRow;
	long m_rCol;
	CString m_rRes;
	long m_wRow;
	long m_wCol;
	CString m_wRes;
	CString m_fileName;
	CString m_pathName;
	afx_msg void OnBnClickedBtnRead();
	afx_msg void OnBnClickedBtnWrte();
	afx_msg void OnBnClickedBtnOpen();
	afx_msg void OnBnClickedBtnSave();
	afx_msg void OnDestroy();
};
