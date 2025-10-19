```json
{
  "id": "a52001da74d2cf2d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291348,
  "host_pid": "9e6742732c60:1",
  "hash": "84eed1dd4a5e2600aca1a191fdd291360403916e9bbd503f09cf358a79f62b25",
  "cid": "QmV184eed1dd4a5e2600aca1a191fdd291360403916e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291348,
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
      "evaluated_at": 1760291348
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
  "sig": "53fcaae86051ab5b182985eb4b16f5e44447b78589b10551265b000246250a45"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023834320
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 61071768, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': 'd0d38b811698e46a'}}}