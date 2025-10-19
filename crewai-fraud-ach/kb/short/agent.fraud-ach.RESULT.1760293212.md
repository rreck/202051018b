```json
{
  "id": "ea9642c5082a667b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293212,
  "host_pid": "9e6742732c60:1",
  "hash": "cd4043e19e93a8a880dbdee1a280f32061d4e8b135c959e3bf87d93368cab427",
  "cid": "QmV1cd4043e19e93a8a880dbdee1a280f32061d4e8b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293212,
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
      "evaluated_at": 1760293212
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
  "sig": "cd4b0d39dc1ec13f4542b48926c805c70b95fda2dc7eb2157c1bac2902f2c1d8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038087823
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 89971806, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '9ca4fa9f5ff6e727'}}}