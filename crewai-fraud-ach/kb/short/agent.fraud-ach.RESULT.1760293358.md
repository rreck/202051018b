```json
{
  "id": "e68bb4a73dcdbf2f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293358,
  "host_pid": "9e6742732c60:1",
  "hash": "cf0d4941033477589d7fe7ea881f63402fdb34b5bdc130ca947a4ebc79a73a4c",
  "cid": "QmV1cf0d4941033477589d7fe7ea881f63402fdb34b5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293358,
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
      "evaluated_at": 1760293358
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
  "sig": "153796b796aacfbd4c6be429568bfcafbf00a5b0eb1217ace9880fdb6469b281"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 063100277197484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 2158583196, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '4232e93b8d4c62d2'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 92, 'details': {'zscore': 5.25, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9947388}}}