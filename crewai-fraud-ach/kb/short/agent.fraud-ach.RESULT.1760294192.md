```json
{
  "id": "7311ec0c5b7e7e1b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294192,
  "host_pid": "9e6742732c60:1",
  "hash": "f6520e1ea59dbe62d35f8cd8fee411120a1423dc075671078f9e68feb17328e5",
  "cid": "QmV1f6520e1ea59dbe62d35f8cd8fee411120a1423dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294192,
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
      "evaluated_at": 1760294192
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
  "sig": "20ff737829b8933390ed7ca81256597d0767255655a3bbbdf5d004c04be3bbe2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022148998
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 64775398, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285765, 'matching_hash': 'cc8f74c02d21ef44'}}}