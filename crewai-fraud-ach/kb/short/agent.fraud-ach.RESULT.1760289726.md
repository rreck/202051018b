```json
{
  "id": "49fb4ccc39e71eec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289726,
  "host_pid": "9e6742732c60:1",
  "hash": "84b7157c5733263285fff7f0e58c7203fc198e659ce89d651a7ef0a4bad7f2da",
  "cid": "QmV184b7157c5733263285fff7f0e58c7203fc198e65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289726,
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
      "evaluated_at": 1760289726
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
  "sig": "ce995e3b8b44545e107f47c03be40c7f46536060f63766db4f87d524e386b3de"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029265266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 48089183, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285764, 'matching_hash': 'a9619dd56a360910'}}}