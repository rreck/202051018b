```json
{
  "id": "affbe58aea7695e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294099,
  "host_pid": "9e6742732c60:1",
  "hash": "47001d6abb6972d8dff64a39961984854e6ba9610da791c798a4e7f69af4c76b",
  "cid": "QmV147001d6abb6972d8dff64a39961984854e6ba961",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294099,
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
      "evaluated_at": 1760294099
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
  "sig": "65ff1cd457a2c8ef8607faee1d79c7f1686a817a848c0989ffc5264b9bbcf626"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024542500
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 100105698, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285765, 'matching_hash': 'f616428a070fc3ba'}}}