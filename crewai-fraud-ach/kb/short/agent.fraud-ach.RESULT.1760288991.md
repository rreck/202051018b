```json
{
  "id": "a73593f3fe4465a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288991,
  "host_pid": "9e6742732c60:1",
  "hash": "d276dca12ecfae9316ace526bb2e559a57f99cf1a87be1112655c0300ce7e5c6",
  "cid": "QmV1d276dca12ecfae9316ace526bb2e559a57f99cf1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288991,
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
      "evaluated_at": 1760288991
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
  "sig": "74fec2ba1963bb248de3e99bed5b5bb1b369d828d73195b05a144d4979121717"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025260373
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 34191300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285765, 'matching_hash': '6c25bdeba85ae9df'}}}