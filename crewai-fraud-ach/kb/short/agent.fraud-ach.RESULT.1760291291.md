```json
{
  "id": "ad1ba464c38dca0e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291291,
  "host_pid": "9e6742732c60:1",
  "hash": "9d074fc737f22c08c1dde1f8d36515fec83c63c4a43b35082e03629607fc4c0d",
  "cid": "QmV19d074fc737f22c08c1dde1f8d36515fec83c63c4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291291,
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
      "evaluated_at": 1760291291
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
  "sig": "316aad053f191042b49c4ee061f5211f9596bf67f757b396779e130b5c949f95"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028263855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 42750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285765, 'matching_hash': 'de539bef65b21552'}}}