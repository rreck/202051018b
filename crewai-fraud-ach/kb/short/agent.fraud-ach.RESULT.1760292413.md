```json
{
  "id": "fc350ea000841c12",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292413,
  "host_pid": "9e6742732c60:1",
  "hash": "b696c7bb01f72ebea101ad606aa7ad36d0e2d38d4382c2c0bc9e9b2c256f1129",
  "cid": "QmV1b696c7bb01f72ebea101ad606aa7ad36d0e2d38d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292413,
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
      "evaluated_at": 1760292413
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
  "sig": "3bd317ab5ad5d520c83b88c334c981e6db8e123a34ef0bc3b5924817ce71fe7a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024487889
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 81413205, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285764, 'matching_hash': '1280efea2d0c7f9c'}}}