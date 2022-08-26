import random
import in_place
import json
import string


def enc_init():
    commands = {'info': enc_info, 'load':enc_load, 'newkey':enc_newkey, 'save':enc_save}
    return commands


def main_cli():
    commands = enc_init()
    cli_end = False
    while not cli_end:
        cmd_str = input('subs>')
        cmd = cmd_str.split()
        if cmd and cmd[0] == 'done':
            cli_end = True
        if  cmd:
            commands[cmd[0]](cmd[1:])


def enc_save(*params):

    global my_dic_key
    my_dic_key = {base[i]:encrypted[i] for i in range(len(base))}
    with in_place.InPlace('enckey.txt') as f:
        f.writelines(json.dumps(my_dic_key))
        print("Enc/Dec are saved in enckey file")

def enc_load(*params):

    fp = open('enckey.txt','r')
    mykey = json.loads(fp.read())
    print("load key: " , mykey)
    fp.close()

def enc_newkey(*params):
    global base
    global encrypted
    base = encrypted = string.ascii_lowercase
    encrypted = list(string.ascii_lowercase)
    random.shuffle(encrypted)
    print(encrypted)

def enc_info(*params):
    
    mydic2 = {encrypted[i]:base[i] for i in range(len(encrypted))}
    print("my current key : " , encrypted)
    print("my encryption key : " , my_dic_key.values())
    print("my decryption key : " , mydic2.values())

main_cli()
