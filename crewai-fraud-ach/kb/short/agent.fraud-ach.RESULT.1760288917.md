```json
{
  "id": "ab325213aeeaabc5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288917,
  "host_pid": "9e6742732c60:1",
  "hash": "3d9197cfe4355f8ec1e36e317863048845ca0157bc924ec69a74409169acb68e",
  "cid": "QmV13d9197cfe4355f8ec1e36e317863048845ca0157",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288917,
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
      "evaluated_at": 1760288917
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
  "sig": "d856928e28ee8def209a667b38aeeca33060ed4714cf32bcda527bbd81eb44aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246132965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 47486628, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285763, 'matching_hash': 'ed6ec2b6e100ea2c'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}