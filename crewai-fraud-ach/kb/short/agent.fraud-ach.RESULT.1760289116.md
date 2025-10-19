```json
{
  "id": "ca872fdc5744fe16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289116,
  "host_pid": "9e6742732c60:1",
  "hash": "9f160924a3d8b92ab6f2784234cfe21fc2a6a6963083657d6a8a6ac5cc90376c",
  "cid": "QmV19f160924a3d8b92ab6f2784234cfe21fc2a6a696",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289116,
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
      "evaluated_at": 1760289116
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
  "sig": "9a9b34c73fc03fa311c3e3a7117af7d390d2f7d7cf6cc4144542cfc06bcba5e8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028779608
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 34311264, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285763, 'matching_hash': 'f4a7019387fd02e9'}}}