```json
{
  "id": "e331b3080740dd9e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293457,
  "host_pid": "9e6742732c60:1",
  "hash": "d09220f29988aaeb0a5f53fb5c2d27c58b13bc8c7e475dba3dee75a669a23683",
  "cid": "QmV1d09220f29988aaeb0a5f53fb5c2d27c58b13bc8c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293457,
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
      "evaluated_at": 1760293457
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
  "sig": "832b8e724ba530090f14e5a80a02c15edbc12c2b0c540a0e18a7cc20e5bb7269"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 122105150872647
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 1578851154, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': 'f142eb53d77ea00a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.69, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7209366}}}