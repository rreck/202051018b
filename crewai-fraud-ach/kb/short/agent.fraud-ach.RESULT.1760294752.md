```json
{
  "id": "76c3085ef9e31e09",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294752,
  "host_pid": "9e6742732c60:1",
  "hash": "6e96eeca761bc4188718f9bd47d8fe1936fb7761c546c10869cd7e907f8ad1be",
  "cid": "QmV16e96eeca761bc4188718f9bd47d8fe1936fb7761",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294752,
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
      "evaluated_at": 1760294752
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
  "sig": "8e42243e9848e016a2c61f18cfb96f2efd0faab641b051dc82ebabdae9977fae"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 408733730305741
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 99057168, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '77eebc6eb9f79eeb'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '408733730', 'validation_error': 'Invalid routing number checksum'}}}