```json
{
  "id": "1894134531e47250",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293287,
  "host_pid": "9e6742732c60:1",
  "hash": "653a091931d575e7ce8806cce20576a443ac7040c33f99b0b664e56f261ca0e0",
  "cid": "QmV1653a091931d575e7ce8806cce20576a443ac7040",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293287,
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
      "evaluated_at": 1760293287
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
  "sig": "44806a8183a868c02e2addc85d92b6afde67f5978b76c3ae24d1fb612f8123dd"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 478694940117269
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 41628300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285764, 'matching_hash': 'c8ebc968ccc74844'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '478694940', 'validation_error': 'Invalid routing number checksum'}}}