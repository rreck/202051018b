```json
{
  "id": "354f5c2142a5f144",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288025,
  "host_pid": "9e6742732c60:1",
  "hash": "00f9f44c3d91cec1b89ac5cee28b6a39220cce7f4a5f083671fd6923b287db3b",
  "cid": "QmV100f9f44c3d91cec1b89ac5cee28b6a39220cce7f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288025,
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
      "evaluated_at": 1760288025
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
  "sig": "a79edb25af6b85e096120c7dd21986696ebbc478dd192fbbd103b0c3d6ca703c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154969717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 62187528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760284979, 'matching_hash': '5065063b494c04f4'}}}y': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.2, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8549284}}}