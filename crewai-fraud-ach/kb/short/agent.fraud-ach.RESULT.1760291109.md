```json
{
  "id": "c50dbd9acd77620d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291109,
  "host_pid": "9e6742732c60:1",
  "hash": "c24a52715f4c67743b8726e1b58717226f58c4ba8d07e7db2cd6a534b4cb8121",
  "cid": "QmV1c24a52715f4c67743b8726e1b58717226f58c4ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291109,
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
      "evaluated_at": 1760291109
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
  "sig": "0d1d9098d67671927b6c83ea38cd4a03a7d215e12eed190fdde1646b4dde99b4"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 671070000820328
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 54405270, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760284979, 'matching_hash': '6a7cc3d9f67da590'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '671070002', 'validation_error': 'Invalid routing number checksum'}}}