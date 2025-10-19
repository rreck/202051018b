```json
{
  "id": "6174fcd717c2be51",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289373,
  "host_pid": "9e6742732c60:1",
  "hash": "d3927c62b15c39d3a4ad958b6cf39290e3e19d716765043f5bc5ab753a705c1f",
  "cid": "QmV1d3927c62b15c39d3a4ad958b6cf39290e3e19d71",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289373,
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
      "evaluated_at": 1760289373
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
  "sig": "8c8d0664d8b31ecf9c2e7e0f5de63ff216e23fda741de38d089245b043a1a12d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593563572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 19524197, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285765, 'matching_hash': 'b3bf50e818486c57'}}}