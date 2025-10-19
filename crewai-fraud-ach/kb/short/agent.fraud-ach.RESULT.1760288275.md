```json
{
  "id": "a8741b5e30b6c5de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288275,
  "host_pid": "9e6742732c60:1",
  "hash": "dfdeebc8b2d2308bacef53f5f4024ebcefb00d081ed84fa11aab8010efdc58d9",
  "cid": "QmV1dfdeebc8b2d2308bacef53f5f4024ebcefb00d08",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288275,
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
      "evaluated_at": 1760288275
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
  "sig": "477ca9921baa6d732cb5e4d199fba6592007f4d64c2aafdbd5fd393d975d446b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244947778
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 26117080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285763, 'matching_hash': '9c8f06e6a18eec99'}}}