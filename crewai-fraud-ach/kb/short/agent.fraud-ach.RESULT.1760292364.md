```json
{
  "id": "bd538880f5cccb73",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292364,
  "host_pid": "9e6742732c60:1",
  "hash": "95b90f3592d655bb81db655c312fb4f2cdd4629c60680efe4bf5410b96995dff",
  "cid": "QmV195b90f3592d655bb81db655c312fb4f2cdd4629c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292364,
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
      "evaluated_at": 1760292364
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
  "sig": "4c56f5f854f8f645175845d564ca3ee62f9ec23a86940999ee12100dd9bf6fe5"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 586667912036113
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 96882408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': '105f91128dc7abfc'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '586667919', 'validation_error': 'Invalid routing number checksum'}}}