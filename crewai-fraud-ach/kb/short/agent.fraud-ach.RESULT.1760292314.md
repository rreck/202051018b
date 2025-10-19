```json
{
  "id": "dfdcd4592e57c40b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292314,
  "host_pid": "9e6742732c60:1",
  "hash": "a4cb098cecbf325da3a8487d5e7c7c8d97cc9f67af510a196423754be44aa32f",
  "cid": "QmV1a4cb098cecbf325da3a8487d5e7c7c8d97cc9f67",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292314,
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
      "evaluated_at": 1760292314
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
  "sig": "7c1ccee4a1ec5044fb488ed232095d98225240fb9c25816bb246e9353a1260cb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462101683
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 64675845, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': 'e66600e2d7fa312e'}}}