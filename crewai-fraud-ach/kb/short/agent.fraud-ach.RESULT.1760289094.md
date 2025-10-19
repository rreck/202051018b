```json
{
  "id": "c4de32db0bd2741c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289094,
  "host_pid": "9e6742732c60:1",
  "hash": "92a3f24dd437e8667cfa41fce36707e4d420be8fe28fb2aae282d60c097d8e07",
  "cid": "QmV192a3f24dd437e8667cfa41fce36707e4d420be8f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289094,
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
      "evaluated_at": 1760289094
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
  "sig": "cd8633d1d87a5cdf33d527d3bcc6fc7061f38badf7c6220be89cd623f20fd97a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467395210
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 12611478, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285765, 'matching_hash': 'b5e2565aea18e07c'}}}aly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.33, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8334426}}}