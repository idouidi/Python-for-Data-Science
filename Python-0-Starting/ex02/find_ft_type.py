# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: idouidi <idouidi@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/09 13:50:33 by idouidi           #+#    #+#              #
#    Updated: 2026/05/09 14:30:33 by idouidi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
    if type(object) is str:
        print(f"{object} is in the kitchen : {type(object)}")
    elif type(object) is int:
        print("Type not found")
    else:
        print(type(object))
    return 42