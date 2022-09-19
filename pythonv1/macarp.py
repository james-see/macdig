import duckdb
import os


def getDevices() -> (list):
    devices = []
    for device in os.popen("arp -a | cut -d' ' -f 2,4 | tr -d '()'"):
        devices.append(device)
    return devices


def main():
    devices = getDevices()
    print(devices[0])
    databasepathname = os.path.dirname(os.path.abspath(__file__))
    print(databasepathname)
    macaddressespath = f"{databasepathname}/assets/macaddresses.csv"
    con = duckdb.connect(
        database=f"{databasepathname}/assets/ducky.db", read_only=False
    )
    con.execute(
        "CREATE TABLE IF NOT EXISTS macaddresses AS SELECT * FROM read_csv_auto(?);",
        [macaddressespath],
    )
    # con.execute("SELECT * from macaddresses;") # testing to confirm working
    for device in devices:
        ip, mac = device.split()
        mac = mac[:8]
        # print(mac)
        # mac = "1:0:5e" testing single digits, makes no difference apparantly
        # print(mac)
        con.execute(
            'SELECT "Vendor Name" from macaddresses where "Mac Prefix" ilike ? limit 1;',
            [mac],
        )
        print(f"For ip: {ip} and mac: {mac}, this is the Vendor Name: {con.fetchall()}")
    # duckdb learning session examples
    # con.execute('SELECT "Mac Prefix" from macaddresses order by random() limit 1;') # testing order by random
    # print(con.description) # testing get column names
    # print(con.fetchall()[0][0])  testing get value from tuple from fetchall return
    # con.execute('SELECT "Vendor Name" from macaddresses where "Mac Prefix" = ?;', [macquery]) testing prepared statements


if __name__ == "__main__":
    main()
