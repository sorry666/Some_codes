
// EXCEL-TESTDlg.cpp : ʵ���ļ�
//

#include "stdafx.h"
#include "EXCEL-TEST.h"
#include "EXCEL-TESTDlg.h"
#include "DlgProxy.h"
#include "afxdialogex.h"




#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CEXCELTESTDlg �Ի���


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
	// ����öԻ������Զ���������
	//  ���˴���ָ��öԻ���ĺ���ָ������Ϊ NULL���Ա�
	//  �˴���֪���öԻ����ѱ�ɾ����
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


// CEXCELTESTDlg ��Ϣ�������

BOOL CEXCELTESTDlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// ���ô˶Ի����ͼ�ꡣ  ��Ӧ�ó��������ڲ��ǶԻ���ʱ����ܽ��Զ�
	//  ִ�д˲���
	SetIcon(m_hIcon, TRUE);			// ���ô�ͼ��
	SetIcon(m_hIcon, FALSE);		// ����Сͼ��

	// TODO: �ڴ���Ӷ���ĳ�ʼ������

	//��excel������
	if (!m_app.CreateDispatch(L"Excel.Application"))
	{
		AfxMessageBox(L"�޷�����Excel������!");
		return FALSE;
	}

	return TRUE;  // ���ǽ��������õ��ؼ������򷵻� TRUE
}

// �����Ի��������С����ť������Ҫ����Ĵ���
//  �����Ƹ�ͼ�ꡣ  ����ʹ���ĵ�/��ͼģ�͵� MFC Ӧ�ó���
//  �⽫�ɿ���Զ���ɡ�

void CEXCELTESTDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // ���ڻ��Ƶ��豸������

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// ʹͼ���ڹ����������о���
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// ����ͼ��
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

//���û��϶���С������ʱϵͳ���ô˺���ȡ�ù��
//��ʾ��
HCURSOR CEXCELTESTDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

// ���û��ر� UI ʱ������������Ա���������ĳ��
//  �������Զ�����������Ӧ�˳���  ��Щ
//  ��Ϣ�������ȷ����������: �����������ʹ�ã�
//  ������ UI�������ڹرնԻ���ʱ��
//  �Ի�����Ȼ�ᱣ�������

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
	// �����������Ա�����������Զ���
	//  �������Իᱣ�ִ�Ӧ�ó���
	//  ʹ�Ի���������������� UI ����������
	if (m_pAutoProxy != NULL)
	{
		ShowWindow(SW_HIDE);
		return FALSE;
	}

	return TRUE;
}


//��ȡexcel
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

	//�򿪹�����
	books = m_app.get_Workbooks();
	book = books.Open(m_fileName, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional, covOptional);

	//��ȡ������
	sheet = book.get_ActiveSheet();

	//��ȡ��Ԫ��
	range = sheet.get_Cells(); //��ȡ���е�,�������ʡ
	range = range.get_Item(_variant_t(m_rRow), _variant_t(m_rCol)).pdispVal; //�ٻ�ȡָ����

	//��ȡ��Ԫ������
	vResult = range.get_Value2();
	if (vResult.vt == VT_R8) //8�ֽڵ�����
		m_rRes.Format(TEXT("%lf"), vResult.dblVal);
	else if (vResult.vt == VT_BSTR) //�ַ���
		m_rRes = vResult.bstrVal;
	UpdateData(FALSE);

	//�رչ�����
	books.Close();

	//�ͷŶ���
	range.ReleaseDispatch();
	sheet.ReleaseDispatch();
	sheets.ReleaseDispatch();
	book.ReleaseDispatch();
	books.ReleaseDispatch();
}

//д��excel
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

	//�½�һ��������
	books = m_app.get_Workbooks();
	book = books.Add(covOptional);

	//�½�һ��������
	sheet = book.get_ActiveSheet();

	//��ȡ��Ԫ��
	range = sheet.get_Cells();

	//д������
	range.put_Item(_variant_t(m_wRow), _variant_t(m_wCol),_variant_t(m_wRes));

	//����
	book.SaveCopyAs(_variant_t(m_pathName));
	book.put_Saved(true);
	//����Ǵ����еģ�����ֱ�ӱ���
	//book.Save();

	AfxMessageBox(L"д��ɹ�");

	//�رչ�����
	books.Close();

	//�ͷŶ���
	range.ReleaseDispatch();
	sheet.ReleaseDispatch();
	sheets.ReleaseDispatch();
	book.ReleaseDispatch();
	books.ReleaseDispatch();
	
}

//��excel�ļ�
void CEXCELTESTDlg::OnBnClickedBtnOpen()
{
	CFileDialog dlg(TRUE, 0, 0, 0, L"*.xlsx|*.xlsx|*.xls|*.xls", this);
	if (dlg.DoModal())
	{
		m_fileName = dlg.GetPathName();
	}
}

//���Ϊ
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

	//�˳�excel
	m_app.Quit();
}
