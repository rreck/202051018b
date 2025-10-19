```json
{
  "id": "cad02d663e665376",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293147,
  "host_pid": "9e6742732c60:1",
  "hash": "f6d61a147500b7e3da0cea023aedf955c86a18a1e1cd63c464351b3ab7ff8a0b",
  "cid": "QmV1f6d61a147500b7e3da0cea023aedf955c86a18a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293147,
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
      "evaluated_at": 1760293147
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
  "sig": "8637002331d5cf45ed62f3ef99d6f52f0d9bc4a971f87a3ca982507c5e268cf7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021597485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 57206504, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285765, 'matching_hash': '53d96e948794c738'}}}