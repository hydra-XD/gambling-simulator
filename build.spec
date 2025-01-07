block_cipher = None
a = Analysis(['build/main.min.py'],
             pathex=[],
             binaries=[],
             datas=[('source/README.md', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[])
pyz = PYZ(a.pure, a.zipped, cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          name='gambling_simulator_v1_11',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Gambling Simulator v1.11')
