```json
{
  "id": "6b2a8fa6d9a3ccd7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292781,
  "host_pid": "9e6742732c60:1",
  "hash": "989e4ff11587c050fed4df74c3da250e038cb5d76855d6d0724b37a4613c2106",
  "cid": "QmV1989e4ff11587c050fed4df74c3da250e038cb5d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292781,
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
      "evaluated_at": 1760292781
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
  "sig": "d4f288bd828064468a2b45f7f953ec6c5c5740ffb3f7d4e03d58b5352b5adc5a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466501917
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 86465515, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': '521eaa6e61198532'}}}