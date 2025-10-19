```json
{
  "id": "1afb627a7b2c5e6f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293610,
  "host_pid": "9e6742732c60:1",
  "hash": "e1fd4d82135875ddd37bdb2696d25a8517a39b5b3db9a1b836c3a72e8a42313d",
  "cid": "QmV1e1fd4d82135875ddd37bdb2696d25a8517a39b5b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293610,
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
      "evaluated_at": 1760293610
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
  "sig": "6242e7161b41b39f0f4d85d2122c4256eddd4a6e15904123f3e442a7c150183f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461662622
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 42649752, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '96e0bea374e50243'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '020899456', 'validation_error': 'Invalid routing number checksum'}}}