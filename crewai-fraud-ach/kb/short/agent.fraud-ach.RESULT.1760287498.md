```json
{
  "id": "d83846045f7078f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287498,
  "host_pid": "9e6742732c60:1",
  "hash": "8caf4c194b43e7b5ab201f96b1d2edbfcfbba8c16be2dc2b86bd5b522b8fbd1c",
  "cid": "QmV18caf4c194b43e7b5ab201f96b1d2edbfcfbba8c1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287498,
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
      "evaluated_at": 1760287498
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
  "sig": "ee1def7109bee3706c8f6b54c38e87631b3d083638a300862f69ae77d27d2f6e"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 063100272414433
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285764, 'matching_hash': 'f489e4bd64364941'}}}