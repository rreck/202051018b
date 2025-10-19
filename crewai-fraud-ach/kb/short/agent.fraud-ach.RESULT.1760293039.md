```json
{
  "id": "0488b72dfc330acb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293039,
  "host_pid": "9e6742732c60:1",
  "hash": "a6ad9b566febf74d62b3fa462af0ddda38271d1cce0148ea01399c8c8674ad04",
  "cid": "QmV1a6ad9b566febf74d62b3fa462af0ddda38271d1c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293039,
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
      "evaluated_at": 1760293039
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
  "sig": "1dc2ef14be58bd4a57ed746ec000b31922649e1b23318ea385c2fe2c73befb42"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596790322
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 286, 'threshold': 50, 'total_amount': 14967524, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 285, 'first_seen': 1760284979, 'matching_hash': 'b9497544c8340a37'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '880809095', 'validation_error': 'Invalid routing number checksum'}}}