```json
{
  "id": "3223815f53703178",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288733,
  "host_pid": "9e6742732c60:1",
  "hash": "30aced22c76558a97f56ec3cfdb07a05d5b2533bb8a337bda6cd275cc615c74a",
  "cid": "QmV130aced22c76558a97f56ec3cfdb07a05d5b2533b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288733,
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
      "evaluated_at": 1760288733
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
  "sig": "12b03e58b3c81051ba3403b5195e52d8d79050f228c9fcd576d4744ff1f9403c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599118273
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 13256124, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285765, 'matching_hash': '777fe2ef7ab8cdc9'}}}