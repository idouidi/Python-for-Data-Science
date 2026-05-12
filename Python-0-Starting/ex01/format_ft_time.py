# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: idouidi <idouidi@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/09 13:11:36 by idouidi           #+#    #+#              #
#    Updated: 2026/05/09 13:31:54 by idouidi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import time
from datetime import datetime

now = time()

print(f"Seconds since January 1, 1970: {now:,.4f} or {now:.2e} in scientific notation")
print(datetime.fromtimestamp(now).strftime("%b %d %Y"))