```json
{
  "id": "a98c7cb9c340ae62",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287690,
  "host_pid": "9e6742732c60:1",
  "hash": "d3a46562c018c642ef79ddaaee941a2c998c86dd257a7afd004eaa65d7f7093a",
  "cid": "QmV1d3a46562c018c642ef79ddaaee941a2c998c86dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287690,
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
      "evaluated_at": 1760287690
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
  "sig": "7abec23e2cdad75256a24b5daa5f76428017d536a16cd4befb79539a867b7072"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 031201468482875
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285764, 'matching_hash': '502f46d9d0122688'}}}een': 1760285763, 'matching_hash': '66d102d4303d651c'}}}