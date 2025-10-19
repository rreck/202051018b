```json
{
  "id": "877b3308cd0a5a52",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289686,
  "host_pid": "9e6742732c60:1",
  "hash": "657bc3d86eec1e1c1f92105411b2495fd66259c654ba747e3064b0499c08f591",
  "cid": "QmV1657bc3d86eec1e1c1f92105411b2495fd66259c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289686,
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
      "evaluated_at": 1760289686
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
  "sig": "cb229d40df9f98124515b9cac6a324fe2f99c2a5b5036c483b6971e58420899a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466150314
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 57978288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760284979, 'matching_hash': '93cc3488fa8b8da9'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '537469236', 'validation_error': 'Invalid routing number checksum'}}}