```json
{
  "id": "e3b3c4caee3fc3ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292457,
  "host_pid": "9e6742732c60:1",
  "hash": "f47a505b77486f7ed36cf37445a91ab77bf5cf61637a533721bd3d40202896f6",
  "cid": "QmV1f47a505b77486f7ed36cf37445a91ab77bf5cf61",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292457,
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
      "evaluated_at": 1760292457
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
  "sig": "bad8415372e9e0bebe015551a3bbe07764f4aa039f73cfdd51a8102132d1dc85"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 020899457068496
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 78093774, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285764, 'matching_hash': '41b228ccdaf61559'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '020899456', 'validation_error': 'Invalid routing number checksum'}}}