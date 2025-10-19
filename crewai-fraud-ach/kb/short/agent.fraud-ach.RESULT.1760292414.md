```json
{
  "id": "92b5005227ff8d2d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292414,
  "host_pid": "9e6742732c60:1",
  "hash": "0f23e151c178721f34691919901a9b1901f115225ed93b05c724b06bc817250a",
  "cid": "QmV10f23e151c178721f34691919901a9b1901f11522",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292414,
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
      "evaluated_at": 1760292414
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
  "sig": "a51e9c2d77875b38cc29dcbea7e0e854814dc0cf821e5c096b1b9c5d8208d8da"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244210031
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 80265483, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285764, 'matching_hash': '572834c9990ead18'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '691661790', 'validation_error': 'Invalid routing number checksum'}}}