#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Copyright (c) RRECKTEK LLC
# Project: CrewAI Fraud Detection Agent - ACH/NACHA Schema Module
# Version: 1.0.0
#
# Purpose:
#   ACH/NACHA file format parser and generator. Supports fixed-width 94-char
#   records conforming to NACHA specifications with all record types:
#   - Type 1: File Header
#   - Type 5: Batch Header
#   - Type 6: Entry Detail
#   - Type 7: Addenda
#   - Type 8: Batch Control
#   - Type 9: File Control
#
#   Includes validation for routing number checksums, transaction codes,
#   and field formatting.
# -----------------------------------------------------------------------------

import re
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import hashlib


class ACHRecordType:
    """NACHA record type constants"""
    FILE_HEADER = '1'
    BATCH_HEADER = '5'
    ENTRY_DETAIL = '6'
    ADDENDA = '7'
    BATCH_CONTROL = '8'
    FILE_CONTROL = '9'


class TransactionCode:
    """NACHA transaction code constants"""
    CHECKING_CREDIT = '22'
    CHECKING_DEBIT = '27'
    CHECKING_PRENOTE_CREDIT = '23'
    CHECKING_PRENOTE_DEBIT = '28'
    SAVINGS_CREDIT = '32'
    SAVINGS_DEBIT = '37'
    SAVINGS_PRENOTE_CREDIT = '33'
    SAVINGS_PRENOTE_DEBIT = '38'

    ALL_CODES = ['22', '27', '23', '28', '32', '37', '33', '38']
    DEBIT_CODES = ['27', '28', '37', '38']
    CREDIT_CODES = ['22', '23', '32', '33']


class ServiceClassCode:
    """NACHA service class code constants"""
    MIXED = '200'  # Mixed debits and credits
    CREDITS_ONLY = '220'
    DEBITS_ONLY = '225'
    AUTOMATED_ACCOUNTING_ADVICES = '280'


class StandardEntryClassCode:
    """NACHA standard entry class codes"""
    PPD = 'PPD'  # Prearranged Payment and Deposit
    CCD = 'CCD'  # Corporate Credit or Debit
    CTX = 'CTX'  # Corporate Trade Exchange
    WEB = 'WEB'  # Internet-Initiated Entry
    TEL = 'TEL'  # Telephone-Initiated Entry
    POS = 'POS'  # Point of Sale

    ALL_CODES = ['PPD', 'CCD', 'CTX', 'WEB', 'TEL', 'POS']


def validate_routing_number(routing: str) -> bool:
    """
    Validate ABA routing number using checksum algorithm.
    Formula: 3*(d1+d4+d7) + 7*(d2+d5+d8) + (d3+d6+d9) mod 10 = 0
    """
    if not routing or len(routing) != 9 or not routing.isdigit():
        return False

    digits = [int(d) for d in routing]
    checksum = (
        3 * (digits[0] + digits[3] + digits[6]) +
        7 * (digits[1] + digits[4] + digits[7]) +
        (digits[2] + digits[5] + digits[8])
    )
    return checksum % 10 == 0


def generate_routing_number(valid: bool = True) -> str:
    """Generate a routing number (valid or invalid based on param)"""
    if valid:
        # Use known valid routing numbers
        valid_routings = [
            '121000248',  # Wells Fargo
            '026009593',  # Bank of America
            '122105155',  # Union Bank
            '111000025',  # Federal Reserve Bank
            '021000021',  # JP Morgan Chase
            '031201467',  # Citibank
            '044000037',  # PNC Bank
            '063100277',  # BB&T
        ]
        return random.choice(valid_routings)
    else:
        # Generate invalid routing number
        routing = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        # Make sure it's actually invalid
        while validate_routing_number(routing):
            routing = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        return routing


class ACHRecord:
    """Base class for ACH records"""

    def __init__(self, record_type: str):
        self.record_type = record_type

    def to_nacha(self) -> str:
        """Convert to NACHA fixed-width format (94 chars)"""
        raise NotImplementedError

    @staticmethod
    def pad_left(value: str, length: int, char: str = '0') -> str:
        """Left-pad string to length"""
        return str(value).rjust(length, char)[:length]

    @staticmethod
    def pad_right(value: str, length: int, char: str = ' ') -> str:
        """Right-pad string to length"""
        return str(value).ljust(length, char)[:length]


class FileHeaderRecord(ACHRecord):
    """Type 1: File Header Record"""

    def __init__(self,
                 immediate_destination: str = '091000019',
                 immediate_origin: str = '091000019',
                 file_creation_date: Optional[str] = None,
                 file_creation_time: Optional[str] = None,
                 file_id_modifier: str = 'A',
                 immediate_destination_name: str = 'RECEIVING BANK',
                 immediate_origin_name: str = 'ORIGINATING BANK',
                 reference_code: str = ''):
        super().__init__(ACHRecordType.FILE_HEADER)
        self.immediate_destination = immediate_destination
        self.immediate_origin = immediate_origin
        self.file_creation_date = file_creation_date or datetime.now().strftime('%y%m%d')
        self.file_creation_time = file_creation_time or datetime.now().strftime('%H%M')
        self.file_id_modifier = file_id_modifier
        self.immediate_destination_name = immediate_destination_name
        self.immediate_origin_name = immediate_origin_name
        self.reference_code = reference_code

    def to_nacha(self) -> str:
        """Generate 94-character file header record"""
        parts = [
            '1',  # Record Type Code
            '01',  # Priority Code
            self.pad_left(self.immediate_destination, 10),  # Immediate Destination
            self.pad_left(self.immediate_origin, 10),  # Immediate Origin
            self.file_creation_date,  # File Creation Date (YYMMDD)
            self.file_creation_time,  # File Creation Time (HHMM)
            self.file_id_modifier,  # File ID Modifier
            '094',  # Record Size
            '10',  # Blocking Factor
            '1',  # Format Code
            self.pad_right(self.immediate_destination_name, 23),  # Immediate Destination Name
            self.pad_right(self.immediate_origin_name, 23),  # Immediate Origin Name
            self.pad_right(self.reference_code, 8),  # Reference Code
        ]
        return ''.join(parts)


class BatchHeaderRecord(ACHRecord):
    """Type 5: Batch Header Record"""

    def __init__(self,
                 service_class_code: str = ServiceClassCode.MIXED,
                 company_name: str = 'COMPANY NAME',
                 company_discretionary_data: str = '',
                 company_id: str = '1234567890',
                 sec_code: str = StandardEntryClassCode.PPD,
                 company_entry_description: str = 'PAYROLL',
                 company_descriptive_date: str = '',
                 effective_entry_date: Optional[str] = None,
                 originating_dfi_id: str = '12345678',
                 batch_number: int = 1):
        super().__init__(ACHRecordType.BATCH_HEADER)
        self.service_class_code = service_class_code
        self.company_name = company_name
        self.company_discretionary_data = company_discretionary_data
        self.company_id = company_id
        self.sec_code = sec_code
        self.company_entry_description = company_entry_description
        self.company_descriptive_date = company_descriptive_date
        self.effective_entry_date = effective_entry_date or (datetime.now() + timedelta(days=1)).strftime('%y%m%d')
        self.originating_dfi_id = originating_dfi_id
        self.batch_number = batch_number

    def to_nacha(self) -> str:
        """Generate 94-character batch header record"""
        parts = [
            '5',  # Record Type Code
            self.service_class_code,  # Service Class Code
            self.pad_right(self.company_name, 16),  # Company Name
            self.pad_right(self.company_discretionary_data, 20),  # Company Discretionary Data
            self.pad_right(self.company_id, 10),  # Company Identification
            self.sec_code,  # Standard Entry Class Code
            self.pad_right(self.company_entry_description, 10),  # Company Entry Description
            self.pad_right(self.company_descriptive_date, 6),  # Company Descriptive Date
            self.effective_entry_date,  # Effective Entry Date
            '   ',  # Settlement Date (Julian)
            '1',  # Originator Status Code
            self.originating_dfi_id,  # Originating DFI Identification
            self.pad_left(str(self.batch_number), 7),  # Batch Number
        ]
        return ''.join(parts)


class EntryDetailRecord(ACHRecord):
    """Type 6: Entry Detail Record"""

    def __init__(self,
                 transaction_code: str = TransactionCode.CHECKING_CREDIT,
                 receiving_dfi_routing: str = '121000248',
                 receiving_dfi_account: str = '123456789',
                 amount: int = 0,  # In cents
                 individual_id: str = '',
                 individual_name: str = 'RECEIVER NAME',
                 discretionary_data: str = '',
                 addenda_indicator: str = '0',
                 trace_number: Optional[str] = None):
        super().__init__(ACHRecordType.ENTRY_DETAIL)
        self.transaction_code = transaction_code
        self.receiving_dfi_routing = receiving_dfi_routing
        self.receiving_dfi_account = receiving_dfi_account
        self.amount = amount
        self.individual_id = individual_id
        self.individual_name = individual_name
        self.discretionary_data = discretionary_data
        self.addenda_indicator = addenda_indicator
        self.trace_number = trace_number or self._generate_trace_number()

    def _generate_trace_number(self) -> str:
        """Generate a trace number (8 digits routing + 7 digit sequence)"""
        routing_prefix = self.receiving_dfi_routing[:8]
        sequence = str(random.randint(1, 9999999))
        return routing_prefix + self.pad_left(sequence, 7)

    def to_nacha(self) -> str:
        """Generate 94-character entry detail record"""
        check_digit = self.receiving_dfi_routing[8] if len(self.receiving_dfi_routing) == 9 else '0'
        parts = [
            '6',  # Record Type Code
            self.transaction_code,  # Transaction Code
            self.receiving_dfi_routing[:8],  # Receiving DFI Identification
            check_digit,  # Check Digit
            self.pad_right(self.receiving_dfi_account, 17),  # DFI Account Number
            self.pad_left(str(self.amount), 10),  # Amount
            self.pad_right(self.individual_id, 15),  # Individual Identification Number
            self.pad_right(self.individual_name, 22),  # Individual Name
            self.pad_right(self.discretionary_data, 2),  # Discretionary Data
            self.addenda_indicator,  # Addenda Record Indicator
            self.pad_right(self.trace_number, 15),  # Trace Number
        ]
        return ''.join(parts)


class AddendaRecord(ACHRecord):
    """Type 7: Addenda Record"""

    def __init__(self,
                 addenda_type_code: str = '05',
                 payment_related_info: str = '',
                 addenda_sequence_number: int = 1,
                 entry_detail_sequence_number: int = 1):
        super().__init__(ACHRecordType.ADDENDA)
        self.addenda_type_code = addenda_type_code
        self.payment_related_info = payment_related_info
        self.addenda_sequence_number = addenda_sequence_number
        self.entry_detail_sequence_number = entry_detail_sequence_number

    def to_nacha(self) -> str:
        """Generate 94-character addenda record"""
        parts = [
            '7',  # Record Type Code
            self.addenda_type_code,  # Addenda Type Code
            self.pad_right(self.payment_related_info, 80),  # Payment Related Information
            self.pad_left(str(self.addenda_sequence_number), 4),  # Addenda Sequence Number
            self.pad_left(str(self.entry_detail_sequence_number), 7),  # Entry Detail Sequence Number
        ]
        return ''.join(parts)


class BatchControlRecord(ACHRecord):
    """Type 8: Batch Control Record"""

    def __init__(self,
                 service_class_code: str = ServiceClassCode.MIXED,
                 entry_addenda_count: int = 0,
                 entry_hash: int = 0,
                 total_debit: int = 0,
                 total_credit: int = 0,
                 company_id: str = '1234567890',
                 originating_dfi_id: str = '12345678',
                 batch_number: int = 1):
        super().__init__(ACHRecordType.BATCH_CONTROL)
        self.service_class_code = service_class_code
        self.entry_addenda_count = entry_addenda_count
        self.entry_hash = entry_hash
        self.total_debit = total_debit
        self.total_credit = total_credit
        self.company_id = company_id
        self.originating_dfi_id = originating_dfi_id
        self.batch_number = batch_number

    def to_nacha(self) -> str:
        """Generate 94-character batch control record"""
        parts = [
            '8',  # Record Type Code
            self.service_class_code,  # Service Class Code
            self.pad_left(str(self.entry_addenda_count), 6),  # Entry/Addenda Count
            self.pad_left(str(self.entry_hash), 10),  # Entry Hash
            self.pad_left(str(self.total_debit), 12),  # Total Debit Entry Dollar Amount
            self.pad_left(str(self.total_credit), 12),  # Total Credit Entry Dollar Amount
            self.pad_right(self.company_id, 10),  # Company Identification
            '                   ',  # Message Authentication Code (19 spaces)
            '      ',  # Reserved (6 spaces)
            self.originating_dfi_id,  # Originating DFI Identification
            self.pad_left(str(self.batch_number), 7),  # Batch Number
        ]
        return ''.join(parts)


class FileControlRecord(ACHRecord):
    """Type 9: File Control Record"""

    def __init__(self,
                 batch_count: int = 0,
                 block_count: int = 0,
                 entry_addenda_count: int = 0,
                 entry_hash: int = 0,
                 total_debit: int = 0,
                 total_credit: int = 0):
        super().__init__(ACHRecordType.FILE_CONTROL)
        self.batch_count = batch_count
        self.block_count = block_count
        self.entry_addenda_count = entry_addenda_count
        self.entry_hash = entry_hash
        self.total_debit = total_debit
        self.total_credit = total_credit

    def to_nacha(self) -> str:
        """Generate 94-character file control record"""
        parts = [
            '9',  # Record Type Code
            self.pad_left(str(self.batch_count), 6),  # Batch Count
            self.pad_left(str(self.block_count), 6),  # Block Count
            self.pad_left(str(self.entry_addenda_count), 8),  # Entry/Addenda Count
            self.pad_left(str(self.entry_hash), 10),  # Entry Hash
            self.pad_left(str(self.total_debit), 12),  # Total Debit Entry Dollar Amount
            self.pad_left(str(self.total_credit), 12),  # Total Credit Entry Dollar Amount
            ' ' * 39,  # Reserved (39 spaces)
        ]
        return ''.join(parts)


class ACHFile:
    """Complete ACH file with all record types"""

    def __init__(self,
                 immediate_destination: str = '091000019',
                 immediate_origin: str = '091000019',
                 immediate_destination_name: str = 'RECEIVING BANK',
                 immediate_origin_name: str = 'ORIGINATING BANK'):
        self.file_header = FileHeaderRecord(
            immediate_destination=immediate_destination,
            immediate_origin=immediate_origin,
            immediate_destination_name=immediate_destination_name,
            immediate_origin_name=immediate_origin_name
        )
        self.batches: List[ACHBatch] = []

    def add_batch(self, batch: 'ACHBatch'):
        """Add a batch to the file"""
        self.batches.append(batch)

    def to_nacha(self) -> str:
        """Generate complete NACHA file"""
        lines = [self.file_header.to_nacha()]

        total_entry_count = 0
        total_entry_hash = 0
        total_debit = 0
        total_credit = 0

        for batch in self.batches:
            batch_lines = batch.to_nacha_lines()
            lines.extend(batch_lines)

            # Accumulate totals
            total_entry_count += batch.entry_count
            total_entry_hash += batch.entry_hash
            total_debit += batch.total_debit
            total_credit += batch.total_credit

        # Calculate block count (round up to nearest 10)
        total_records = len(lines) + 1  # +1 for file control
        block_count = ((total_records + 9) // 10) * 10 // 10

        # Add file control record
        file_control = FileControlRecord(
            batch_count=len(self.batches),
            block_count=block_count,
            entry_addenda_count=total_entry_count,
            entry_hash=total_entry_hash % 10000000000,  # Keep last 10 digits
            total_debit=total_debit,
            total_credit=total_credit
        )
        lines.append(file_control.to_nacha())

        # Pad to block size (multiple of 10 records)
        while len(lines) % 10 != 0:
            lines.append('9' * 94)

        return '\n'.join(lines)

    def compute_hash(self) -> str:
        """Compute SHA256 hash of the ACH file content"""
        content = self.to_nacha()
        return hashlib.sha256(content.encode('utf-8')).hexdigest()


class ACHBatch:
    """ACH batch with header, entries, and control"""

    def __init__(self,
                 service_class_code: str = ServiceClassCode.MIXED,
                 company_name: str = 'COMPANY NAME',
                 company_id: str = '1234567890',
                 sec_code: str = StandardEntryClassCode.PPD,
                 company_entry_description: str = 'PAYROLL',
                 originating_dfi_id: str = '12345678',
                 batch_number: int = 1):
        self.batch_header = BatchHeaderRecord(
            service_class_code=service_class_code,
            company_name=company_name,
            company_id=company_id,
            sec_code=sec_code,
            company_entry_description=company_entry_description,
            originating_dfi_id=originating_dfi_id,
            batch_number=batch_number
        )
        self.entries: List[Tuple[EntryDetailRecord, Optional[AddendaRecord]]] = []
        self.entry_count = 0
        self.entry_hash = 0
        self.total_debit = 0
        self.total_credit = 0

    def add_entry(self, entry: EntryDetailRecord, addenda: Optional[AddendaRecord] = None):
        """Add an entry detail record (and optional addenda) to the batch"""
        self.entries.append((entry, addenda))

        # Update counts and totals
        self.entry_count += 1
        if addenda:
            self.entry_count += 1

        # Update entry hash (sum of first 8 digits of routing numbers)
        routing_num = int(entry.receiving_dfi_routing[:8])
        self.entry_hash += routing_num

        # Update debit/credit totals
        if entry.transaction_code in TransactionCode.DEBIT_CODES:
            self.total_debit += entry.amount
        else:
            self.total_credit += entry.amount

    def to_nacha_lines(self) -> List[str]:
        """Generate all NACHA lines for this batch"""
        lines = [self.batch_header.to_nacha()]

        for entry, addenda in self.entries:
            lines.append(entry.to_nacha())
            if addenda:
                lines.append(addenda.to_nacha())

        # Add batch control record
        batch_control = BatchControlRecord(
            service_class_code=self.batch_header.service_class_code,
            entry_addenda_count=self.entry_count,
            entry_hash=self.entry_hash % 10000000000,  # Keep last 10 digits
            total_debit=self.total_debit,
            total_credit=self.total_credit,
            company_id=self.batch_header.company_id,
            originating_dfi_id=self.batch_header.originating_dfi_id,
            batch_number=self.batch_header.batch_number
        )
        lines.append(batch_control.to_nacha())

        return lines


class ACHParser:
    """Parse NACHA format ACH files"""

    @staticmethod
    def parse_file(content: str) -> Dict:
        """Parse NACHA file content into structured data"""
        lines = content.strip().split('\n')
        result = {
            'file_header': None,
            'batches': [],
            'file_control': None,
            'errors': []
        }

        current_batch = None

        for line_num, line in enumerate(lines, 1):
            if len(line) != 94:
                result['errors'].append(f"Line {line_num}: Invalid length {len(line)} (expected 94)")
                continue

            record_type = line[0]

            try:
                if record_type == ACHRecordType.FILE_HEADER:
                    result['file_header'] = ACHParser._parse_file_header(line)

                elif record_type == ACHRecordType.BATCH_HEADER:
                    if current_batch:
                        result['batches'].append(current_batch)
                    current_batch = {
                        'batch_header': ACHParser._parse_batch_header(line),
                        'entries': [],
                        'batch_control': None
                    }

                elif record_type == ACHRecordType.ENTRY_DETAIL:
                    if current_batch:
                        current_batch['entries'].append({
                            'entry': ACHParser._parse_entry_detail(line),
                            'addenda': None
                        })

                elif record_type == ACHRecordType.ADDENDA:
                    if current_batch and current_batch['entries']:
                        current_batch['entries'][-1]['addenda'] = ACHParser._parse_addenda(line)

                elif record_type == ACHRecordType.BATCH_CONTROL:
                    if current_batch:
                        current_batch['batch_control'] = ACHParser._parse_batch_control(line)

                elif record_type == ACHRecordType.FILE_CONTROL:
                    if current_batch:
                        result['batches'].append(current_batch)
                        current_batch = None
                    result['file_control'] = ACHParser._parse_file_control(line)

            except Exception as e:
                result['errors'].append(f"Line {line_num}: Parse error - {str(e)}")

        return result

    @staticmethod
    def _parse_file_header(line: str) -> Dict:
        return {
            'record_type': line[0:1],
            'priority_code': line[1:3],
            'immediate_destination': line[3:13].strip(),
            'immediate_origin': line[13:23].strip(),
            'file_creation_date': line[23:29],
            'file_creation_time': line[29:33],
            'file_id_modifier': line[33:34],
            'record_size': line[34:37],
            'blocking_factor': line[37:39],
            'format_code': line[39:40],
            'immediate_destination_name': line[40:63].strip(),
            'immediate_origin_name': line[63:86].strip(),
            'reference_code': line[86:94].strip()
        }

    @staticmethod
    def _parse_batch_header(line: str) -> Dict:
        return {
            'record_type': line[0:1],
            'service_class_code': line[1:4],
            'company_name': line[4:20].strip(),
            'company_discretionary_data': line[20:40].strip(),
            'company_id': line[40:50].strip(),
            'sec_code': line[50:53].strip(),
            'company_entry_description': line[53:63].strip(),
            'company_descriptive_date': line[63:69].strip(),
            'effective_entry_date': line[69:75],
            'settlement_date': line[75:78],
            'originator_status_code': line[78:79],
            'originating_dfi_id': line[79:87],
            'batch_number': int(line[87:94])
        }

    @staticmethod
    def _parse_entry_detail(line: str) -> Dict:
        return {
            'record_type': line[0:1],
            'transaction_code': line[1:3],
            'receiving_dfi_routing': line[3:11] + line[11:12],  # Include check digit
            'receiving_dfi_account': line[12:29].strip(),
            'amount': int(line[29:39]),
            'individual_id': line[39:54].strip(),
            'individual_name': line[54:76].strip(),
            'discretionary_data': line[76:78].strip(),
            'addenda_indicator': line[78:79],
            'trace_number': line[79:94].strip()
        }

    @staticmethod
    def _parse_addenda(line: str) -> Dict:
        return {
            'record_type': line[0:1],
            'addenda_type_code': line[1:3],
            'payment_related_info': line[3:83].strip(),
            'addenda_sequence_number': int(line[83:87]),
            'entry_detail_sequence_number': int(line[87:94])
        }

    @staticmethod
    def _parse_batch_control(line: str) -> Dict:
        return {
            'record_type': line[0:1],
            'service_class_code': line[1:4],
            'entry_addenda_count': int(line[4:10]),
            'entry_hash': int(line[10:20]),
            'total_debit': int(line[20:32]),
            'total_credit': int(line[32:44]),
            'company_id': line[44:54].strip(),
            'message_authentication_code': line[54:73].strip(),
            'reserved': line[73:79],
            'originating_dfi_id': line[79:87],
            'batch_number': int(line[87:94])
        }

    @staticmethod
    def _parse_file_control(line: str) -> Dict:
        return {
            'record_type': line[0:1],
            'batch_count': int(line[1:7]),
            'block_count': int(line[7:13]),
            'entry_addenda_count': int(line[13:21]),
            'entry_hash': int(line[21:31]),
            'total_debit': int(line[31:43]),
            'total_credit': int(line[43:55]),
            'reserved': line[55:94]
        }
