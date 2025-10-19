```json
{
  "id": "bc4b62aeeb4eef96",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293165,
  "host_pid": "9e6742732c60:1",
  "hash": "dedd608f13e285ba83319f46e9357b1edf3f907a8e253d3cacd5015a1b6b9454",
  "cid": "QmV1dedd608f13e285ba83319f46e9357b1edf3f907a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293165,
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
      "evaluated_at": 1760293165
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
  "sig": "4c861846eba32971d135f8504b4b179f4fbc9a4c3f57c04e7b74930eb97b26ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027419247
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 100071873, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': 'f49fdb64c00c5aec'}}}