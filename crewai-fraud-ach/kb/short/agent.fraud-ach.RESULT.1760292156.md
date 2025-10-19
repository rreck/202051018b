```json
{
  "id": "9a2fb0e5dfcefa74",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292156,
  "host_pid": "9e6742732c60:1",
  "hash": "b1f9e2b49a1d6255d78aedf74b3081bee2ba3ae131ba7f589e6e0a272cbb15c8",
  "cid": "QmV1b1f9e2b49a1d6255d78aedf74b3081bee2ba3ae1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292156,
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
      "evaluated_at": 1760292156
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
  "sig": "e9d9909da7ad628e61504c95164669d2bb91c9ff11900c5f5ba7db8621828172"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 735962402542057
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 84718050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285764, 'matching_hash': '8fcdc870d029f888'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '735962404', 'validation_error': 'Invalid routing number checksum'}}}