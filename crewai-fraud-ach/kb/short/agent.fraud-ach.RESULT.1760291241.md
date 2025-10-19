```json
{
  "id": "ed263380a566f0ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291241,
  "host_pid": "9e6742732c60:1",
  "hash": "8fc22f6eb1276a66ae3c5068020bdcc412b432501ce7ae773bb5b8c40e1b295e",
  "cid": "QmV18fc22f6eb1276a66ae3c5068020bdcc412b43250",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291241,
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
      "evaluated_at": 1760291241
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
  "sig": "c8e1fc25aaf835bfb86875c12035de595c54eb889b8cc079f1f17c64af2ed275"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025895266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 48263000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': '9ac81502eabc8fa5'}}}