```json
{
  "id": "57015fb5e493c1ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293193,
  "host_pid": "9e6742732c60:1",
  "hash": "b3795cebbd4accab054ebfe504b09c81ae52338777c23a46720d9eceba9bf43f",
  "cid": "QmV1b3795cebbd4accab054ebfe504b09c81ae523387",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293193,
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
      "evaluated_at": 1760293193
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
  "sig": "13d3e11104128528beb408fdaa83c538cf00c1e25450c709999edfc7dfb7d90d"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 021000024248654
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 1651591137, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285765, 'matching_hash': '6adb7b11c0829b91'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.0, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7753949}}}