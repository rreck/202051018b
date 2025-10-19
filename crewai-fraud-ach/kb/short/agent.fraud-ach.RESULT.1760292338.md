```json
{
  "id": "99cac0365cc42c0e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292338,
  "host_pid": "9e6742732c60:1",
  "hash": "92b1a53b9625b0a7c42f6cd2682dedd02336a2207434d87f5182c8cf3f15b286",
  "cid": "QmV192b1a53b9625b0a7c42f6cd2682dedd02336a220",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292338,
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
      "evaluated_at": 1760292338
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
  "sig": "0ccbcc27ea1c21af8795e20b8f218250550a4f0cd9caf823e282cabee043a940"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279234721
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 44930340, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285764, 'matching_hash': 'a4a7a8ef6540eadb'}}}