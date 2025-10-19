```json
{
  "id": "bf03c2590ae5f5cf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286557,
  "host_pid": "9e6742732c60:1",
  "hash": "5f720a0af44d0668dc046f6551f9e3f12b0177dda7d3cf1b41f01a1de93ec331",
  "cid": "QmV15f720a0af44d0668dc046f6551f9e3f12b0177dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286557,
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
      "evaluated_at": 1760286557
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
  "sig": "d374c4eb20f6dfc89ee037d922bd5884585ec2f66c781a185b797b9a36d05d42"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243277611
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285763, 'matching_hash': '2d64263c5765c58b'}}}