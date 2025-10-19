```json
{
  "id": "e167f1b5864202dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294392,
  "host_pid": "9e6742732c60:1",
  "hash": "6394fff8ccd4adaed83d580633177b0fba745217123aea2068e163649036f0bc",
  "cid": "QmV16394fff8ccd4adaed83d580633177b0fba745217",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294392,
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
      "evaluated_at": 1760294392
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "ac511cae96ce367c2132a38f6d346fb50b3056525aee515f6feaeac713f2044a"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 607486347609576
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 103699587, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': '01e47067eb24b5e9'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '607486349', 'validation_error': 'Invalid routing number checksum'}}}