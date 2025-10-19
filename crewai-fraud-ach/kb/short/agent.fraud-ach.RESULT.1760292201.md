```json
{
  "id": "a7abc5ef253a8c1c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292201,
  "host_pid": "9e6742732c60:1",
  "hash": "ab2fda48c9cecf6753ca5498b2afc3c63e5b90f367325ed26009983bc33d55b7",
  "cid": "QmV1ab2fda48c9cecf6753ca5498b2afc3c63e5b90f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292201,
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
      "evaluated_at": 1760292201
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
  "sig": "676fe0c70ab3357adf5a296f9d366934a533ffa2da4e57fd1e19e48f5d7442c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464452578
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 18490944, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285764, 'matching_hash': '0a8d6c8cd4d67655'}}}