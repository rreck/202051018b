```json
{
  "id": "d61d6333e23263c5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285921,
  "host_pid": "9e6742732c60:1",
  "hash": "f6662631d1d174cdf83e0667acdad78f111a1a9ee1ed9fea1101d2e4f673aff8",
  "cid": "QmV1f6662631d1d174cdf83e0667acdad78f111a1a9e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285921,
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
      "evaluated_at": 1760285921
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
  "sig": "27303905e2cac528dab4482b38bcc6b7a299be6563e6b88f40b70175019a65ab"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201469922578
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285763, 'matching_hash': '96901979868c282a'}}}