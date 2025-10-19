```json
{
  "id": "fea938edcf6a1c79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291544,
  "host_pid": "9e6742732c60:1",
  "hash": "c94a181fae93edf12f8419c85334d267483383e9fd3d8f18971bbd3794d7e85a",
  "cid": "QmV1c94a181fae93edf12f8419c85334d267483383e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291544,
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
      "evaluated_at": 1760291544
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
  "sig": "96b05fa5ba6318973997f2a0b236f8e8cf8be9a81e52c88c1b4f39b569bfbf0c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037820415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285765, 'matching_hash': 'e2c6bf9b42825543'}}}