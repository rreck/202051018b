```json
{
  "id": "5cf007ef09c77335",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290063,
  "host_pid": "9e6742732c60:1",
  "hash": "9b5184f673e1a00dd56398c78c02b464764667fe2a0d9bfb57311bbb1643d3cf",
  "cid": "QmV19b5184f673e1a00dd56398c78c02b464764667fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290063,
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
      "evaluated_at": 1760290063
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
  "sig": "fd046724fb50874943bfac9abb23696cec12190a8a0128674fb5664c9eaf306b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245511773
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 27030500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285765, 'matching_hash': '976242956abb43a6'}}}