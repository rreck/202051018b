```json
{
  "id": "031712e7475b0c6c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292472,
  "host_pid": "9e6742732c60:1",
  "hash": "e930c81328eb6cf189c644c6be7f875d1eb9a5eb57742ea73b9e69d5ed067733",
  "cid": "QmV1e930c81328eb6cf189c644c6be7f875d1eb9a5eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292472,
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
      "evaluated_at": 1760292472
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
  "sig": "efeff515a128586f694cd735b51d890eb0aefbce4cbef053fc54c68f47b43954"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245329334
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 73018836, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285765, 'matching_hash': 'de3fbc58a94e529a'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '491975133', 'validation_error': 'Invalid routing number checksum'}}}