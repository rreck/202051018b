```json
{
  "id": "7502d53900523103",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291873,
  "host_pid": "9e6742732c60:1",
  "hash": "e447784203fe00adfde7a1b7f876ebfca1dcaa00682ea61a41feb83a3ab0d4e2",
  "cid": "QmV1e447784203fe00adfde7a1b7f876ebfca1dcaa00",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291873,
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
      "evaluated_at": 1760291873
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
  "sig": "3e5303030b60596dc2a233e77b2a90d949f3d4b5347eed4fea5ee18efe72a3b3"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 728187407566692
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 86543925, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285764, 'matching_hash': '1da2d57caa7d5158'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '728187403', 'validation_error': 'Invalid routing number checksum'}}}