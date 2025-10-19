```json
{
  "id": "48e5a91b89a384f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290352,
  "host_pid": "9e6742732c60:1",
  "hash": "7d770e6e23710e1a598e84d72bc630ce26e302ed722d9eda869d412da882fbda",
  "cid": "QmV17d770e6e23710e1a598e84d72bc630ce26e302ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290352,
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
      "evaluated_at": 1760290352
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
  "sig": "cc2944a8107003d98d349757e07e8a00fb1ba0a6cdc9483e7eb36c54422a62db"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 443655357779767
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 54951364, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285764, 'matching_hash': 'b8048cbf6aca9902'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '443655354', 'validation_error': 'Invalid routing number checksum'}}}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}