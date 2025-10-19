```json
{
  "id": "d3e7b8f9da482f35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294895,
  "host_pid": "9e6742732c60:1",
  "hash": "650bacfc13c2f9be2b836e2aa2a55277a3a703981360de37f112b39a156f7a15",
  "cid": "QmV1650bacfc13c2f9be2b836e2aa2a55277a3a70398",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294895,
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
      "evaluated_at": 1760294895
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
  "sig": "e2394d0b8c13779719da8a36aeeeef9db9fa3235720e9b7f29b5dbb43c334d1f"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 111000028335360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 1829504952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285764, 'matching_hash': '8e80efed4b38ef8e'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 78, 'details': {'zscore': 3.82, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7437012}}}