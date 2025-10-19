```json
{
  "id": "28dcfdfc5a13b8f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290292,
  "host_pid": "9e6742732c60:1",
  "hash": "a8cee3f3c5b85f199760c562ff879eea16231073c74a340e7e9710fcc5cd5767",
  "cid": "QmV1a8cee3f3c5b85f199760c562ff879eea16231073",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290292,
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
      "evaluated_at": 1760290292
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
  "sig": "da637300881005660cd74148661307a542ca8b9fbb2d6aa5d78ecf1a11e49782"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 46464208, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}