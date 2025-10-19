```json
{
  "id": "59467812ef1254c5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294122,
  "host_pid": "9e6742732c60:1",
  "hash": "690078fe4082d91a0b1275a5f239df0f1e7e4093ec464b781a9cd173c0578ada",
  "cid": "QmV1690078fe4082d91a0b1275a5f239df0f1e7e4093",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294122,
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
      "evaluated_at": 1760294122
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
  "sig": "05be6f37189d5c71d130f4e579e7a882102534eb6754940c740d36afbe770598"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 026009591320033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 1868106224, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285764, 'matching_hash': '73d2316250f00dec'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.17, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8052182}}}