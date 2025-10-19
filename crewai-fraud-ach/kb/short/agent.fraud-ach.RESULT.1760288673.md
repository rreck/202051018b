```json
{
  "id": "3fab1b07a9b09af5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288673,
  "host_pid": "9e6742732c60:1",
  "hash": "b503315d2fcb92ce84c1670b2e7ad286db4ec8595945383c05c984ec103485c2",
  "cid": "QmV1b503315d2fcb92ce84c1670b2e7ad286db4ec859",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288673,
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
      "evaluated_at": 1760288673
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
  "sig": "7f667fefac8acf73ff29dd48c36e802c9bcf7140663a10c50ee78fbc0e6954ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 31824800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}