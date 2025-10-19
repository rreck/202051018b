```json
{
  "id": "688ddbcb17a308fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291482,
  "host_pid": "9e6742732c60:1",
  "hash": "bca75612912101781ad97c5e918de4120e97fa5c868f7c2b6238705f27066dbd",
  "cid": "QmV1bca75612912101781ad97c5e918de4120e97fa5c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291482,
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
      "evaluated_at": 1760291482
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
  "sig": "6bdb4da564400a2d95a7d3eb0385dee9af26a663349614f61097d2131bba9caf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021660163
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 43246896, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': '34e344aa40e60b39'}}}maly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9245331}}}