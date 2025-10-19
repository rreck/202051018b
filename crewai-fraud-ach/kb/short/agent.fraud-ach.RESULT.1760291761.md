```json
{
  "id": "5d9070761f24b5ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291761,
  "host_pid": "9e6742732c60:1",
  "hash": "b75e703e17eafd30a4df9cc41e8da0746808ace2e1908ad843042e0709fdb462",
  "cid": "QmV1b75e703e17eafd30a4df9cc41e8da0746808ace2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291761,
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
      "evaluated_at": 1760291761
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
  "sig": "4103c5aa0ffa91f203a15afa8f3c8199e365e8abc5c542db6415a250f0dcca16"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 272809904666410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 56590352, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285765, 'matching_hash': 'b8be43189937b834'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '272809901', 'validation_error': 'Invalid routing number checksum'}}}