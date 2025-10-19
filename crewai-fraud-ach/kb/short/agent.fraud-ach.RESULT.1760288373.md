```json
{
  "id": "28a0f916a16784e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288373,
  "host_pid": "9e6742732c60:1",
  "hash": "d0699872c9ba3f68a635010b77332b2b72b2eb3d14e9646fd21c585d0f8d51ec",
  "cid": "QmV1d0699872c9ba3f68a635010b77332b2b72b2eb3d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288373,
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
      "evaluated_at": 1760288373
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
  "sig": "212c2764445703123646eb22dcda72d5304cd62139b2465804927e5a454e51fa"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 031201464331888
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 576281797, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285764, 'matching_hash': '6a7d940bcd4512ca'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6332767}}}