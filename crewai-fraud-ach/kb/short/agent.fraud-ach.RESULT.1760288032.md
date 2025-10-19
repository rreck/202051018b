```json
{
  "id": "33a8ae3c357c726a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288032,
  "host_pid": "9e6742732c60:1",
  "hash": "cc9e2182b993df02b7ddf6051c2df994fe9a87feb2ad3a51c62382890ec890c4",
  "cid": "QmV1cc9e2182b993df02b7ddf6051c2df994fe9a87fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288032,
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
      "evaluated_at": 1760288032
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
  "sig": "7aa708a9ef6ad8867f5fb29b84dc521c95b9ef3f3cdece0879d498272d036270"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 845955323982908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 28876320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285765, 'matching_hash': '603efe89834eadf7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '845955329', 'validation_error': 'Invalid routing number checksum'}}}