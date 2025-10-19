```json
{
  "id": "2ff2ce2ac6644685",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292785,
  "host_pid": "9e6742732c60:1",
  "hash": "9a4c33e8519f60effc6160c73007a3d9bc797d34724d04c338b19ec26634a037",
  "cid": "QmV19a4c33e8519f60effc6160c73007a3d9bc797d34",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292785,
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
      "evaluated_at": 1760292785
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
  "sig": "e32f26c40287be58b52b4e953b94cec9a2e971e31c6a570707daa041bd824832"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 026009591320033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 1650697310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285764, 'matching_hash': '73d2316250f00dec'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.17, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8052182}}}