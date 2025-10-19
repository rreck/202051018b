```json
{
  "id": "59756654ff1b497f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288088,
  "host_pid": "9e6742732c60:1",
  "hash": "1aa5e12ff7a4d5bc93df5b8383c5e8d12ee19296f01288db02250b28e7cf2333",
  "cid": "QmV11aa5e12ff7a4d5bc93df5b8383c5e8d12ee19296",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288088,
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
      "evaluated_at": 1760288088
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
  "sig": "420787710cc47352bd7ae03cc4446252e16845a5c1c919a1c1b7ad7f27828362"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024765233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 27966756, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285763, 'matching_hash': 'feb1cc4bc40c71bc'}}}