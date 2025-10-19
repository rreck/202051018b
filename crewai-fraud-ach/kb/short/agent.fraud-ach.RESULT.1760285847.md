```json
{
  "id": "49193dd8af7d0409",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285847,
  "host_pid": "9e6742732c60:1",
  "hash": "f5c5451ab20b889bcace36c4663a1bd88415bceb2cec582f6f3c6a24e39d748b",
  "cid": "QmV1f5c5451ab20b889bcace36c4663a1bd88415bceb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285847,
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
      "evaluated_at": 1760285847
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
  "sig": "9791ea40d566b733b7768d8d44b4c32a6696dea2e7dbf67b793d41c8dee3f0ad"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157375662
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760284979, 'matching_hash': '8218a7a652f8297c'}}}