```json
{
  "id": "a0cd4223788e1739",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292668,
  "host_pid": "9e6742732c60:1",
  "hash": "c31c9a86e0d1c0a79f4535d07a8395af2180bcfbe3121213b4a7e19fe3b7832c",
  "cid": "QmV1c31c9a86e0d1c0a79f4535d07a8395af2180bcfb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292668,
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
      "evaluated_at": 1760292668
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
  "sig": "3d1bf474870abe77492cccf9a0ffb1c0cd78e3550ff5f0dee1423cbc3420becf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593122933
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 81733038, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285765, 'matching_hash': '1a44b34bf830cda9'}}}