```json
{
  "id": "1e9e420de4807aa7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293667,
  "host_pid": "9e6742732c60:1",
  "hash": "63a097dafe77b5217ace102c41054849c540175d920f56c0762564e948846481",
  "cid": "QmV163a097dafe77b5217ace102c41054849c540175d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293667,
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
      "evaluated_at": 1760293667
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
  "sig": "56f1cf31edd6bc7a0434e8e4ee803050027753eaad3b6b2db5c183c6d528d928"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 443655357779767
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 82798339, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285764, 'matching_hash': 'b8048cbf6aca9902'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '443655354', 'validation_error': 'Invalid routing number checksum'}}}