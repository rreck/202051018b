```json
{
  "id": "c3eae756845e5736",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288185,
  "host_pid": "9e6742732c60:1",
  "hash": "22fb7282fb515e2262b571fb37e0e0180e3072f2e038a102d5e0bed5e311ec75",
  "cid": "QmV122fb7282fb515e2262b571fb37e0e0180e3072f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288185,
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
      "evaluated_at": 1760288185
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
  "sig": "b9be455787f78e7bb75a2dc2de79f2b70fece2111372e09d2b9c43306b5ce636"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593563572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 13715345, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285765, 'matching_hash': 'b3bf50e818486c57'}}}