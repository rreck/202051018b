```json
{
  "id": "3c85fe6930e5579e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293908,
  "host_pid": "9e6742732c60:1",
  "hash": "3e804f0a71d18f26ba3b4721a1bce7d94ec0977e2803d4360d202a34f1aa340c",
  "cid": "QmV13e804f0a71d18f26ba3b4721a1bce7d94ec0977e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293908,
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
      "evaluated_at": 1760293908
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
  "sig": "40445b32316a6031a8d6a021ba20152d0445283a8c078124b8407344b3aeb6a1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159848459
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 46975296, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': 'f6f76290fac8b474'}}}