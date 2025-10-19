```json
{
  "id": "e63a2693bf9b659f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293922,
  "host_pid": "9e6742732c60:1",
  "hash": "c0059d10381890059009d592cb413d8081c0d08856c64f361af714a59d4cd674",
  "cid": "QmV1c0059d10381890059009d592cb413d8081c0d088",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293922,
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
      "evaluated_at": 1760293923
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
  "sig": "111b3f775ae4c7f1e9f08fdbd723c93ec12f0d894030f5f698ccc1b6cb95e75e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157518284
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 66570072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285764, 'matching_hash': '79d45ba49f6b4a46'}}}