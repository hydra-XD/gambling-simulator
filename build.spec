block_cipher = None

DISTPATH = os.path.join('build')  # Specify your custom dist folder
WORKPATH = os.path.join('build')  # Specify your custom build folder

a = Analysis(['build/main.min.py'],
             pathex=[],
             binaries=[],
             datas=[('', '.', 'source/README.md')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[])
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          name='gambling_simulator_v1_12',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          onefile=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Gambling Simulator v1.12')

coll.distpath = DISTPATH
coll.workpath = WORKPATH