```json
{
  "id": "c208d2d793b119a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288739,
  "host_pid": "9e6742732c60:1",
  "hash": "b7038ac9978031601942e8245bc64c8534fea008486d5163408fd6123427adbb",
  "cid": "QmV1b7038ac9978031601942e8245bc64c8534fea008",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288739,
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
      "evaluated_at": 1760288739
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
  "sig": "bebd4c7d1f652daf496b43871b3df4439f34dfd5fe3b247513933b87a4916f39"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 32461296, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}