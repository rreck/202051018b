```json
{
  "id": "769cb60563eae914",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289801,
  "host_pid": "9e6742732c60:1",
  "hash": "ca2d5b3a395f20e378e7a465d6f1891a3846843187308d73669f3c84d6b73c4e",
  "cid": "QmV1ca2d5b3a395f20e378e7a465d6f1891a38468431",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289801,
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
      "evaluated_at": 1760289801
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
  "sig": "36db0728617de44c229b17f66d2d80cba15e7b003abd796d137e1313050ec6af"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 063100273946283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 1290157190, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285765, 'matching_hash': 'ff0c3c22534c93d5'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.11, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9700430}}}