```json
{
  "id": "4c342e1451c4199c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290208,
  "host_pid": "9e6742732c60:1",
  "hash": "b034b2c674d2523d46a1e155c1640d46edd3234535fc91a5e4ca57ccd3bf2919",
  "cid": "QmV1b034b2c674d2523d46a1e155c1640d46edd32345",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290208,
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
      "evaluated_at": 1760290208
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
  "sig": "7edd1de60622c7ea7d1090182f511b16f3904f4e97035b495eb80bd857446edd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460644681
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 49141872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285764, 'matching_hash': '02c671505c0a8698'}}}