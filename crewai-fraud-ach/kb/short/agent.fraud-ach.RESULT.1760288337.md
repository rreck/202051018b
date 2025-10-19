```json
{
  "id": "1879de542b6e8d11",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288337,
  "host_pid": "9e6742732c60:1",
  "hash": "d68161c76e3b45e06c5e2d0b411bf5da7081bf919bc9a92d883bc284cb9ceb2e",
  "cid": "QmV1d68161c76e3b45e06c5e2d0b411bf5da7081bf91",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288337,
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
      "evaluated_at": 1760288337
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
  "sig": "966af2aacdb07db74662a8be378753590c2a0fecd3de93da7bdbfaadc9e9eafb"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 789209528183836
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 23467230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285765, 'matching_hash': 'e8f44f77b3005867'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '789209527', 'validation_error': 'Invalid routing number checksum'}}}