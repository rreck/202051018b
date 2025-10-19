```json
{
  "id": "60ebb316377456c7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292893,
  "host_pid": "9e6742732c60:1",
  "hash": "569f99cc50d47d05ea986a4ffb38ad2008dc109d0dd4cbe9a179f9fff2f1c25a",
  "cid": "QmV1569f99cc50d47d05ea986a4ffb38ad2008dc109d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292893,
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
      "evaluated_at": 1760292893
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
  "sig": "ad1d73c74d777e0424b5d6018f709ef7321f880769ee1c2b17dedacd0b520904"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 021000029388663
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 283, 'threshold': 50, 'total_amount': 2772129330, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 282, 'first_seen': 1760284979, 'matching_hash': '503d742180c16441'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.16, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9795510}}}