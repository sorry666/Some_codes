
// EXCEL-TEST.h : PROJECT_NAME Ӧ�ó������ͷ�ļ�
//

#pragma once

#ifndef __AFXWIN_H__
	#error "�ڰ������ļ�֮ǰ������stdafx.h�������� PCH �ļ�"
#endif

#include "resource.h"		// ������


// CEXCELTESTApp: 
// �йش����ʵ�֣������ EXCEL-TEST.cpp
//

class CEXCELTESTApp : public CWinApp
{
public:
	CEXCELTESTApp();

// ��д
public:
	virtual BOOL InitInstance();
	virtual int ExitInstance();

// ʵ��

	DECLARE_MESSAGE_MAP()
};

extern CEXCELTESTApp theApp;