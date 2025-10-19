```json
{
  "id": "468e6b5591efbca0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291119,
  "host_pid": "9e6742732c60:1",
  "hash": "b5a0b4aad94336a5b192613c93ad7bbfb5191edf8ed20b12dfe57f41660ab4cf",
  "cid": "QmV1b5a0b4aad94336a5b192613c93ad7bbfb5191edf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291119,
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
      "evaluated_at": 1760291119
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
  "sig": "fd1602c204d0c8de82c2dfebdd97f10fdce952c9e7fec52aa0cc9133a03a057f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248914863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285765, 'matching_hash': '9c0338b7ffb65590'}}}