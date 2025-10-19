```json
{
  "id": "6af51544692ee242",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287558,
  "host_pid": "9e6742732c60:1",
  "hash": "5dffed4b58813b3f4200401b9712761b60ce168ef6e2c87699a926eae021f6ea",
  "cid": "QmV15dffed4b58813b3f4200401b9712761b60ce168e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287558,
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
      "evaluated_at": 1760287558
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
  "sig": "89dfe7a9d71724ce3ec0f20277a3e2e1bc7310025af7ee44d2a03494e409781c"
}
```

Fraud detected: invalid_routing (score: 86)
Transaction: 589241761167275
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 20071296, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285765, 'matching_hash': 'a1dced1ef969015f'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '589241760', 'validation_error': 'Invalid routing number checksum'}}}