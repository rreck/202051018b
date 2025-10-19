```json
{
  "id": "ea21d3e8dde62837",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286677,
  "host_pid": "9e6742732c60:1",
  "hash": "c86af4ea764effa105e4757b870b6806ef1df48743ecfe6e225bbf2d1c49061e",
  "cid": "QmV1c86af4ea764effa105e4757b870b6806ef1df487",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286677,
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
      "evaluated_at": 1760286677
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "2397d94db8482ed9ed3af53719fc25ba2fbc88815d676852bde1c9ca1ca7f255"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000024109289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11529177, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285765, 'matching_hash': 'ac2c8f9ff893d8ff'}}}