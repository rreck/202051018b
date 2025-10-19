```json
{
  "id": "008596a8a7f4b85c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294809,
  "host_pid": "9e6742732c60:1",
  "hash": "786fc7609e281e62b0f869cba06a1839614d74d5734a3c23cd3dc4af76a716ed",
  "cid": "QmV1786fc7609e281e62b0f869cba06a1839614d74d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294809,
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
      "evaluated_at": 1760294809
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
  "sig": "789beb558b521706fa0bc43c436591676e165fce5c7220a94e81a1002d77abd7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159848459
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 50477840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': 'f6f76290fac8b474'}}}