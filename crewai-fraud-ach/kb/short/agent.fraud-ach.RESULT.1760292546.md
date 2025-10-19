```json
{
  "id": "376ac6a3b9ef9a48",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292546,
  "host_pid": "9e6742732c60:1",
  "hash": "c641b15a30ae5e04d73013ab01c1c547ab92c543dadbed48f28092c5042cfe97",
  "cid": "QmV1c641b15a30ae5e04d73013ab01c1c547ab92c543",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292546,
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
      "evaluated_at": 1760292546
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
  "sig": "bbc3e73241ab2fd285c553fff3a7ec42d02e66d4812b5584676a6adfbcf7d8a6"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 063100270720281
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 1847442200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': 'aab950dc161fb34f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9237211}}}