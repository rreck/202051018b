```json
{
  "id": "2c302a9dfab609ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294452,
  "host_pid": "9e6742732c60:1",
  "hash": "36be8aeca27af82c3e775a53c8863095463ff0a76fcb4e17a3d1fb2a23c90eda",
  "cid": "QmV136be8aeca27af82c3e775a53c8863095463ff0a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294452,
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
      "evaluated_at": 1760294452
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
  "sig": "b82780550542c99a53aeaa4be4e0d3191c919e48fce0db9e6ec05915bee0168e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021222877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 23800000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285765, 'matching_hash': 'c44c29fab5dec0d9'}}}