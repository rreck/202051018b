```json
{
  "id": "deab7fd4681719b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289761,
  "host_pid": "9e6742732c60:1",
  "hash": "032857ea5a26abba86200620cce848842e5421b56df39a4502998f655f39be3f",
  "cid": "QmV1032857ea5a26abba86200620cce848842e5421b5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289761,
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
      "evaluated_at": 1760289761
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
  "sig": "8469582dddda4efae3cd596c6c34a062109dc3b0fef6d29a3c6364ce912ff4a7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593439334
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 50287116, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285763, 'matching_hash': 'a46c33998c9a26e1'}}}