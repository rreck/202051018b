```json
{
  "id": "7a2ce3e8ba5509ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289467,
  "host_pid": "9e6742732c60:1",
  "hash": "7eb7fae2a6906c76f2568a12ad643045ead3b34bd761ac315f3b88773472034c",
  "cid": "QmV17eb7fae2a6906c76f2568a12ad643045ead3b34b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289467,
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
      "evaluated_at": 1760289467
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
  "sig": "c4d04a5addd6ab4b0c3cc2cb062a724b792e8235978cd4369676f9a066a54f7f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240945799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285763, 'matching_hash': '2868277a63cf50ca'}}}5765, 'matching_hash': 'c666b8c882e80c0b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '649278788', 'validation_error': 'Invalid routing number checksum'}}}