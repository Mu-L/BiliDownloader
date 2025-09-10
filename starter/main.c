#include <Windows.h>
#include <WinBase.h>
#include <tchar.h>
#include <stdlib.h>

#define bool  int
#define false 0
#define true  1

bool SetCurrentDirectoryToExeDir() {
    TCHAR szCurrentDir[MAX_PATH];
    TCHAR szModulePath[MAX_PATH];
    TCHAR szModuleDir[MAX_PATH];
    DWORD dwResult;

    // ��ȡ��ǰ����Ŀ¼
    dwResult = GetCurrentDirectory(MAX_PATH, szCurrentDir);
    if (dwResult == 0 || dwResult >= MAX_PATH) {
        return false; // ��ȡʧ��
    }

    // ��ȡ�����ִ���ļ�������·��
    dwResult = GetModuleFileName(NULL, szModulePath, MAX_PATH);
    if (dwResult == 0 || dwResult >= MAX_PATH) {
        return false; // ��ȡʧ��
    }

    // ������·������ȡĿ¼����
    TCHAR* pLastSlash = _tcsrchr(szModulePath, _T('\\'));
    if (pLastSlash == NULL) {
        // �����Ŀ¼��������� C:
        TCHAR* pColon = _tcschr(szModulePath, _T(':'));
        if (pColon != NULL && *(pColon + 1) == _T('\0')) {
            _tcscpy(szModuleDir, szModulePath);
            _tcscat(szModuleDir, _T("\\"));
        } else {
            return false; // �޷�����·��
        }
    } else {
        size_t dirLength = (pLastSlash - szModulePath) + 1;
        if (dirLength >= MAX_PATH) {
            return false; // ·������
        }
        _tcsncpy(szModuleDir, szModulePath, dirLength);
        szModuleDir[dirLength] = _T('\0');
    }

    // �Ƚϵ�ǰĿ¼�ͳ�������Ŀ¼�������ִ�Сд��
    if (_tcsicmp(szCurrentDir, szModuleDir) == 0) {
        return true; // Ŀ¼����ȷ���������
    }

    // ���Ը���Ŀ¼
    if (SetCurrentDirectory(szModuleDir)) {
        return true; // ���ĳɹ�
    }

    // ����ʧ��
    return false;
}

int WINAPI WinMain(
    HINSTANCE hInstance,
    HINSTANCE hPrevInstance,
    LPSTR lpCmdLine,
    int nShowCmd
)
{
    SetCurrentDirectoryToExeDir();
    SHELLEXECUTEINFO sei = { sizeof(SHELLEXECUTEINFO) };
    sei.lpVerb = TEXT("runas");
    sei.lpFile = TEXT(".\\bin\\BiliDownloader.exe");
    sei.nShow = SW_SHOWNORMAL;
    ShellExecuteEx(&sei);
    return 0;
}
