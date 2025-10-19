```json
{
  "id": "c8ee9e8f43fa7624",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292886,
  "host_pid": "9e6742732c60:1",
  "hash": "ea68f0fab915e086d40089e9c095f2d026d8a86faace024b6a1d1807a9851724",
  "cid": "QmV1ea68f0fab915e086d40089e9c095f2d026d8a86f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292886,
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
      "evaluated_at": 1760292886
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
  "sig": "251b9e4051f396eccc4d11f4ecc27199d18c4566f7540fe3741493024f347dbd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468629827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 18299214, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': 'f998250ed7d87b2f'}}}