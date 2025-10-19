```json
{
  "id": "c6fd862a9a406059",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289217,
  "host_pid": "9e6742732c60:1",
  "hash": "1bd61220fae9f407ee871d5b62dc9a7607b7d7d381eadb8b2830ffae999f19ea",
  "cid": "QmV11bd61220fae9f407ee871d5b62dc9a7607b7d7d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289217,
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
      "evaluated_at": 1760289217
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
  "sig": "283582c3e961d5fa8c5e24ad6e14d42b8904110cb4245ca3f5e535505cce59f7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272419137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 30242394, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285763, 'matching_hash': '38281b9a763b4bf2'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '408733730', 'validation_error': 'Invalid routing number checksum'}}}