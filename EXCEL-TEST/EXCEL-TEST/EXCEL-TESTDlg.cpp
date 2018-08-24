
// EXCEL-TESTDlg.cpp : 实现文件
//

#include "stdafx.h"
#include "EXCEL-TEST.h"
#include "EXCEL-TESTDlg.h"
#include "DlgProxy.h"
#include "afxdialogex.h"




#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CEXCELTESTDlg 对话框


IMPLEMENT_DYNAMIC(CEXCELTESTDlg, CDialogEx);

CEXCELTESTDlg::CEXCELTESTDlg(CWnd* pParent /*=NULL*/)
	: CDialogEx(IDD_EXCELTEST_DIALOG, pParent)
	, m_rRow(0)
	, m_rCol(0)
	, m_rRes(_T(""))
	, m_wRow(0)
	, m_wCol(0)
	, m_wRes(_T(""))
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
	m_pAutoProxy = NULL;
}

CEXCELTESTDlg::~CEXCELTESTDlg()
{
	// 如果该对话框有自动化代理，则
	//  将此代理指向该对话框的后向指针设置为 NULL，以便
	//  此代理知道该对话框已被删除。
	if (m_pAutoProxy != NULL)
		m_pAutoProxy->m_pDialog = NULL;
}

void CEXCELTESTDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
	DDX_Text(pDX, IDC_EDIT_ROW, m_rRow);
	DDX_Text(pDX, IDC_EDIT_COL, m_rCol);
	DDX_Text(pDX, IDC_EDIT_RES, m_rRes);
	DDX_Text(pDX, IDC_EDIT_ROW2, m_wRow);
	DDX_Text(pDX, IDC_EDIT_COL2, m_wCol);
	DDX_Text(pDX, IDC_EDIT_RES2, m_wRes);
}

BEGIN_MESSAGE_MAP(CEXCELTESTDlg, CDialogEx)
	ON_WM_CLOSE()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_BTN_READ, &CEXCELTESTDlg::OnBnClickedBtnRead)
	ON_BN_CLICKED(IDC_BTN_WRTE, &CEXCELTESTDlg::OnBnClickedBtnWrte)
	ON_BN_CLICKED(IDC_BTN_OPEN, &CEXCELTESTDlg::OnBnClickedBtnOpen)
	ON_BN_CLICKED(IDC_BTN_SAVE, &CEXCELTESTDlg::OnBnClickedBtnSave)
	ON_WM_DESTROY()
END_MESSAGE_MAP()


// CEXCELTESTDlg 消息处理程序

BOOL CEXCELTESTDlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// 设置此对话框的图标。  当应用程序主窗口不是对话框时，框架将自动
	//  执行此操作
	SetIcon(m_hIcon, TRUE);			// 设置大图标
	SetIcon(m_hIcon, FALSE);		// 设置小图标

	// TODO: 在此添加额外的初始化代码

	//打开excel服务器
	if (!m_app.CreateDispatch(L"Excel.Application"))
	{
		AfxMessageBox(L"无法启动Excel服务器!");
		return FALSE;
	}

	return TRUE;  // 除非将焦点设置到控件，否则返回 TRUE
}

// 如果向对话框添加最小化按钮，则需要下面的代码
//  来绘制该图标。  对于使用文档/视图模型的 MFC 应用程序，
//  这将由框架自动完成。

void CEXCELTESTDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // 用于绘制的设备上下文

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// 使图标在工作区矩形中居中
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// 绘制图标
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

//当用户拖动最小化窗口时系统调用此函数取得光标
//显示。
HCURSOR CEXCELTESTDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

// 当用户关闭 UI 时，如果控制器仍保持着它的某个
//  对象，则自动化服务器不应退出。  这些
//  消息处理程序确保如下情形: 如果代理仍在使用，
//  则将隐藏 UI；但是在关闭对话框时，
//  对话框仍然会保留在那里。

void CEXCELTESTDlg::OnClose()
{
	if (CanExit())
		CDialogEx::OnClose();
}

void CEXCELTESTDlg::OnOK()
{
	if (CanExit())
		CDialogEx::OnOK();
}

void CEXCELTESTDlg::OnCancel()
{
	if (CanExit())
		CDialogEx::OnCancel();
}

BOOL CEXCELTESTDlg::CanExit()
{
	// 如果代理对象仍保留在那里，则自动化
	//  控制器仍会保持此应用程序。
	//  使对话框保留在那里，但将其 UI 隐藏起来。
	if (m_pAutoProxy != NULL)
	{
		ShowWindow(SW_HIDE);
		return FALSE;
	}

	return TRUE;
}


//读取excel
void CEXCELTESTDlg::OnBnClickedBtnRead()
{
	UpdateData(TRUE);
	m_rRes.Empty();
	CWorkbooks books;
	CWorkbook book;
	CWorksheets sheets;
	CWorksheet sheet;
	CRange range;
	COleVariant vResult;
	COleVariant covOptional((long)DISP_E_PARAMNOTFOUND, VT_ERROR);

	//打开工作簿
	books = m_app.get_Workbooks();
	book = books.Open(m_fileName, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional);

	//获取工作表
	sheet = book.get_ActiveSheet();

	//获取单元格
	range = sheet.get_Cells(); //获取所有的,这个不能省
	range = range.get_Item(_variant_t(m_rRow), _variant_t(m_rCol)).pdispVal; //再获取指定的

	//获取单元格内容
	vResult = range.get_Value2();
	if (vResult.vt == VT_R8) //8字节的数字
		m_rRes.Format(TEXT("%lf"), vResult.dblVal);
	else if (vResult.vt == VT_BSTR) //字符串
		m_rRes = vResult.bstrVal;
	UpdateData(FALSE);

	//关闭工作簿
	books.Close();

	//释放对象
	range.ReleaseDispatch();
	sheet.ReleaseDispatch();
	sheets.ReleaseDispatch();
	book.ReleaseDispatch();
	books.ReleaseDispatch();
}

//写入excel
void CEXCELTESTDlg::OnBnClickedBtnWrte()
{
	UpdateData(TRUE);
	CWorkbooks books;
	CWorkbook book;
	CWorksheets sheets;
	CWorksheet sheet;
	CRange range;
	COleVariant vResult;
	COleVariant covOptional((long)DISP_E_PARAMNOTFOUND, VT_ERROR);

	//新建一个工作簿
	books = m_app.get_Workbooks();
	book = books.Add(covOptional);

	//新建一个工作表
	sheet = book.get_ActiveSheet();

	//获取单元格
	range = sheet.get_Cells();

	//写入内容
	range.put_Item(_variant_t(m_wRow), _variant_t(m_wCol),_variant_t(m_wRes));

	//保存
	book.SaveCopyAs(_variant_t(m_pathName));
	book.put_Saved(true);
	//如果是打开已有的，可以直接保存
	//book.Save();

	AfxMessageBox(L"写入成功");

	//关闭工作簿
	books.Close();

	//释放对象
	range.ReleaseDispatch();
	sheet.ReleaseDispatch();
	sheets.ReleaseDispatch();
	book.ReleaseDispatch();
	books.ReleaseDispatch();
	
}

//打开excel文件
void CEXCELTESTDlg::OnBnClickedBtnOpen()
{
	CFileDialog dlg(TRUE, 0, 0, 0, L"*.xlsx|*.xlsx|*.xls|*.xls", this);
	if (dlg.DoModal())
	{
		m_fileName = dlg.GetPathName();
	}
}

//另存为
void CEXCELTESTDlg::OnBnClickedBtnSave()
{
	CFileDialog dlg(FALSE, 0, 0, 0, L"*.xlsx|*.xlsx|*.xls|*.xls", this);
	if (dlg.DoModal())
	{
		m_pathName = dlg.GetPathName();
	}
}


void CEXCELTESTDlg::OnDestroy()
{
	CDialogEx::OnDestroy();

	m_app.ReleaseDispatch();

	//退出excel
	m_app.Quit();
}
