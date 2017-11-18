all:
	echo '#!/usr/bin/env python' | cat - Sender.py > secret_sender
	chmod +x secret_sender
