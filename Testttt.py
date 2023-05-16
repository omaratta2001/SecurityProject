import pickle
import socket
import threading
from tkinter import *
import DES, AES, RSA3, gamal


class Client:
    def __init__(self, host=socket.gethostname(), port=55555):
        self.message1 = None
        self.s = 0
        self.algo = None
        self.ciphertext_list = None
        self.nickname = ""
        self.key = ""
        self.p = None
        self.q = None
        self.p2 = None
        self.q2 = None
        self.p1 = None
        self.g1=None
        self.y1 = None
        self.x1=None
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.mypublic_key =None
        self.public_key =None
        self.private_key =None
        self.root = Tk()
        self.root.title("Chat Room")
        self.root.configure(bg="lightgray")
        self.root.protocol("WM_DELETE_WINDOW", self.stop)

        self.message_frame = Frame(self.root)
        self.scrollbar = Scrollbar(self.message_frame)
        self.message_list = Listbox(self.message_frame, height=20, width=80, yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.message_list.pack(side=LEFT, fill=BOTH)
        self.message_frame.pack(pady=10)

        self.input_frame = Frame(self.root)
        self.message_entry = Entry(self.input_frame, width=60)
        self.message_entry.pack(side=LEFT, padx=10)
        self.send_button = Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=LEFT)
        self.input_frame.pack(pady=10)

        self.nickname_frame = Frame(self.root)
        self.nickname_label = Label(self.nickname_frame, text="Nickname:")
        self.nickname_label.pack(side=LEFT, padx=5)
        self.nickname_entry = Entry(self.nickname_frame, width=20)
        self.nickname_entry.pack(side=LEFT)
        self.nickname_button = Button(self.nickname_frame, text="Set Nickname", command=self.set_nickname)
        self.nickname_button.pack(side=LEFT)

        # Add four new buttons above the nickname entry
        self.button_frame = Frame(self.root)
        self.button1 = Button(self.button_frame, text="DES", command=self.button1_clicked)
        self.button1.pack(side=LEFT, padx=5)
        self.button2 = Button(self.button_frame, text="AES", command=self.button2_clicked)
        self.button2.pack(side=LEFT, padx=5)
        # self.button1 = Button(self.root, text="Button 1", command=lambda: self.button_clicked("Button 1"))
        # self.button2 = Button(self.root, text="Button 2", command=lambda: self.button_clicked("Button 2"))
        # self.button3 = Button(self.root, text="Button 3", command=lambda: self.button_clicked("Button 3"))
        # self.button4 = Button(self.root, text="Button 4", command=lambda: self.button_clicked("Button 4"))
        self.button3 = Button(self.button_frame, text="Gamal", command=self.button3_clicked)
        self.button3.pack(side=LEFT, padx=5)
        self.button4 = Button(self.button_frame, text="RSA", command=self.button4_clicked)
        self.button4.pack(side=LEFT, padx=5)

        self.nickname_frame.pack(pady=5)
        self.button_frame.pack(pady=5)

        self.key_frame = Frame(self.root)
        self.key_label = Label(self.key_frame, text="Key:")
        self.key_label.pack(side=LEFT, padx=5)
        self.key_entry = Entry(self.key_frame, width=20, show="*")
        self.key_entry.pack(side=LEFT)
        self.key_button = Button(self.key_frame, text="Set Key", command=self.set_key)
        self.key_button.pack(side=LEFT)
        self.key_frame.pack(pady=5)

        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def set_nickname(self):
        nickname = self.nickname_entry.get().strip()
        if nickname:
            self.nickname = nickname
            self.nickname_entry.config(state=DISABLED)
            self.nickname_button.config(state=DISABLED)
            self.message_entry.config(state=NORMAL)
            self.send_button.config(state=NORMAL)

    def button1_clicked(self):
        self.algo = "1"
        self.button1.config(state=DISABLED)
        self.button2.config(state=DISABLED)
        self.button3.config(state=DISABLED)
        self.button4.config(state=DISABLED)

    def button2_clicked(self):
        self.algo = "2"
        self.button1.config(state=DISABLED)
        self.button2.config(state=DISABLED)
        self.button3.config(state=DISABLED)
        self.button4.config(state=DISABLED)

    def button3_clicked(self):
        self.algo = "3"
        self.button1.config(state=DISABLED)
        self.button2.config(state=DISABLED)
        self.button3.config(state=DISABLED)
        self.button4.config(state=DISABLED)

    def button4_clicked(self):
        self.algo = "4"
        self.button1.config(state=DISABLED)
        self.button2.config(state=DISABLED)
        self.button3.config(state=DISABLED)
        self.button4.config(state=DISABLED)

    def set_key(self):
        key = self.key_entry.get().strip()
        print(self.algo)
        if key:
            self.key = key
            self.key_entry.config(state=DISABLED)
            self.key_button.config(state=DISABLED)
        if self.algo == "1":
            binary = DES.text_to_binary(key)
            self.round_keys = DES.generate_round_keys(binary)
            print(self.round_keys)
        if self.algo == "2":
            self.k0, self.k1, self.k2 = AES.Key_Generation(key)

        if self.algo == "3":
            self.s=1
            keys = gamal.generate_keys()
            self.p1, self.g1, self.y1, self.x1 = keys
            self.private_key = (self.p1, self.g1, self.y1, self.x1)
            self.mypublic_key = (self.p1, self.g1, self.y1)
            self.client.sendall(pickle.dumps(self.mypublic_key))
            while True:

                self.public_key = pickle.loads(self.client.recv(4096))
                if not self.public_key:
                    break
            print(self.public_key)
            self.s=0

        if self.algo == "4":
            self.s = 1
            self.p, self.q = key.split(',')
            self.p, self.q = RSA3.generate_keypair(int(self.p), int(self.q))
            self.client.sendall(pickle.dumps(self.p))
            self.p2 = pickle.loads(self.client.recv(4096))
            print(self.p2,self.q)


    def send_message(self):

        message = self.message_entry.get().strip()
        if message:
            print(message)
            if self.algo == "1":
                print(self.algo)

                plaintext_list = [message[i:i + 8] for i in range(0, len(message), 8)]
                if len(plaintext_list[-1]) < 8:
                    plaintext_list[-1] += ' ' * (8 - len(plaintext_list[-1]))
                print(plaintext_list)
                ciphertext_list = []
                for block in plaintext_list:
                    # Convert the block to binary
                    block_binary = DES.text_to_binary(block)
                    print(block_binary)
                    # Encrypt the block using the round keys
                    ciphertext_binary = DES.encrypt_DES(block_binary, self.round_keys)

                    # Convert the ciphertext back to a string and add it to the list
                    ciphertext_list.append(DES.bin_to_str(ciphertext_binary))
                    print(ciphertext_list)
                    message = f"".join(ciphertext_list)
            if self.algo == "2":
                message = AES.plaintext_to_binary1(message)
                message = AES.encryption(message, self.k0, self.k1, self.k2)
                message = AES.tostring(message)

            if self.algo == "4":
                message = RSA3.encrypt_RSA(self.p, message)
                print(message)
            if self.algo =="3":
               message = gamal.encrypt_str(self.public_key[0], self.public_key[1], self.public_key[2], message)

            self.client.send(pickle.dumps(str(message)))
            self.message_entry.delete(0, END)

    def receive_messages(self):
        while True:
            try:
                if self.s == 0:
                    message = pickle.loads(self.client.recv((4096)))
                if self.public_key:
                    message = pickle.loads(self.client.recv((4096)))

                if self.algo == "1":

                    plaintext_list = [message[i:i + 8] for i in range(0, len(message), 8)]
                    if len(plaintext_list[-1]) < 8:
                        plaintext_list[-1] += ' ' * (8 - len(plaintext_list[-1]))
                    print(plaintext_list)
                    self.ciphertext_list = []
                    for block in plaintext_list:
                        # Convert the block to binary
                        block_binary = DES.text_to_binary(block)
                        print(block_binary)
                        # Encrypt the block using the round keys
                        ciphertext_binary = DES.decrypt_DES(block_binary, self.round_keys)

                        # Convert the ciphertext back to a string and add it to the list
                        self.ciphertext_list.append(DES.bin_to_str(ciphertext_binary))
                        print(self.ciphertext_list)
                        message = f"".join(self.ciphertext_list)
                if self.algo == "2":
                    message = AES.plaintext_to_binary1(message)
                    message = AES.decryption(message, self.k0, self.k1, self.k2)
                    message = AES.tostring(message)
                if self.algo == "4":
                    message = RSA3.decrypt_RSA(self.q, message)
                if self.algo == "3":
                    message = gamal.decrypt_str(self.private_key[0], self.private_key[3], message[0], message[1])

                if not message:
                    raise ConnectionAbortedError()
                self.message_list.insert(END, message)
                self.message_list.yview(END)
            except ConnectionAbortedError:
                print("Connection aborted.")
                self.client.close()
                break
            except ConnectionResetError:
                print("Connection reset by peer.")
                self.client.close()
                break
            except OSError:
                print("Connection closed.")
                self.client.close()
                break
            except Exception as e:
                print("Error occurred:", str(e))
                self.client.close()
                break

    def stop(self):
        self.client.close()
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    client = Client()
    client.run()
