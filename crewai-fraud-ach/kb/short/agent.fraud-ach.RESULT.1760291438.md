```json
{
  "id": "32f0a2bc297f7e0c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291438,
  "host_pid": "9e6742732c60:1",
  "hash": "b6373816abcf2ef22e9a4b69ad6df53ea3b60328db3cb388b54ca7cd401e0484",
  "cid": "QmV1b6373816abcf2ef22e9a4b69ad6df53ea3b60328",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291438,
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
      "evaluated_at": 1760291438
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
  "sig": "ed954dd47989c08897aa637f3d6ae42c51c72cb956c01f07a7190f4af4cb3e9b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592648645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 66186225, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': 'd7971b176fb0516b'}}}