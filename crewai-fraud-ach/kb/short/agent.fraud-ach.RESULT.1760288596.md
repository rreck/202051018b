```json
{
  "id": "23860d22f1488779",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288596,
  "host_pid": "9e6742732c60:1",
  "hash": "797cb3045713b0dd33275da25cfbfa9ce2bbed6c607a8dd33df6610e890046e2",
  "cid": "QmV1797cb3045713b0dd33275da25cfbfa9ce2bbed6c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288596,
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
      "evaluated_at": 1760288596
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
  "sig": "7a429e869240931c1aa514c4a5537ea5f7a2a82f4ad69f47cc475716ceb76f73"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467519914
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 11982460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285765, 'matching_hash': '8f358df1d478d699'}}}nomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.16, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9795510}}}