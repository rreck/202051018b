```json
{
  "id": "bea94a32d5d03ed0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293936,
  "host_pid": "9e6742732c60:1",
  "hash": "d614ffedd563019a474521de40959da6164205d9b7be1234bbdb750ea9ea46db",
  "cid": "QmV1d614ffedd563019a474521de40959da6164205d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293936,
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
      "evaluated_at": 1760293936
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
  "sig": "c8e7bd8b6a727a6ce88c3a8e459f5c0d5100e1519b1c1405876ff6c5cbe3a34d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246289995
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 23874336, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285764, 'matching_hash': '1ab4d10c626d0dd7'}}}