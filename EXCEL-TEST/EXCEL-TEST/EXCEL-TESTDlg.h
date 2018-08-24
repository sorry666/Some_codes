
// EXCEL-TESTDlg.h : 头文件
//

#pragma once
#include "CApplication.h"
#include "CRange.h"
#include "CWorkbooks.h"
#include "CWorkbook.h"
#include "CWorksheets.h"
#include "CWorksheet.h"

class CEXCELTESTDlgAutoProxy;


// CEXCELTESTDlg 对话框
class CEXCELTESTDlg : public CDialogEx
{
	DECLARE_DYNAMIC(CEXCELTESTDlg);
	friend class CEXCELTESTDlgAutoProxy;

// 构造
public:
	CEXCELTESTDlg(CWnd* pParent = NULL);	// 标准构造函数
	virtual ~CEXCELTESTDlg();

// 对话框数据
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_EXCELTEST_DIALOG };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV 支持


// 实现
protected:
	CEXCELTESTDlgAutoProxy* m_pAutoProxy;
	HICON m_hIcon;

	BOOL CanExit();

	// 生成的消息映射函数
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
