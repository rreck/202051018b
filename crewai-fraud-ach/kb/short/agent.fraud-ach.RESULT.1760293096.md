```json
{
  "id": "8522f03719d71c0f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293096,
  "host_pid": "9e6742732c60:1",
  "hash": "20f33269b7240dc5be66e35443063e4726e05015cbdb78e40703fcf5c1dbe17e",
  "cid": "QmV120f33269b7240dc5be66e35443063e4726e05015",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293096,
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
      "evaluated_at": 1760293096
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
  "sig": "577ee5fe586c25c83e01258fad05ec2a3b63142d914ecf8ad24a94d3842dfc68"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 109883193945676
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 63534210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285765, 'matching_hash': '153e74d04ee716fe'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '109883192', 'validation_error': 'Invalid routing number checksum'}}}