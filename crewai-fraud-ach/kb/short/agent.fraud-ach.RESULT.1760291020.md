```json
{
  "id": "107d663321f7e118",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291020,
  "host_pid": "9e6742732c60:1",
  "hash": "27df1aeb378d61ac07477ecef3a7b09e10f2c4dff6ee983ca1c2d6736fcd2278",
  "cid": "QmV127df1aeb378d61ac07477ecef3a7b09e10f2c4df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291020,
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
      "evaluated_at": 1760291020
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
  "sig": "c4727f796615fbf7af2f54f086dda39bcd1fe40c49777dd126a07d9f81981caf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249268740
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 12801690, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': '2b1c4c9f55d7dd69'}}}