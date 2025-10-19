```json
{
  "id": "87054220818a16c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291635,
  "host_pid": "9e6742732c60:1",
  "hash": "653fb69ad0cc2f68379fe646afc123e0c0563513af3cc8c58a34eb78bb3a56b0",
  "cid": "QmV1653fb69ad0cc2f68379fe646afc123e0c0563513",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291635,
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
      "evaluated_at": 1760291635
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
  "sig": "f3479085d5ca20dcbac9664f3b410bb13ea295137180a2b5b5d8c7477185160b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 56966392, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}