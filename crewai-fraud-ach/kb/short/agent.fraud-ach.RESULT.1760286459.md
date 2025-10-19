```json
{
  "id": "c944bf94252fc7d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286459,
  "host_pid": "9e6742732c60:1",
  "hash": "15455ecbf0f458ad43c5e58c870f4242f9aad602b7f477d0827320c93ce12247",
  "cid": "QmV115455ecbf0f458ad43c5e58c870f4242f9aad602",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286459,
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
      "evaluated_at": 1760286459
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "12b8a7aea1e990c69d161ff61ffe801e46efa216014b7e73d379937a6e1b1201"
}
```

Fraud detected: amount_anomaly (score: 75)
Transaction: 111000020782458
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 223488512, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285764, 'matching_hash': '09f46afbb4d14766'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.22, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8595712}}}