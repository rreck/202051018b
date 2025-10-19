```json
{
  "id": "f0fc380b45fe746b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288239,
  "host_pid": "9e6742732c60:1",
  "hash": "d6a4bf6c2eb6287972bfe6a5dac57d07ddc55ed86b88ced4021d61a84e2d9ed7",
  "cid": "QmV1d6a4bf6c2eb6287972bfe6a5dac57d07ddc55ed8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288239,
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
      "evaluated_at": 1760288239
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
  "sig": "0ee682c4db340f9445cbac895d5a2ac498c8d6fc8364e047c6d21461bd963f13"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243741176
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 26475405, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285763, 'matching_hash': 'e78a513bf0bcec2f'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}