

/* this ALWAYS GENERATED file contains the definitions for the interfaces */


 /* File created by MIDL compiler version 8.00.0603 */
/* at Fri Apr 27 10:09:29 2018
 */
/* Compiler settings for EXCELTEST.idl:
    Oicf, W1, Zp8, env=Win32 (32b run), target_arch=X86 8.00.0603 
    protocol : dce , ms_ext, c_ext, robust
    error checks: allocation ref bounds_check enum stub_data 
    VC __declspec() decoration level: 
         __declspec(uuid()), __declspec(selectany), __declspec(novtable)
         DECLSPEC_UUID(), MIDL_INTERFACE()
*/
/* @@MIDL_FILE_HEADING(  ) */

#pragma warning( disable: 4049 )  /* more than 64k source lines */


/* verify that the <rpcndr.h> version is high enough to compile this file*/
#ifndef __REQUIRED_RPCNDR_H_VERSION__
#define __REQUIRED_RPCNDR_H_VERSION__ 475
#endif

#include "rpc.h"
#include "rpcndr.h"

#ifndef __RPCNDR_H_VERSION__
#error this stub requires an updated version of <rpcndr.h>
#endif // __RPCNDR_H_VERSION__


#ifndef __EXCELTEST_h_h__
#define __EXCELTEST_h_h__

#if defined(_MSC_VER) && (_MSC_VER >= 1020)
#pragma once
#endif

/* Forward Declarations */ 

#ifndef __IEXCELTEST_FWD_DEFINED__
#define __IEXCELTEST_FWD_DEFINED__
typedef interface IEXCELTEST IEXCELTEST;

#endif 	/* __IEXCELTEST_FWD_DEFINED__ */


#ifndef __EXCELTEST_FWD_DEFINED__
#define __EXCELTEST_FWD_DEFINED__

#ifdef __cplusplus
typedef class EXCELTEST EXCELTEST;
#else
typedef struct EXCELTEST EXCELTEST;
#endif /* __cplusplus */

#endif 	/* __EXCELTEST_FWD_DEFINED__ */


#ifdef __cplusplus
extern "C"{
#endif 



#ifndef __EXCELTEST_LIBRARY_DEFINED__
#define __EXCELTEST_LIBRARY_DEFINED__

/* library EXCELTEST */
/* [version][uuid] */ 


EXTERN_C const IID LIBID_EXCELTEST;

#ifndef __IEXCELTEST_DISPINTERFACE_DEFINED__
#define __IEXCELTEST_DISPINTERFACE_DEFINED__

/* dispinterface IEXCELTEST */
/* [uuid] */ 


EXTERN_C const IID DIID_IEXCELTEST;

#if defined(__cplusplus) && !defined(CINTERFACE)

    MIDL_INTERFACE("55F8E529-8DE2-41A1-8CE3-191E7C84C609")
    IEXCELTEST : public IDispatch
    {
    };
    
#else 	/* C style interface */

    typedef struct IEXCELTESTVtbl
    {
        BEGIN_INTERFACE
        
        HRESULT ( STDMETHODCALLTYPE *QueryInterface )( 
            IEXCELTEST * This,
            /* [in] */ REFIID riid,
            /* [annotation][iid_is][out] */ 
            _COM_Outptr_  void **ppvObject);
        
        ULONG ( STDMETHODCALLTYPE *AddRef )( 
            IEXCELTEST * This);
        
        ULONG ( STDMETHODCALLTYPE *Release )( 
            IEXCELTEST * This);
        
        HRESULT ( STDMETHODCALLTYPE *GetTypeInfoCount )( 
            IEXCELTEST * This,
            /* [out] */ UINT *pctinfo);
        
        HRESULT ( STDMETHODCALLTYPE *GetTypeInfo )( 
            IEXCELTEST * This,
            /* [in] */ UINT iTInfo,
            /* [in] */ LCID lcid,
            /* [out] */ ITypeInfo **ppTInfo);
        
        HRESULT ( STDMETHODCALLTYPE *GetIDsOfNames )( 
            IEXCELTEST * This,
            /* [in] */ REFIID riid,
            /* [size_is][in] */ LPOLESTR *rgszNames,
            /* [range][in] */ UINT cNames,
            /* [in] */ LCID lcid,
            /* [size_is][out] */ DISPID *rgDispId);
        
        /* [local] */ HRESULT ( STDMETHODCALLTYPE *Invoke )( 
            IEXCELTEST * This,
            /* [annotation][in] */ 
            _In_  DISPID dispIdMember,
            /* [annotation][in] */ 
            _In_  REFIID riid,
            /* [annotation][in] */ 
            _In_  LCID lcid,
            /* [annotation][in] */ 
            _In_  WORD wFlags,
            /* [annotation][out][in] */ 
            _In_  DISPPARAMS *pDispParams,
            /* [annotation][out] */ 
            _Out_opt_  VARIANT *pVarResult,
            /* [annotation][out] */ 
            _Out_opt_  EXCEPINFO *pExcepInfo,
            /* [annotation][out] */ 
            _Out_opt_  UINT *puArgErr);
        
        END_INTERFACE
    } IEXCELTESTVtbl;

    interface IEXCELTEST
    {
        CONST_VTBL struct IEXCELTESTVtbl *lpVtbl;
    };

    

#ifdef COBJMACROS


#define IEXCELTEST_QueryInterface(This,riid,ppvObject)	\
    ( (This)->lpVtbl -> QueryInterface(This,riid,ppvObject) ) 

#define IEXCELTEST_AddRef(This)	\
    ( (This)->lpVtbl -> AddRef(This) ) 

#define IEXCELTEST_Release(This)	\
    ( (This)->lpVtbl -> Release(This) ) 


#define IEXCELTEST_GetTypeInfoCount(This,pctinfo)	\
    ( (This)->lpVtbl -> GetTypeInfoCount(This,pctinfo) ) 

#define IEXCELTEST_GetTypeInfo(This,iTInfo,lcid,ppTInfo)	\
    ( (This)->lpVtbl -> GetTypeInfo(This,iTInfo,lcid,ppTInfo) ) 

#define IEXCELTEST_GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId)	\
    ( (This)->lpVtbl -> GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId) ) 

#define IEXCELTEST_Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr)	\
    ( (This)->lpVtbl -> Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr) ) 

#endif /* COBJMACROS */


#endif 	/* C style interface */


#endif 	/* __IEXCELTEST_DISPINTERFACE_DEFINED__ */


EXTERN_C const CLSID CLSID_EXCELTEST;

#ifdef __cplusplus

class DECLSPEC_UUID("A9E9DAED-42BA-4C05-89D5-08ED9407F763")
EXCELTEST;
#endif
#endif /* __EXCELTEST_LIBRARY_DEFINED__ */

/* Additional Prototypes for ALL interfaces */

/* end of Additional Prototypes */

#ifdef __cplusplus
}
#endif

#endif


