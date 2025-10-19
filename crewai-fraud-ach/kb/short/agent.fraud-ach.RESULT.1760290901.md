```json
{
  "id": "1a096e67acce0ff1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290901,
  "host_pid": "9e6742732c60:1",
  "hash": "a2a62298cf3c1e16d4a540d9e7977a0ae04ca3d8116d560011b4d12c5ef3258b",
  "cid": "QmV1a2a62298cf3c1e16d4a540d9e7977a0ae04ca3d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290901,
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
      "evaluated_at": 1760290901
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
  "sig": "6b04c0b341f0d68d869697163030e8fac92b8f0643d11a473ceb6be9525c6e93"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 063100275656907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 1116579978, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285764, 'matching_hash': '3d5aab5dd753a251'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6892469}}}