```json
{
  "id": "6745a011430f799f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290862,
  "host_pid": "9e6742732c60:1",
  "hash": "de0ce7175a6a8efe03bd62da986a47439a799c6ad99733bcbc3193076a65aceb",
  "cid": "QmV1de0ce7175a6a8efe03bd62da986a47439a799c6a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290862,
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
      "evaluated_at": 1760290862
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
  "sig": "1a938fcbe7b88a90ee2925a0c4e219a00922c7446e60cd231328b2054c7dd8dc"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 164661958921180
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 37697023, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': '1848c81652336fb1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '164661952', 'validation_error': 'Invalid routing number checksum'}}}