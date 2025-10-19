```json
{
  "id": "4d7d3d96a5e47b59",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288703,
  "host_pid": "9e6742732c60:1",
  "hash": "c41c8b332ceedce49f5dc63242a906ef5170653bb6dc0d289f8834e13005a4a7",
  "cid": "QmV1c41c8b332ceedce49f5dc63242a906ef5170653b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288703,
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
      "evaluated_at": 1760288703
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
  "sig": "6688695ded7a7fa7e812d642a1001eda698ebeba49bff77af0a1e8f7c87676bf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247383202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 40223755, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285765, 'matching_hash': '32929947211460fd'}}}