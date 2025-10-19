```json
{
  "id": "d3c9f4b117247d61",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293232,
  "host_pid": "9e6742732c60:1",
  "hash": "997ad892b5f24cf3abc3330d85895e413145f0fa2bc7ab98f3feb49cd39bac12",
  "cid": "QmV1997ad892b5f24cf3abc3330d85895e413145f0fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293232,
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
      "evaluated_at": 1760293232
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
  "sig": "e4fdee51d373e890f5a8c0cfe48c69844bd4f8661ab3b0cf766898ae7b74308c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244838202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 290, 'threshold': 50, 'total_amount': 69626100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 289, 'first_seen': 1760284979, 'matching_hash': 'f90729670e1d4f48'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '612898023', 'validation_error': 'Invalid routing number checksum'}}}