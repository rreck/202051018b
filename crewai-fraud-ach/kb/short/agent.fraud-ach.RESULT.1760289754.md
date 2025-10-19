```json
{
  "id": "bb55384370998fc6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289754,
  "host_pid": "9e6742732c60:1",
  "hash": "3ff7cfaeb465e1d5fb5d05239fe413f0a288c00d3c88c5f3bd58e61e18dd995e",
  "cid": "QmV13ff7cfaeb465e1d5fb5d05239fe413f0a288c00d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289754,
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
      "evaluated_at": 1760289754
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
  "sig": "aaad98770a7136679c6697393163bdf14c3271fea7df7bf03ab1e8bf0b355840"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 529024316192383
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 33400092, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285764, 'matching_hash': 'dc6c8a77c50d9997'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '529024315', 'validation_error': 'Invalid routing number checksum'}}}