```json
{
  "id": "f2cc563447c69763",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286795,
  "host_pid": "9e6742732c60:1",
  "hash": "6374ad0b57b5d6e92b67d61531b7c3085a59f2f30749fe59886f3418c0234aa9",
  "cid": "QmV16374ad0b57b5d6e92b67d61531b7c3085a59f2f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286795,
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
      "evaluated_at": 1760286795
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "741d5a338c1cc77e8819785afa81858213a77faa28ebda01f89d41c3729442aa"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009593122933
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14970903, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285765, 'matching_hash': '1a44b34bf830cda9'}}}