```json
{
  "id": "ae23303624c5776a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290698,
  "host_pid": "9e6742732c60:1",
  "hash": "1b099d919921056b8b7a3de852c9bceafd6521f68865d7b4bee6e171b22fb1c4",
  "cid": "QmV11b099d919921056b8b7a3de852c9bceafd6521f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290698,
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
      "evaluated_at": 1760290698
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
  "sig": "33643bdc16262ef931b1e54f4d44729dbc16709d3e47fc28bf40d3fefe726489"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 614505621863127
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 43583514, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285764, 'matching_hash': '8748c624c8dfcb5e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '614505622', 'validation_error': 'Invalid routing number checksum'}}}