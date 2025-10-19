```json
{
  "id": "68beb21a9d50c60f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289649,
  "host_pid": "9e6742732c60:1",
  "hash": "281f7c3c56d3e98f3575e7f00d1f688dbfeb81bceee406dd9898116ce690006a",
  "cid": "QmV1281f7c3c56d3e98f3575e7f00d1f688dbfeb81bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289649,
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
      "evaluated_at": 1760289649
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
  "sig": "3d3bdcf01f9bea043e7c4ccc6199a02e2741f8012a316304a5baebea4ddf0686"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272268645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 56800119, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285765, 'matching_hash': '088fbc730f5432fe'}}}