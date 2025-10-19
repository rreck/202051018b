```json
{
  "id": "63ab64b3f58408ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289619,
  "host_pid": "9e6742732c60:1",
  "hash": "72f0fa2bfc57359698a86c7eea2376d43f37cb2e0b5679e06bdb0b958ed5c619",
  "cid": "QmV172f0fa2bfc57359698a86c7eea2376d43f37cb2e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289619,
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
      "evaluated_at": 1760289619
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
  "sig": "250ba45de78270252b40221da3678ffda985314d5d576251605ac0edb4109260"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157316048
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 32000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285764, 'matching_hash': '8f4887477877b00a'}}}