```json
{
  "id": "3a6ac9ca326a857d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292742,
  "host_pid": "9e6742732c60:1",
  "hash": "a354f5364ecda58674982c38b825f75730e73f2262384467044d7e71e331b10a",
  "cid": "QmV1a354f5364ecda58674982c38b825f75730e73f22",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292742,
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
      "evaluated_at": 1760292742
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
  "sig": "b6828c18fc67b3eed28ae57700f89b17f63291ebe7a13b273c74c356f7ae7c66"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026876887
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 54437808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': 'ac27634a0ee0b6ee'}}}