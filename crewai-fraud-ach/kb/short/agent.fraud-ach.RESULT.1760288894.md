```json
{
  "id": "304d793b31ca7de1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288894,
  "host_pid": "9e6742732c60:1",
  "hash": "0bdfe5c9c698f046310ca8073f26c380216f3207e12760bdd57278fb8bd8e05d",
  "cid": "QmV10bdfe5c9c698f046310ca8073f26c380216f3207",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288894,
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
      "evaluated_at": 1760288894
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "ef22870cbd0c2aadfbfba4feb20d576381b1580f4cdab14d760bcf7b9f56fd15"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 121000247715779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 107000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285763, 'matching_hash': 'e635467487b35661'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}