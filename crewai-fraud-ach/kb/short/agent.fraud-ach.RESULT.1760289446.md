```json
{
  "id": "3ac4e5d5f698a75d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289446,
  "host_pid": "9e6742732c60:1",
  "hash": "4f8b0c7e0a9c35db090c2922d3e84a7add9301110177f32accc1ffc25e0cb969",
  "cid": "QmV14f8b0c7e0a9c35db090c2922d3e84a7add930111",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289446,
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
      "evaluated_at": 1760289446
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
  "sig": "fd723988bb687c87706a5eb17826ab58505b8c3581c573cb740a750731b6a80c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153937190
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 59619699, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285765, 'matching_hash': '8cf441fb6328957e'}}}