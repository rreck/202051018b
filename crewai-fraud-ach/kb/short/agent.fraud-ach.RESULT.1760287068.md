```json
{
  "id": "17f6d223be34de26",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287068,
  "host_pid": "9e6742732c60:1",
  "hash": "d5aa32e4c54ce2a359634e737abb9c704174b0df0de5fcaf9e3cb489ab3eb349",
  "cid": "QmV1d5aa32e4c54ce2a359634e737abb9c704174b0df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287068,
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
      "evaluated_at": 1760287068
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
  "sig": "e160b987b9124d168113af756f994d03cf2e7aa1eab63151f4db51578f4e4f9b"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 728187407566692
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 21986835, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285764, 'matching_hash': '1da2d57caa7d5158'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '728187403', 'validation_error': 'Invalid routing number checksum'}}}