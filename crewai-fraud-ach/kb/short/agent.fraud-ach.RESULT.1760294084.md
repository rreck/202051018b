```json
{
  "id": "ccf0be1418e747db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294084,
  "host_pid": "9e6742732c60:1",
  "hash": "92a8cd1c8d01424e08ad24abc09b02a7c70d828520a4d4d6060d037ec22aa06f",
  "cid": "QmV192a8cd1c8d01424e08ad24abc09b02a7c70d8285",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294084,
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
      "evaluated_at": 1760294084
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
  "sig": "94b374a1349147c87574b4d2ac15d7cafe39064ae542307424c59772a23ad14b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021533630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 34052634, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285765, 'matching_hash': 'e04be99e47eedc93'}}}