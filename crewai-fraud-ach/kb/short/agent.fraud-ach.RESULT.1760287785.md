```json
{
  "id": "465d07944882890d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287785,
  "host_pid": "9e6742732c60:1",
  "hash": "89c0773e4d60ce745b0d24124243436611fdb3f3bdc68bdd7273ac812d0667d5",
  "cid": "QmV189c0773e4d60ce745b0d24124243436611fdb3f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287785,
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
      "evaluated_at": 1760287785
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
  "sig": "e096eb7eeb2fe5cfb7ebbac0083a6dfd74884caced59a0bd2331ef59e07c1be7"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 121000244410720
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285763, 'matching_hash': 'eab520de73a5b8cf'}}}