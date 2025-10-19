```json
{
  "id": "41bcb2042d2bc662",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287327,
  "host_pid": "9e6742732c60:1",
  "hash": "6bdba1fd719ece5bd98a5be1548575da2b32b6b6d98868c7e74ca7280850ea77",
  "cid": "QmV16bdba1fd719ece5bd98a5be1548575da2b32b6b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287327,
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
      "evaluated_at": 1760287327
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
  "sig": "6a05c91dd9d4b76f3686afd93a0bc7edd1dbb680e1a4b9b5a8c27041734fe5de"
}
```

Fraud detected: duplicate_transaction (score: 73)
Transaction: 044000038607326
Details: {'velocity': {'fraud_detected': True, 'risk_score': 62, 'details': {'transaction_count': 56, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285763, 'matching_hash': '23e85c6499cf881c'}}}