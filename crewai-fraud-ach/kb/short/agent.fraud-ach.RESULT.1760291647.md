```json
{
  "id": "5990e648bd263fcb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291647,
  "host_pid": "9e6742732c60:1",
  "hash": "5a3ce459ddc7bb2edfefe91c761a23cdb20b1fee7b16cf52837271af3d21f0b1",
  "cid": "QmV15a3ce459ddc7bb2edfefe91c761a23cdb20b1fee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291647,
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
      "evaluated_at": 1760291647
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
  "sig": "fbf27d0d4f0d94baaddb49f370ce6bd1fe068d7214154c2cce12252a6dd20c2f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276193597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 45673200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': 'c482c58c8f3e1991'}}}