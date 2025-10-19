```json
{
  "id": "46761bad41c1d690",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288186,
  "host_pid": "9e6742732c60:1",
  "hash": "1937d269858a84aa1be8a45409b1da6281a6c3a3abf04e4bf4e3ad07b020cc38",
  "cid": "QmV11937d269858a84aa1be8a45409b1da6281a6c3a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288186,
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
      "evaluated_at": 1760288186
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "1674cd5270ed27e8209a5d732f2c3f30599de0b6c1728e93da24df2292c8a2e1"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100278543685
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 602595430, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285765, 'matching_hash': 'e9470cd0cc07fb40'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7089358}}}