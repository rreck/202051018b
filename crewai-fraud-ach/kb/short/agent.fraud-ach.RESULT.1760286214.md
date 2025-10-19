```json
{
  "id": "64dc2aa38e87d4d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286214,
  "host_pid": "9e6742732c60:1",
  "hash": "42cd4db1ea9e0b14f0419b0335b57eb6694ad2d0b063f204dcaebf71456136de",
  "cid": "QmV142cd4db1ea9e0b14f0419b0335b57eb6694ad2d0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286214,
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
      "evaluated_at": 1760286214
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
  "sig": "dc117522d41d2a7a2573f14c1b7d388406e3d41160389292a016886776992066"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201468454923
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285765, 'matching_hash': '07b42bdcb312ebee'}}} 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760284979, 'matching_hash': 'a7fb9dc83800d725'}}}