

# module os  



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
| 2    | [os.chdir(path)](http://www.runoob.com/python3/python3-os-chdir.html)改变当前工作目录 |
| 3    | [os.chflags(path, flags)](http://www.runoob.com/python3/python3-os-chflags.html)设置路径的标记为数字标记。 |
| 4    | [os.chmod(path, mode)](http://www.runoob.com/python3/python3-os-chmod.html)更改权限 |
| 5    | [os.chown(path, uid, gid)](http://www.runoob.com/python3/python3-os-chown.html)更改文件所有者 |
| 6    | [os.chroot(path)](http://www.runoob.com/python3/python3-os-chroot.html)改变当前进程的根目录 |
| 7    | [os.close(fd)](http://www.runoob.com/python3/python3-os-close.html)关闭文件描述符 fd |
| 8    | [os.closerange(fd_low, fd_high)](http://www.runoob.com/python3/python3-os-closerange.html)关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略 |
| 9    | [os.dup(fd)](http://www.runoob.com/python3/python3-os-dup.html)复制文件描述符 fd |
| 10   | [os.dup2(fd, fd2)](http://www.runoob.com/python3/python3-os-dup2.html)将一个文件描述符 fd 复制到另一个 fd2 |
| 11   | [os.fchdir(fd)](http://www.runoob.com/python3/python3-os-fchdir.html)通过文件描述符改变当前工作目录 |
| 12   | [os.fchmod(fd, mode)](http://www.runoob.com/python3/python3-os-fchmod.html)改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。 |
| 13   | [os.fchown(fd, uid, gid)](http://www.runoob.com/python3/python3-os-fchown.html)修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。 |
| 14   | [os.fdatasync(fd)](http://www.runoob.com/python3/python3-os-fdatasync.html)强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。 |
| 15   | [os.fdopen(fd[, mode[, bufsize\]])](http://www.runoob.com/python3/python3-os-fdopen.html)通过文件描述符 fd 创建一个文件对象，并返回这个文件对象 |
| 16   | [os.fpathconf(fd, name)](http://www.runoob.com/python3/python3-os-fpathconf.html)返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。 |
| 17   | [os.fstat(fd)](http://www.runoob.com/python3/python3-os-fstat.html)返回文件描述符fd的状态，像stat()。 |
| 18   | [os.fstatvfs(fd)](http://www.runoob.com/python3/python3-os-fstatvfs.html)返回包含文件描述符fd的文件的文件系统的信息，像 statvfs() |
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