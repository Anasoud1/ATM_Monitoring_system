-- Insert data into Region table
INSERT INTO Region (id, regionName) VALUES
(1, 'East Coast'),
(2, 'West Coast'),
(3, 'Midwest');

-- Insert data into Branch table
INSERT INTO Branch (branchId, branchName, regionId) VALUES
(1, 'Main Branch', 1),
(2, 'Downtown Branch', 1),
(3, 'West Coast Headquarters', 2),
(4, 'Chicago Office', 3),
(5, 'University Branch', 2);

-- Insert data into Device table
INSERT INTO Device (deviceId, deviceModel, deviceManufacturer, deviceSerialNumber) VALUES
(1, 'Cash Dispenser 5000', 'Acme Corporation', 'ACME-CD5000-12345'),
(2, 'Card Reader CR-700', 'GlobalTech', 'GT-CR700-54321'),
(3, 'Receipt Printer RP-200', 'ValuePrint', 'VP-RP200-98765'),
(4, 'Cash Acceptor CA-3000', 'SecureCash', 'SC-CA3000-01234'),
(5, 'Fingerprint Scanner FS-1000', 'BioTech Security', 'BTS-FS1000-33456'),
(6, 'Touchscreen Display TS-500', 'EasyTouch Solutions', 'ETS-TS500-78945'),
(7, 'PIN Pad PP-200 (older model)', 'Legacy Systems', 'LS-PP200-12345'),
(8, 'Cash Dispenser HD-8000 (high-capacity)', 'SecureCash', 'SC-HD8000-56789'),
(9, 'Card Reader CR-800 (contactless)', 'GlobalTech', 'GT-CR800-90123'),
(10, 'Thermal Camera TC-2000 (environmental monitoring)', 'EnviroTech', 'ET-TC2000-45678'),
(11, 'Voice Guidance Module VG-100', 'Accessibility Solutions', 'AS-VG100-78901');


-- Insert data into AtmDevices table
INSERT INTO AtmDevice (atmId, deviceId, deviceStatus) VALUES
(4, 6, 'Operational'),
(1, 3, 'Operational'),
(5, 8, 'Faulty'),
(2, 4, 'Under Maintenance'),
(3, 5, 'Faulty'),
(1, 2, 'Under Maintenance'),
(6, 10, 'Under Maintenance'),
(5, 9, 'Operational'),
(1, 1, 'Operational'),
(4, 7, 'Under Maintenance'),
(2, 1, 'Operational'),
(6, 11, 'Operational'),
(3, 1, 'Operational');


-- Insert data into ElectronicJournals table
INSERT INTO ElectronicJournal (ejId, ejData, atmId, timestamp) VALUES
(1, 'Network interface card (NIC) rebooted due to unresponsive state.', 1, '2024-03-05T10:15:00Z'),
(2, 'Software update v1.2.4 downloaded and installed successfully. Reboot initiated.', 2, '2024-03-05T12:00:00Z'),
(3, 'Disk space usage threshold exceeded (95%). Initiated disk cleanup procedures.', 3, '2024-03-05T08:30:00Z'),
(4, 'Cash dispenser motor detected overheating. Disabling cash dispense functionality until further investigation.', 4, '2024-03-05T14:22:00Z'),
(5, 'Receipt printer low on paper (20% remaining). Sending alert for paper refill.', 5, '2024-03-05T16:05:00Z'),
(6, 'Application error encountered (code: ABC123). Restarting application service.', 6, '2024-03-05T13:40:00Z'),
(7, 'ATM communication lost (ping timeout). Attempting to re-establish connection.', 7, '2024-03-05T17:15:00Z'),
(8, 'System log rotated successfully. Old logs archived.', 1, '2024-03-04T23:59:00Z'),
(9, 'Scheduled maintenance completed. System rebooted and services restarted.', 3, '2024-03-05T06:00:00Z'),
(10, 'Security software detected suspicious activity. User attempted to access unauthorized functionality. Initiating investigation.', 5, '2024-03-05T15:30:00Z');


-- Insert data into Event table
INSERT INTO Event (eventId, eventName, eventLevel, ejId) VALUES
(1, 'Network Connectivity Issue', 'WARNING', 1),
(2, 'Software Update', 'INFO', 2),
(3, 'Cash Dispenser Malfunction', 'ERROR', 3),
(4, 'Paper Refill Required', 'INFO', 4),
(5, 'Card Reader Error', 'ERROR', 5),
(6, 'Application Error', 'ERROR', 6),
(7, 'ATM Communication Loss', 'CRITICAL', 7),
(8, 'System Log Rotation', 'INFO', 8),
(9, 'Scheduled Maintenance', 'INFO', 9),
(10, 'Suspicious Activity Detected', 'CRITICAL', 10);

-- Insert data into Groups table
INSERT INTO Group (groupId, groupName, groupDescription, groupType) VALUES
(1, 'Hardware Issues', 'ATMs in this group are experiencing various hardware malfunctions...', 'Dynamic'),
(2, 'Network Connectivity Issues', 'ATMs in this group are unable to communicate with the central network...', 'Dynamic'),
(3, 'Software Glitches', 'ATMs in this group are exhibiting software-related issues...', 'Dynamic'),
(4, 'Environmental Sensor Alerts', 'ATMs in this group have reported sensor readings exceeding recommended thresholds...', 'Dynamic');


-- Insert data into Transaction table
INSERT INTO Transaction (transactionId, transactionType, transactionDetail, ejId) VALUES
(1, 'Cash Withdrawal', 'Account: 12345678, Amount: $200, ATM: 123', 1),
(2, 'Balance Inquiry', 'Account: 87654321, ATM: 456', 2),
(3, 'Deposit', 'Account: 98765432, Amount: $500, Bill denominations: 20x $20', 3),
(4, 'Transfer', 'From account: 12345678, To account: 87654321, Amount: $100', 4),
(5, 'Card Payment', 'Merchant: ABC Store, Amount: $35.78, Card number: XXXX-XXXX-XXXX-1234', 5),
(6, 'PIN Change', NULL), -- Set "transactionDetail" to NULL for PIN Change
(7, 'Failed Transaction', 'Reason: Insufficient funds, Account: 87654321, ATM: 234', 7),
(8, 'Account Lockout', 'Reason: Invalid PIN attempts, Account: 12345678', 8),
(9, 'Service Request', 'Request type: Mini statement, Account: 98765432', 9),
(10, 'System Maintenance', 'Description: ATM software update', 10);


-- Insert data into ATM table (assuming atmName is not used)
INSERT INTO ATM (atmId, atmName, networkAddress, latitude, longitude, timezone, subnet, branchId, groupId, status, cash_level, last_cash_replenishment, software_version, uptime) VALUES
(1, 'ATM 1 - Main Branch', '192.168.1.10', 34.05223, -118.24368, '2024-03-05T12:00:00Z', '255.255.255.0', 1, 1, 'Online', 10000.00, '2024-02-22T10:00:00Z', 'v1.2.3', 36000),
(2, 'ATM 2 - City Center', '192.168.2.20', 34.06862, -118.33524, '2024-03-05T12:00:00Z', '255.255.255.0', 2, 2, 'Offline', 5000.00, '2024-02-15T09:00:00Z', 'v1.1.5', 0),
(3, 'ATM 3 - Airport', '172.16.0.30', 34.04167, -118.24368, '2024-03-05T12:00:00Z', '255.255.0.0', 3, 1, 'Under Maintenance', 7500.00, '2024-03-04T15:00:00Z', 'v1.2.1', 14400),
(4, 'ATM 4 - University Branch', '10.0.1.10', 34.06528, -118.24368, '2024-03-05T12:00:00Z', '255.255.255.0', 5, 3, 'Online', 8000.00, '2024-02-29T14:00:00Z', 'v1.3.0', 86400),
(5, 'ATM 5 - East Branch', '192.168.3.30', 34.08118, -118.29073, '2024-03-05T12:00:00Z', '255.255.255.0', 2, 4, 'Online', 6000.00, '2024-03-02T16:00:00Z', 'v1.1.7', 36000),
(6, 'ATM 6 - Shopping Mall', '172.16.1.50', 34.05820, -118.25860, '2024-03-05T12:00:00Z', '255.255.0.0', 1, 2, 'Offline', 4000.00, '2024-02-20T12:00:00Z', 'v1.2.2', 0),
(7, 'ATM 7 - Hospital', '10.10.1.20', 34.07416, -118.31322, '2024-03-05T12:00:00Z', '255.255.255.0', 4, 3, 'Under Maintenance', 9000.00, '2024-03-01T10:00:00Z', 'v1.3.1', 28800);
