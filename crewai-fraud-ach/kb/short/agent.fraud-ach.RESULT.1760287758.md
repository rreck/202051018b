```json
{
  "id": "36d2085d8c04f1ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287758,
  "host_pid": "9e6742732c60:1",
  "hash": "4840e6cc909db1f59a4e9f7f02a230d14ae6106db4aa8474520ac3e97bd0e511",
  "cid": "QmV14840e6cc909db1f59a4e9f7f02a230d14ae6106d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287758,
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
      "evaluated_at": 1760287758
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
  "sig": "dd574cc9e01becf0552a394923d6d9912d124a5faf6d91055462599de38f3d2f"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 122105152430853
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285764, 'matching_hash': 'fa17beca2cfad33c'}}}