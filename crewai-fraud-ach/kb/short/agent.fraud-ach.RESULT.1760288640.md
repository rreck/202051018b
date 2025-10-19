```json
{
  "id": "e7d578452331ca36",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288640,
  "host_pid": "9e6742732c60:1",
  "hash": "23d01f8b07fa02047296793d78bc04da3bed6e195c2eabdd9aa50aaa64b6229c",
  "cid": "QmV123d01f8b07fa02047296793d78bc04da3bed6e19",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288640,
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
      "evaluated_at": 1760288640
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
  "sig": "9923da04b3207da35e83f0c0603bcb24685d01cd4be4e49453319bef1c9aef9a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 31506552, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}