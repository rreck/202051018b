```json
{
  "id": "cab648987ba87349",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290053,
  "host_pid": "9e6742732c60:1",
  "hash": "d59269458b160ea04f86a78f1fa8c9446b570998962267a8c804598201b51108",
  "cid": "QmV1d59269458b160ea04f86a78f1fa8c9446b570998",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290053,
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
      "evaluated_at": 1760290053
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
  "sig": "50b950eee3acd6a1c28b4864814a97900e4e7934e3077c504c6126e7fa5c792f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021533630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 20637960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285765, 'matching_hash': 'e04be99e47eedc93'}}}