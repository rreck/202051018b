```json
{
  "id": "0c60452ebeaea82b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291530,
  "host_pid": "9e6742732c60:1",
  "hash": "69aa7ad370a9ff8829bd6339567b14ae39d6a701a0488ccabe35d82d7d5524b0",
  "cid": "QmV169aa7ad370a9ff8829bd6339567b14ae39d6a701",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291530,
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
      "evaluated_at": 1760291530
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
  "sig": "5a3a94d8c2da8be906c979fb41996ffda7a3185b554566a83f61185dbbb67937"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 443655357779767
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 65718861, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285764, 'matching_hash': 'b8048cbf6aca9902'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '443655354', 'validation_error': 'Invalid routing number checksum'}}}