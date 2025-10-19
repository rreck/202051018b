```json
{
  "id": "5b5f1cb833be79df",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290863,
  "host_pid": "9e6742732c60:1",
  "hash": "39ac747390941a062c599eb6d0120e45d380abb83aaf0d006a0ee49b29c3ed5a",
  "cid": "QmV139ac747390941a062c599eb6d0120e45d380abb8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290863,
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
      "evaluated_at": 1760290863
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
  "sig": "721e12829d69381469d97d4b0ee98f18237d7be6e3d6d32eeb9ff519fbc977c9"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 291093508895399
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 76460188, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': 'b750a26a60b25ace'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '291093507', 'validation_error': 'Invalid routing number checksum'}}}