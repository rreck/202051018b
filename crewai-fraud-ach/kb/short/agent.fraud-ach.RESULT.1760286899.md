```json
{
  "id": "d46f9d1f9cc62733",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286899,
  "host_pid": "9e6742732c60:1",
  "hash": "ca6f56e53bad473f1e115846b1bbf7d96dada62e8227fd1b1d423be9a0081cc2",
  "cid": "QmV1ca6f56e53bad473f1e115846b1bbf7d96dada62e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286899,
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
      "evaluated_at": 1760286899
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
  "sig": "d114d004b3cf2b2a62a4ff1db8f1aadebe5141bb530c349eb895dbc66b507fc5"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 818309298369568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 19315510, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285765, 'matching_hash': '9e3984c977816ea5'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818309298', 'validation_error': 'Invalid routing number checksum'}}}