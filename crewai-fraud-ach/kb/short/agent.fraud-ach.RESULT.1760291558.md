```json
{
  "id": "f96afab44d1d8380",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291558,
  "host_pid": "9e6742732c60:1",
  "hash": "462a5df8219f285ff40eee31d250b10bb99130d0c1b1ae31513cc3219a40c495",
  "cid": "QmV1462a5df8219f285ff40eee31d250b10bb99130d0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291558,
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
      "evaluated_at": 1760291559
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
  "sig": "55b6e0b45b42de23a1f3e24b72616fc87eed072898136af762248a85fa5d88dd"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 987899138590267
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 79070270, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285763, 'matching_hash': '4a74fde2b8c56926'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '987899137', 'validation_error': 'Invalid routing number checksum'}}}