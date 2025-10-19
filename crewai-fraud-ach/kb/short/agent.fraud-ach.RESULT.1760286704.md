```json
{
  "id": "7f7df1b0bb0098b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286704,
  "host_pid": "9e6742732c60:1",
  "hash": "bb13dd23053d0726b7170a23763e22828e7f4e2c716dea6aaa4a9fefbfc55a99",
  "cid": "QmV1bb13dd23053d0726b7170a23763e22828e7f4e2c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286704,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760286704
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "6bd231cf7eeb7e774266d583296fab8b36ef863d0662d8d414c154f636edb194"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009597956116
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12487180, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285764, 'matching_hash': '37dac3adff3764b9'}}}