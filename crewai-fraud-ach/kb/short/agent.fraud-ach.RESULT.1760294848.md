```json
{
  "id": "6cbcc977e623863f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294848,
  "host_pid": "9e6742732c60:1",
  "hash": "6961cb76d6242c2f722391351886c2302e89d795b5c6bb62a1efa445820c1627",
  "cid": "QmV16961cb76d6242c2f722391351886c2302e89d795",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294848,
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
      "evaluated_at": 1760294848
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
  "sig": "0dd03eb71e4d63e53b818d1fb5d43b33b7d548fea36240ef48fca2e188896bcc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 77970760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}