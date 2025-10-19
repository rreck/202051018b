```json
{
  "id": "4a188985e0eb5baa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293194,
  "host_pid": "9e6742732c60:1",
  "hash": "707c87c4e91d7a5f8297a85b4bf66873c3501beb2e8cfb6b4d0c294f4455e2c0",
  "cid": "QmV1707c87c4e91d7a5f8297a85b4bf66873c3501beb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293194,
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
      "evaluated_at": 1760293194
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
  "sig": "88c553ceaaa947b7bb113d86e721ce9a9c7a58127afcc02ac9ff84f51c43d12f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242007664
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 30831537, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285765, 'matching_hash': 'b61887453511199f'}}}