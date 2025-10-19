```json
{
  "id": "59e7c3a387cb7658",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289985,
  "host_pid": "9e6742732c60:1",
  "hash": "8c5faffa0bacb7b7cac900c7bd26caab0aa8ebff30c91c873278770d61fbb249",
  "cid": "QmV18c5faffa0bacb7b7cac900c7bd26caab0aa8ebff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289985,
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
      "evaluated_at": 1760289985
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
  "sig": "341f0f1a61c29ef655cbaf03602af507486c2f9c9f07dc37f2c3e409a4a04bfc"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 031201467532863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 760978782, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285764, 'matching_hash': 'b320222423bba5e6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5514339}}}