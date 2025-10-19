```json
{
  "id": "fc93249ed2561eed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289676,
  "host_pid": "9e6742732c60:1",
  "hash": "a6816f29ae3016e109a012a50c09a7209da9005e81e4e5de39af77976cbaf8fb",
  "cid": "QmV1a6816f29ae3016e109a012a50c09a7209da9005e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289676,
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
      "evaluated_at": 1760289676
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
  "sig": "642a77676bf43b4888a6954d725056c93579fabd8be6e2ee787e9d0811859403"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270759086
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 46631000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285763, 'matching_hash': 'eb79951538526d2c'}}}aly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.1, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6161479}}}