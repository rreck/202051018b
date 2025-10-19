```json
{
  "id": "bec0065e4988bd8e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285911,
  "host_pid": "9e6742732c60:1",
  "hash": "9c97d191074b6d7d2d3d896ed0e27259cbdf6839130cfa69e31ec3f10c1f087d",
  "cid": "QmV19c97d191074b6d7d2d3d896ed0e27259cbdf6839",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285911,
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
      "evaluated_at": 1760285911
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
  "sig": "4498f4794219635bc756309a61b2de7c8a4293a350dc766acecc85950d4daec6"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000023834320
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285763, 'matching_hash': 'd0d38b811698e46a'}}}