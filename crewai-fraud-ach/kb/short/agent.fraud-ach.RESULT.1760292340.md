```json
{
  "id": "2858f7fe54e2a164",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292340,
  "host_pid": "9e6742732c60:1",
  "hash": "2337e7a48e0f60a8a0203bce7cae27eb056d965ab954e4966e4c3fed15df925d",
  "cid": "QmV12337e7a48e0f60a8a0203bce7cae27eb056d965a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292340,
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
      "evaluated_at": 1760292340
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
  "sig": "5e7f40b2b4cf26fa964bac59fdee66ba13cd9057bb97369c54301de578695e0d"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 264316140004295
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 75890685, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285765, 'matching_hash': 'f346c773c62e50ad'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '264316140', 'validation_error': 'Invalid routing number checksum'}}}