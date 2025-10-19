```json
{
  "id": "41c082e7b4c7719d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290666,
  "host_pid": "9e6742732c60:1",
  "hash": "4a2d83ad12e2a5192bf9381f892f5edca20e2d64cb77a9418cec09ca3bb9c3df",
  "cid": "QmV14a2d83ad12e2a5192bf9381f892f5edca20e2d64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290666,
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
      "evaluated_at": 1760290666
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "98d9d2e8257dd18c6255b01c18256a20c837410026697938a022267ebeef3a31"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596082668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 49896008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760284979, 'matching_hash': '3a96bbca6babd2b6'}}}