```json
{
  "id": "41bc89904af417c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293228,
  "host_pid": "9e6742732c60:1",
  "hash": "cce73299307c6627a3efc3d4257f28e844f85ae4a345bbad6330792af0d03608",
  "cid": "QmV1cce73299307c6627a3efc3d4257f28e844f85ae4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293228,
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
      "evaluated_at": 1760293228
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
  "sig": "198870519f0f35f7603aeb964348729a71e6023709c41db9fbeb6dbed6add3be"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271259155
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 84658186, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '525a45536127a4d2'}}}