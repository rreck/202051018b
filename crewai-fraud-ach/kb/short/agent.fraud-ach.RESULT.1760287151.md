```json
{
  "id": "86ce98c53d9f4099",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287151,
  "host_pid": "9e6742732c60:1",
  "hash": "9f54d63c06aadaa3d0484e498796a6292b864cac6fcbf19025ca76e49f321c3c",
  "cid": "QmV19f54d63c06aadaa3d0484e498796a6292b864cac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287151,
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
      "evaluated_at": 1760287151
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
  "sig": "f6571eada0e25480030366c062a049aeebb350efa99d4589365215c14efe4cf6"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009592795708
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 22982550, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285763, 'matching_hash': '6f9672c314113419'}}}