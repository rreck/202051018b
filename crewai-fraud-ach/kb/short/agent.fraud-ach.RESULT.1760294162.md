```json
{
  "id": "b6b6d44149b4984a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294162,
  "host_pid": "9e6742732c60:1",
  "hash": "98b5dc948f3d311a842e860f6054b7a66ccd28f7580b68b7beb8061db9ab049f",
  "cid": "QmV198b5dc948f3d311a842e860f6054b7a66ccd28f7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294162,
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
      "evaluated_at": 1760294162
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
  "sig": "5ad7d8634ac1e5b6d81fd310e80d37fbaeb36f6484a884ded6cca020528d53c8"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 929669860929959
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 48927903, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': 'bbfcfb9a6aef8521'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '929669867', 'validation_error': 'Invalid routing number checksum'}}}