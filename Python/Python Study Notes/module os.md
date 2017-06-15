

# module os  



## help(os)

```
Help on module os:

NAME
    os - OS routines for NT or Posix depending on what system we're on.

MODULE REFERENCE
    http://docs.python.org/3.4/library/os
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This exports:
      - all functions from posix, nt or ce, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix', 'nt' or 'ce'.
      - os.curdir is a string representing the current directory ('.' or ':')
      - os.pardir is a string representing the parent directory ('..' or '::')
      - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)
    
    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).

FUNCTIONS
    _exit(...)
        _exit(status)
        
        Exit to the system with specified status, without normal exit processing.
    
    execl(file, *args)
        execl(file, *args)
        
        Execute the executable file with argument list args, replacing the
        current process.
    
    execle(file, *args)
        execle(file, *args, env)
        
        Execute the executable file with argument list args and
        environment env, replacing the current process.
    
    execlp(file, *args)
        execlp(file, *args)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args, replacing the current process.
    
    execlpe(file, *args)
        execlpe(file, *args, env)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args and environment env, replacing the current
        process.
    
    execvp(file, args)
        execvp(file, args)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args, replacing the current process.
        args may be a list or tuple of strings.
    
    execvpe(file, args, env)
        execvpe(file, args, env)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args and environment env , replacing the
        current process.
        args may be a list or tuple of strings.
    
    fdopen(fd, *args, **kwargs)
        # Supply os.fdopen()
    
    fsdecode(filename)
        Decode filename from the filesystem encoding with 'surrogateescape' error
        handler, return str unchanged. On Windows, use 'strict' error handler if
        the file system encoding is 'mbcs' (which is the default encoding).
    
    fsencode(filename)
        Encode filename to the filesystem encoding with 'surrogateescape' error
        handler, return bytes unchanged. On Windows, use 'strict' error handler if
        the file system encoding is 'mbcs' (which is the default encoding).
    
    get_exec_path(env=None)
        Returns the sequence of directories that will be searched for the
        named executable (similar to a shell) when launching a process.
        
        *env* must be an environment variable dict or None.  If *env* is None,
        os.environ will be used.
    
    getenv(key, default=None)
        Get an environment variable, return None if it doesn't exist.
        The optional second argument can specify an alternate default.
        key, default and the result are str.
    
    getenvb(key, default=None)
        Get an environment variable, return None if it doesn't exist.
        The optional second argument can specify an alternate default.
        key, default and the result are bytes.
    
    makedirs(name, mode=511, exist_ok=False)
        makedirs(name [, mode=0o777][, exist_ok=False])
        
        Super-mkdir; create a leaf directory and all intermediate ones.  Works like
        mkdir, except that any intermediate path segment (not just the rightmost)
        will be created if it does not exist. If the target directory already
        exists, raise an OSError if exist_ok is False. Otherwise no exception is
        raised.  This is recursive.
    
    popen(cmd, mode='r', buffering=-1)
        # Supply os.popen()
    
    putenv(...)
        putenv(key, value)
        
        Change or add an environment variable.
    
    removedirs(name)
        removedirs(name)
        
        Super-rmdir; remove a leaf directory and all empty intermediate
        ones.  Works like rmdir except that, if the leaf directory is
        successfully removed, directories corresponding to rightmost path
        segments will be pruned away until either the whole path is
        consumed or an error occurs.  Errors during this latter phase are
        ignored -- they generally mean that a directory was not empty.
    
    renames(old, new)
        renames(old, new)
        
        Super-rename; create directories as necessary and delete any left
        empty.  Works like rename, except creation of any intermediate
        directories needed to make the new pathname good is attempted
        first.  After the rename, directories corresponding to rightmost
        path segments of the old name will be pruned way until either the
        whole path is consumed or a nonempty directory is found.
        
        Note: this function can fail with the new directory structure made
        if you lack permissions needed to unlink the leaf directory or
        file.
    
    spawnl(mode, file, *args)
        spawnl(mode, file, *args) -> integer
        
        Execute file with arguments from args in a subprocess.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnle(mode, file, *args)
        spawnle(mode, file, *args, env) -> integer
        
        Execute file with arguments from args in a subprocess with the
        supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnlp(mode, file, *args)
        spawnlp(mode, file, *args) -> integer
        
        Execute file (which is looked for along $PATH) with arguments from
        args in a subprocess with the supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnlpe(mode, file, *args)
        spawnlpe(mode, file, *args, env) -> integer
        
        Execute file (which is looked for along $PATH) with arguments from
        args in a subprocess with the supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnv(mode, file, args)
        spawnv(mode, file, args) -> integer
        
        Execute file with arguments from args in a subprocess.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnve(mode, file, args, env)
        spawnve(mode, file, args, env) -> integer
        
        Execute file with arguments from args in a subprocess with the
        specified environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnvp(mode, file, args)
        spawnvp(mode, file, args) -> integer
        
        Execute file (which is looked for along $PATH) with arguments from
        args in a subprocess.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnvpe(mode, file, args, env)
        spawnvpe(mode, file, args, env) -> integer
        
        Execute file (which is looked for along $PATH) with arguments from
        args in a subprocess with the supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    unsetenv(...)
        unsetenv(key)
        
        Delete an environment variable.
    
    walk(top, topdown=True, onerror=None, followlinks=False)
        Directory tree generator.
        
        For each directory in the directory tree rooted at top (including top
        itself, but excluding '.' and '..'), yields a 3-tuple
        
            dirpath, dirnames, filenames
        
        dirpath is a string, the path to the directory.  dirnames is a list of
        the names of the subdirectories in dirpath (excluding '.' and '..').
        filenames is a list of the names of the non-directory files in dirpath.
        Note that the names in the lists are just names, with no path components.
        To get a full path (which begins with top) to a file or directory in
        dirpath, do os.path.join(dirpath, name).
        
        If optional arg 'topdown' is true or not specified, the triple for a
        directory is generated before the triples for any of its subdirectories
        (directories are generated top down).  If topdown is false, the triple
        for a directory is generated after the triples for all of its
        subdirectories (directories are generated bottom up).
        
        When topdown is true, the caller can modify the dirnames list in-place
        (e.g., via del or slice assignment), and walk will only recurse into the
        subdirectories whose names remain in dirnames; this can be used to prune the
        search, or to impose a specific order of visiting.  Modifying dirnames when
        topdown is false is ineffective, since the directories in dirnames have
        already been generated by the time dirnames itself is generated. No matter
        the value of topdown, the list of subdirectories is retrieved before the
        tuples for the directory and its subdirectories are generated.
        
        By default errors from the os.listdir() call are ignored.  If
        optional arg 'onerror' is specified, it should be a function; it
        will be called with one argument, an OSError instance.  It can
        report the error to continue with the walk, or raise the exception
        to abort the walk.  Note that the filename is available as the
        filename attribute of the exception object.
        
        By default, os.walk does not follow symbolic links to subdirectories on
        systems that support them.  In order to get this functionality, set the
        optional argument 'followlinks' to true.
        
        Caution:  if you pass a relative pathname for top, don't change the
        current working directory between resumptions of walk.  walk never
        changes the current directory, and assumes that the client doesn't
        either.
        
        Example:
        
        import os
        from os.path import join, getsize
        for root, dirs, files in os.walk('python/Lib/email'):
            print(root, "consumes", end="")
            print(sum([getsize(join(root, name)) for name in files]), end="")
            print("bytes in", len(files), "non-directory files")
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS directories

DATA
    P_NOWAIT = 1
    P_NOWAITO = 1
    P_WAIT = 0
    SEEK_CUR = 1
    SEEK_END = 2
    SEEK_SET = 0
    __all__ = ['altsep', 'curdir', 'pardir', 'sep', 'pathsep', 'linesep', ...
    altsep = None
    curdir = '.'
    defpath = ':/bin:/usr/bin'
    devnull = '/dev/null'
    environb = environ({b'TERM_PROGRAM_VERSION': b'361.1', b'SS...GS': b'0...
    extsep = '.'
    linesep = '\n'
    name = 'posix'
    pardir = '..'
    pathsep = ':'
    sep = '/'
    supports_bytes_environ = True

FILE
    /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/os.py
```



## dir(os)

```
>>> import os
>>> dir(os)
['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 'F_LOCK', 'F_OK', 'F_TEST', 'F_TLOCK', 'F_ULOCK', 'MutableMapping', 'NGROUPS_MAX', 'O_ACCMODE', 'O_APPEND', 'O_ASYNC', 'O_CREAT', 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_EXLOCK', 'O_NDELAY', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O_RDONLY', 'O_RDWR', 'O_SHLOCK', 'O_SYNC', 'O_TRUNC', 'O_WRONLY', 'PRIO_PGRP', 'PRIO_PROCESS', 'PRIO_USER', 'P_ALL', 'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_WAIT', 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD', 'RTLD_NOW', 'R_OK', 'SCHED_FIFO', 'SCHED_OTHER', 'SCHED_RR', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'ST_NOSUID', 'ST_RDONLY', 'TMP_MAX', 'WCONTINUED', 'WCOREDUMP', 'WEXITED', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_get_exports_list', '_get_masked_mode', '_putenv', '_spawnvef', '_unsetenv', '_wrap_close', 'abort', 'access', 'altsep', 'chdir', 'chflags', 'chmod', 'chown', 'chroot', 'close', 'closerange', 'confstr', 'confstr_names', 'cpu_count', 'ctermid', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'environb', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 'fchmod', 'fchown', 'fdopen', 'fork', 'forkpty', 'fpathconf', 'fsdecode', 'fsencode', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'get_exec_path', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 'getgrouplist', 'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid', 'getppid', 'getpriority', 'getsid', 'getuid', 'initgroups', 'isatty', 'kill', 'killpg', 'lchflags', 'lchmod', 'lchown', 'linesep', 'link', 'listdir', 'lockf', 'lseek', 'lstat', 'major', 'makedev', 'makedirs', 'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty', 'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'popen', 'pread', 'putenv', 'pwrite', 'read', 'readlink', 'readv', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'sched_get_priority_max', 'sched_get_priority_min', 'sched_yield', 'sendfile', 'sep', 'set_inheritable', 'setegid', 'seteuid', 'setgid', 'setgroups', 'setpgid', 'setpgrp', 'setpriority', 'setregid', 'setreuid', 'setsid', 'setuid', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe', 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'st', 'stat', 'stat_float_times', 'stat_result', 'statvfs', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names', 'system', 'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 'truncate', 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitpid', 'walk', 'write', 'writev']
```



## dir(os) list

```
CLD_CONTINUED
CLD_DUMPED
CLD_EXITED
CLD_TRAPPED
EX_CANTCREAT
EX_CONFIG
EX_DATAERR
EX_IOERR
EX_NOHOST
EX_NOINPUT
EX_NOPERM
EX_NOUSER
EX_OK
EX_OSERR
EX_OSFILE
EX_PROTOCOL
EX_SOFTWARE
EX_TEMPFAIL
EX_UNAVAILABLE
EX_USAGE
F_LOCK
F_OK
F_TEST
F_TLOCK
F_ULOCK
MutableMapping
NGROUPS_MAX
O_ACCMODE
O_APPEND
O_ASYNC
O_CREAT
O_DIRECTORY
O_DSYNC
O_EXCL
O_EXLOCK
O_NDELAY
O_NOCTTY
O_NOFOLLOW
O_NONBLOCK
O_RDONLY
O_RDWR
O_SHLOCK
O_SYNC
O_TRUNC
O_WRONLY
PRIO_PGRP
PRIO_PROCESS
PRIO_USER
P_ALL
P_NOWAIT
P_NOWAITO
P_PGID
P_PID
P_WAIT
RTLD_GLOBAL
RTLD_LAZY
RTLD_LOCAL
RTLD_NODELETE
RTLD_NOLOAD
RTLD_NOW
R_OK
SCHED_FIFO
SCHED_OTHER
SCHED_RR
SEEK_CUR
SEEK_END
SEEK_SET
ST_NOSUID
ST_RDONLY
TMP_MAX
WCONTINUED
WCOREDUMP
WEXITED
WEXITSTATUS
WIFCONTINUED
WIFEXITED
WIFSIGNALED
WIFSTOPPED
WNOHANG
WNOWAIT
WSTOPPED
WSTOPSIG
WTERMSIG
WUNTRACED
W_OK
X_OK
_Environ
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
_execvpe
_exists
_exit
_get_exports_list
_get_masked_mode
_putenv
_spawnvef
_unsetenv
_wrap_close
abort
access
altsep
chdir
chflags
chmod
chown
chroot
close
closerange
confstr
confstr_names
cpu_count
ctermid
curdir
defpath
device_encoding
devnull
dup
dup2
environ
environb
errno
error
execl
execle
execlp
execlpe
execv
execve
execvp
execvpe
extsep
fchdir
fchmod
fchown
fdopen
fork
forkpty
fpathconf
fsdecode
fsencode
fstat
fstatvfs
fsync
ftruncate
get_exec_path
get_inheritable
get_terminal_size
getcwd
getcwdb
getegid
getenv
getenvb
geteuid
getgid
getgrouplist
getgroups
getloadavg
getlogin
getpgid
getpgrp
getpid
getppid
getpriority
getsid
getuid
initgroups
isatty
kill
killpg
lchflags
lchmod
lchown
linesep
link
listdir
lockf
lseek
lstat
major
makedev
makedirs
minor
mkdir
mkfifo
mknod
name
nice
open
openpty
pardir
path
pathconf
pathconf_names
pathsep
pipe
popen
pread
putenv
pwrite
read
readlink
readv
remove
removedirs
rename
renames
replace
rmdir
sched_get_priority_max
sched_get_priority_min
sched_yield
sendfile
sep
set_inheritable
setegid
seteuid
setgid
setgroups
setpgid
setpgrp
setpriority
setregid
setreuid
setsid
setuid
spawnl
spawnle
spawnlp
spawnlpe
spawnv
spawnve
spawnvp
spawnvpe
st
stat
stat_float_times
stat_result
statvfs
statvfs_result
strerror
supports_bytes_environ
supports_dir_fd
supports_effective_ids
supports_fd
supports_follow_symlinks
symlink
sync
sys
sysconf
sysconf_names
system
tcgetpgrp
tcsetpgrp
terminal_size
times
times_result
truncate
ttyname
umask
uname
uname_result
unlink
unsetenv
urandom
utime
wait
wait3
wait4
waitpid
walk
write
writev
```



## os 模块的处理文件和目录，常用的方法

| 序号   | 方法及描述                                    |
| ---- | ---------------------------------------- |
| 1    | [os.access(path, mode)](http://www.runoob.com/python3/python3-os-access.html) 检验权限模式 |
| 2    | [os.chdir(path)](http://www.runoob.com/python3/python3-os-chdir.html) 改变当前工作目录 |
| 3    | [os.chflags(path, flags)](http://www.runoob.com/python3/python3-os-chflags.html) 设置路径的标记为数字标记。 |
| 4    | [os.chmod(path, mode)](http://www.runoob.com/python3/python3-os-chmod.html) 更改权限 |
| 5    | [os.chown(path, uid, gid)](http://www.runoob.com/python3/python3-os-chown.html) 更改文件所有者 |
| 6    | [os.chroot(path)](http://www.runoob.com/python3/python3-os-chroot.html) 改变当前进程的根目录 |
| 7    | [os.close(fd)](http://www.runoob.com/python3/python3-os-close.html) 关闭文件描述符 fd |
| 8    | [os.closerange(fd_low, fd_high) ](http://www.runoob.com/python3/python3-os-closerange.html) 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略 |
| 9    | [os.dup(fd)](http://www.runoob.com/python3/python3-os-dup.html) 复制文件描述符 fd |
| 10   | [os.dup2(fd, fd2)](http://www.runoob.com/python3/python3-os-dup2.html) 将一个文件描述符 fd 复制到另一个 fd2 |
| 11   | [os.fchdir(fd)](http://www.runoob.com/python3/python3-os-fchdir.html) 通过文件描述符改变当前工作目录 |
| 12   | [os.fchmod(fd, mode)](http://www.runoob.com/python3/python3-os-fchmod.html) 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。 |
| 13   | [os.fchown(fd, uid, gid)](http://www.runoob.com/python3/python3-os-fchown.html) 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。 |
| 14   | [os.fdatasync(fd)](http://www.runoob.com/python3/python3-os-fdatasync.html) 强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。 |
| 15   | [os.fdopen(fd[, mode[, bufsize\]])](http://www.runoob.com/python3/python3-os-fdopen.html) 通过文件描述符 fd 创建一个文件对象，并返回这个文件对象 |
| 16   | [os.fpathconf(fd, name)](http://www.runoob.com/python3/python3-os-fpathconf.html) 返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。 |
| 17   | [os.fstat(fd)](http://www.runoob.com/python3/python3-os-fstat.html) 返回文件描述符fd的状态，像stat()。 |
| 18   | [os.fstatvfs(fd)](http://www.runoob.com/python3/python3-os-fstatvfs.html) 返回包含文件描述符fd的文件的文件系统的信息，像 statvfs() |
| 19   | [os.fsync(fd)](http://www.runoob.com/python3/python3-os-fsync.html)强制将文件描述符为fd的文件写入硬盘。 |
| 20   | [os.ftruncate(fd, length)](http://www.runoob.com/python3/python3-os-ftruncate.html)裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。 |
| 21   | [os.getcwd()](http://www.runoob.com/python3/python3-os-getcwd.html)返回当前工作目录 |
| 22   | [os.getcwdu()](http://www.runoob.com/python3/python3-os-getcwdu.html)返回一个当前工作目录的Unicode对象 |
| 23   | [os.isatty(fd)](http://www.runoob.com/python3/python3-os-isatty.html)如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。 |
| 24   | [os.lchflags(path, flags)](http://www.runoob.com/python3/python3-os-lchflags.html)设置路径的标记为数字标记，类似 chflags()，但是没有软链接 |
| 25   | [os.lchmod(path, mode)](http://www.runoob.com/python3/python3-os-lchmod.html)修改连接文件权限 |
| 26   | [os.lchown(path, uid, gid)](http://www.runoob.com/python3/python3-os-lchown.html)更改文件所有者，类似 chown，但是不追踪链接。 |
| 27   | [os.link(src, dst)](http://www.runoob.com/python3/python3-os-link.html)创建硬链接，名为参数 dst，指向参数 src |
| 28   | [os.listdir(path)](http://www.runoob.com/python3/python3-os-listdir.html)返回path指定的文件夹包含的文件或文件夹的名字的列表。 |
| 29   | [os.lseek(fd, pos, how)](http://www.runoob.com/python3/python3-os-lseek.html)设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效 |
| 30   | [os.lstat(path)](http://www.runoob.com/python3/python3-os-lstat.html)像stat(),但是没有软链接 |
| 31   | [os.major(device)](http://www.runoob.com/python3/python3-os-major.html)从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。 |
| 32   | [os.makedev(major, minor)](http://www.runoob.com/python3/python3-os-makedev.html)以major和minor设备号组成一个原始设备号 |
| 33   | [os.makedirs(path[, mode])](http://www.runoob.com/python3/python3-os-makedirs.html) 递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。 |
| 34   | [os.minor(device)](http://www.runoob.com/python3/python3-os-minor.html)从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。 |
| 35   | [os.mkdir(path[, mode])](http://www.runoob.com/python3/python3-os-mkdir.html) 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。 |
| 36   | [os.mkfifo(path[, mode])](http://www.runoob.com/python3/python3-os-mkfifo.html) 创建命名管道，mode 为数字，默认为 0666 (八进制) |
| 37   | [os.mknod(filename[, mode=0600, device])](http://www.runoob.com/python3/python3-os-mknod.html) 创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。 |
| 38   | [os.open(file, flags[, mode])](http://www.runoob.com/python3/python3-os-open.html) 打开一个文件，并且设置需要的打开选项，mode参数是可选的 |
| 39   | [os.openpty()](http://www.runoob.com/python3/python3-os-openpty.html)打开一个新的伪终端对。返回 pty 和 tty的文件描述符。 |
| 40   | [os.pathconf(path, name)](http://www.runoob.com/python3/python3-os-pathconf.html)返回相关文件的系统配置信息。 |
| 41   | [os.pipe()](http://www.runoob.com/python3/python3-os-pipe.html)创建一个管道. 返回一对文件描述符(r, w) 分别为读和写 |
| 42   | [os.popen(command[, mode[, bufsize\]])](http://www.runoob.com/python3/python3-os-popen.html)从一个 command 打开一个管道 |
| 43   | [os.read(fd, n)](http://www.runoob.com/python3/python3-os-read.html)从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。 |
| 44   | [os.readlink(path)](http://www.runoob.com/python3/python3-os-readlink.html)返回软链接所指向的文件 |
| 45   | [os.remove(path)](http://www.runoob.com/python3/python3-os-remove.html)删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。 |
| 46   | [os.removedirs(path)](http://www.runoob.com/python3/python3-os-removedirs.html)递归删除目录。 |
| 47   | [os.rename(src, dst)](http://www.runoob.com/python3/python3-os-rename.html)重命名文件或目录，从 src 到 dst |
| 48   | [os.renames(old, new)](http://www.runoob.com/python3/python3-os-renames.html)递归地对目录进行更名，也可以对文件进行更名。 |
| 49   | [os.rmdir(path)](http://www.runoob.com/python3/python3-os-rmdir.html)删除path指定的空目录，如果目录非空，则抛出一个OSError异常。 |
| 50   | [os.stat(path)](http://www.runoob.com/python3/python3-os-stat.html)获取path指定的路径的信息，功能等同于C API中的stat()系统调用。 |
| 51   | [os.stat_float_times([newvalue])](http://www.runoob.com/python3/python3-os-stat_float_times.html) 决定stat_result是否以float对象显示时间戳 |
| 52   | [os.statvfs(path)](http://www.runoob.com/python3/python3-os-statvfs.html)获取指定路径的文件系统统计信息 |
| 53   | [os.symlink(src, dst)](http://www.runoob.com/python3/python3-os-symlink.html)创建一个软链接 |
| 54   | [os.tcgetpgrp(fd)](http://www.runoob.com/python3/python3-os-tcgetpgrp.html)返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组 |
| 55   | [os.tcsetpgrp(fd, pg)](http://www.runoob.com/python3/python3-os-tcsetpgrp.html)设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。 |
| 56   | [os.tempnam([dir[, prefix\]])](http://www.runoob.com/python3/python3-os-tempnam.html)返回唯一的路径名用于创建临时文件。 |
| 57   | [os.tmpfile()](http://www.runoob.com/python3/python3-os-tmpfile.html)返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。 |
| 58   | [os.tmpnam()](http://www.runoob.com/python3/python3-os-tmpnam.html)为创建一个临时文件返回一个唯一的路径 |
| 59   | [os.ttyname(fd)](http://www.runoob.com/python3/python3-os-ttyname.html)返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。 |
| 60   | [os.unlink(path)](http://www.runoob.com/python3/python3-os-unlink.html)删除文件路径 |
| 61   | [os.utime(path, times)](http://www.runoob.com/python3/python3-os-utime.html)返回指定的path文件的访问和修改的时间。 |
| 62   | `os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])` 输出在文件夹中的文件名通过在树中游走，向上或者向下。 |
| 63   | [os.write(fd, str)](http://www.runoob.com/python3/python3-os-write.html)写入字符串到文件描述符 fd中. 返回实际写入的字符串长度 |



### os.chdir()

`os.chdir()` 方法用于改变当前工作目录到指定的路径。

> ```
> Help on built-in function chdir in module posix:
>
> chdir(...)
>     chdir(path)
>     
>     Change the current working directory to the specified path.
>     
>     path may always be specified as a string.
>     On some platforms, path may also be specified as an open file descriptor.
>       If this functionality is unavailable, using it raises an exception.
> ```

语法:

```
os.chdir(path)
```

**path** -- 要切换到的新路径。

如果允许访问返回 True , 否则返回False。

example:

```python
>>> os.getcwd()
'/Users/mac'
>>> os.chdir("/Users/yulei/Music")
>>> os.getcwd()
'/Users/mac/Music'
```









### os.getcwd()

os.getcwd() 方法用于返回当前工作目录。

> ```
> getcwd(...)
>     getcwd() -> path
>     
>     Return a unicode string representing the current working directory.
> ```

**语法**

```
os.getcwd()
```

返回当前进程的工作目录。

example:

```python
>>> import os
>>> print(os.getcwd())
/Users/myMac
```





### os.listdir()

`os.listdir()` 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。

只支持在 Unix, Windows 下使用。

> ```
> Help on built-in function listdir in module posix:
>
> listdir(...)
>     listdir(path='.') -> list_of_filenames
>     
>     Return a list containing the names of the files in the directory.
>     The list is in arbitrary order.  It does not include the special
>     entries '.' and '..' even if they are present in the directory.
>     
>     path can be specified as either str or bytes.  If path is bytes,
>       the filenames returned will also be bytes; in all other circumstances
>       the filenames returned will be str.
>     On some platforms, path may also be specified as an open file descriptor;
>       the file descriptor must refer to a directory.
>       If this functionality is unavailable, using it raises NotImplementedError.
> ```

**语法**

```
os.listdir(path)
```

**path** -- 需要列出的目录路径

返回指定路径下的文件和文件夹列表。

example:

```python
>>> import os
>>> print(os.listdir("/Users"))
['.localized', 'Shared', 'userMac']
```





### os.rename()

`os.rename()` 方法用于命名文件或目录，从 src 到 dst,如果dst是一个存在的目录, 将抛出OSError。

> ```
> Help on built-in function rename in module posix:
>
> rename(...)
>     rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
>     
>     Rename a file or directory.
>     
>     If either src_dir_fd or dst_dir_fd is not None, it should be a file
>       descriptor open to a directory, and the respective path string (src or dst)
>       should be relative; the path will then be relative to that directory.
>     src_dir_fd and dst_dir_fd, may not be implemented on your platform.
>       If they are unavailable, using them will raise a NotImplementedError.
> ```

**语法**

```
os.rename(src, dst)
```

- **src** -- 要修改的目录名
- **dst** -- 修改后的目录名

该方法没有返回值

example:

```python
>>> import os
>>> os.getcwd()
'/Users/yulei/Documents/YL/Hub/HTMLCSSJS_imac/Test Field/py/renameFiles'
>>> os.listdir()
['.DS_Store', 'folder', 'X.txt', 'XXYY.txt', 'Y.txt']
>>> file = os.listdir()[1]
>>> file
'folder'
>>> os.rename(file, "FOLDER")
>>> os.listdir()
['.DS_Store', 'FOLDER', 'X.txt', 'XXYY.txt', 'Y.txt']
```