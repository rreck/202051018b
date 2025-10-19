```json
{
  "id": "13a6b116a3110a02",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294412,
  "host_pid": "9e6742732c60:1",
  "hash": "48a26559e8a864d39f3b5ce1c921d755fe50a3d6712c4a2b8163ebb0280291dc",
  "cid": "QmV148a26559e8a864d39f3b5ce1c921d755fe50a3d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294412,
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
      "evaluated_at": 1760294412
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
  "sig": "790e30c3d8fb5ceaa210a79f55db7911b258468c8fb35127e031e068709455d3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034020503
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 11850000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285765, 'matching_hash': '8db66b2beb557931'}}}