```json
{
  "id": "0f86688ba713c9be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290194,
  "host_pid": "9e6742732c60:1",
  "hash": "21ee0bb9e75659b5c44d6625fd05c1aa7e8a98ed47cef408800bb1d51369624d",
  "cid": "QmV121ee0bb9e75659b5c44d6625fd05c1aa7e8a98ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290194,
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
      "evaluated_at": 1760290194
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
  "sig": "a0a84fe59db1165f6b99395fb6c49f29c84bcd15599f598a67860d8d5920b4a7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597385398
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 35183088, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285763, 'matching_hash': '354842811986f77e'}}}