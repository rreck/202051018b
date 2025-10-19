```json
{
  "id": "df502865e27631fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288575,
  "host_pid": "9e6742732c60:1",
  "hash": "5ab7463146def0d3461c3e707da2ae3e6dccd1e498d4945daaaace3b07a9feeb",
  "cid": "QmV15ab7463146def0d3461c3e707da2ae3e6dccd1e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288575,
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
      "evaluated_at": 1760288575
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
  "sig": "2347837fdd7e478ffa098e86f5c668b84225b7f3f8d87d7bc972960aeab17584"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 30870056, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}