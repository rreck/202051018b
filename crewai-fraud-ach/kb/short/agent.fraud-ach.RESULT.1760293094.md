```json
{
  "id": "f2630e06f7a2bcff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293094,
  "host_pid": "9e6742732c60:1",
  "hash": "e0c605f62cdc51d7c4cdc505103a6ab747b214aa11ba6d9df97a8fed535bbeac",
  "cid": "QmV1e0c605f62cdc51d7c4cdc505103a6ab747b214aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293094,
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
      "evaluated_at": 1760293094
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
  "sig": "49730f09d1affebd0c9e131be298890772c64e4b4be1b95acd6d235a198c8b18"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279234721
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 48616932, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285764, 'matching_hash': 'a4a7a8ef6540eadb'}}}