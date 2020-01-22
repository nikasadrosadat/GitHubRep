<h1>Raspberry Pi Status: rpi13</h1>
<h2>Host Info</h2>
<li>Host name : rpi13</li>
<li>IP Address: 172.19.32.113 </li>
<li>OS name:    Raspbian GNU/Linux 10 (buster)</li>
<h2>Who is logged in</h2>
<pre>           system boot  1969-12-31 16:00
           run-level 3  2020-01-17 14:37
LOGIN      tty1         2020-01-17 14:37               468 id=tty1
sp1a     + pts/0        2020-01-22 11:59   .         10312 (172.19.32.49)
sp1b     + pts/1        2020-01-22 11:59   .         10314 (172.19.32.26)</pre>
<h2>Performance Summary</h2>
<pre>top - 12:44:22 up 1 day,  1:16,  2 users,  load average: 0.00, 0.00, 0.00
Tasks: 121 total,   1 running, 120 sleeping,   0 stopped,   0 zombie
%Cpu(s):  1.4 us,  2.8 sy,  0.0 ni, 95.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :    926.1 total,    637.8 free,     73.5 used,    214.8 buff/cache
MiB Swap:    100.0 total,    100.0 free,      0.0 used.    788.5 avail Mem </pre>
<h2>Top 5 Processes by CPU</h2>
<pre>USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
sp1a     11233  1.0  0.2   7676  2460 pts/0    S+   12:44   0:00 /bin/bash ./pistatus.cgi
sp1b     11229  0.3  0.4   8668  3848 pts/1    S+   12:42   0:00 nano chem2.c
root         1  0.0  0.8  33696  7920 ?        Ss   Jan21   0:07 /sbin/init splash
root         2  0.0  0.0      0     0 ?        S    Jan21   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        I<   Jan21   0:00 [rcu_gp]</pre>
<h2>Top 5 Processes by Memory</h2>
<pre>USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root       449  0.0  1.8 191656 17120 ?        Ss   Jan21   0:03 /usr/sbin/apache2 -k star
root       107  0.0  0.8  18952  8380 ?        Ss   Jan21   0:03 /lib/systemd/systemd-jour
root         1  0.0  0.8  33696  7920 ?        Ss   Jan21   0:07 /sbin/init splash
sp1b     10357  0.0  0.7  14564  7304 ?        Ss   11:59   0:00 /lib/systemd/systemd --us
sp1a     10320  0.0  0.7  14564  7260 ?        Ss   11:59   0:00 /lib/systemd/systemd --us</pre>
